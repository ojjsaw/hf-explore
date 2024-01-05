```
python -m venv hf_ojas_explore
source hf_ojas_explore/bin/activate
```

```bash
mkdir my_venv
cd my_venv
touch Pipfile
export PIPENV_VENV_IN_PROJECT=1
mkdir .venv

### paste Pipefile config

pipenv install
```


```
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
optimum = {extras = ["openvino", "nncf", "diffusers"]}

[requires]
python_version = "3.8"
```

```bash
python -m pip install --upgrade pip
pipenv install --upgrade-strategy eager "optimum[openvino,nncf,diffusers]"
```

### Q&A
```
bash hf_download.sh AshanGimhana/llama2-chat-ashan-QQ test_project
```

```
bash hf_benchmark_question_answering.sh AshanGimhana/llama2-chat-ashan-QQ Who\ is\ Harry\ Potter? 1000 The\ Harry\ Potter\ universe\ is\ a\ richly\ detailed,\ magical\ world\ created\ by\ J.K.\ Rowling,\ centered\ around\ a\ young\ wizard\ named\ Harry\ Potter.\ It\ unfolds\ at\ Hogwarts\ School\ of\ Witchcraft\ and\ Wizardry,\ where\ Harry\ discovers\ his\ heritage\ and\ battles\ the\ dark\ wizard\ Voldemort.\ With\ its\ unique\ blend\ of\ magic,\ friendship,\ and\ courage,\ the\ series\ has\ captivated\ audiences\ worldwide,\ creating\ a\ vast,\ immersive\ lore\ that\ includes\ magical\ creatures,\ ancient\ spells,\ and\ a\ complex\ society\ hidden\ from\ the\ non-magical\ world.\ It\ is\ a\ tale\ of\ good\ versus\ evil,\ personal\ growth,\ and\ the\ power\ of\ love\ and\ friendship. test_project
```

### Text2IMG

```bash
bash hf_download.sh helenai/CompVis-stable-diffusion-v1-4-ov test_img_project
```

```bash

```