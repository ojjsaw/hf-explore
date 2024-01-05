import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid_url(href):
            # not a valid URL
            continue
        if domain_name not in href:
            # external link
            continue
        urls.add(href)
    return urls

def crawl(url):
    """
    Crawls a web page and extracts all links.
    """
    links = get_all_website_links(url)
    return links

def extract_file_size(input_string):
    # Regex pattern to match strings like '137 MB', '2 GB', '1024 KB', etc.
    file_size_pattern = re.compile(r'(\d+(\.\d+)?)\s*(GB|MB|KB)', re.IGNORECASE)

    # Search for the pattern in the input string
    match = file_size_pattern.search(input_string)

    # If a match is found, return the file size and unit
    if match:
        # Extracting the size and unit from the match object
        size = match.group(1)  # The numeric part of the file size
        unit = match.group(3).upper()  # The unit part (GB, MB, KB), converted to uppercase for consistency
        return size, unit
    
def find_bin_lines(url):
    """
    Finds and prints lines containing '.bin' in the webpage text.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            if ".bin" in href:
                if "download=true" in href:
                    modified_string = href.replace("?download=true", "")
                    size, unit = extract_file_size(a_tag.text)
                    final_string = size + unit + " | " + modified_string
                    print(final_string)

top_url = "https://huggingface.co/Kano001/Dreamshaper_v7-Openvino/tree/main"

# Crawl the website starting from the top URL
crawled_urls = crawl(top_url)

# For each URL, find and print lines containing '.bin'
for url in crawled_urls:
    find_bin_lines(url)
