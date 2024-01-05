```
python -m venv hf_ojas_explore
source hf_ojas_explore/bin/activate
```

```
python -m pip install --upgrade pip
pip install --upgrade-strategy eager "optimum[openvino,nncf,diffusers]"
```

```
bash hf_download.sh AshanGimhana/llama2-chat-ashan-QQ /home/u01/dlworkbench/65976d4563f73eebf594861d
```

```
bash hf_benchmark_question_answering.sh AshanGimhana/llama2-chat-ashan-QQ Who\ is\ Harry\ Potter? 1000 The\ Harry\ Potter\ universe\ is\ a\ richly\ detailed,\ magical\ world\ created\ by\ J.K.\ Rowling,\ centered\ around\ a\ young\ wizard\ named\ Harry\ Potter.\ It\ unfolds\ at\ Hogwarts\ School\ of\ Witchcraft\ and\ Wizardry,\ where\ Harry\ discovers\ his\ heritage\ and\ battles\ the\ dark\ wizard\ Voldemort.\ With\ its\ unique\ blend\ of\ magic,\ friendship,\ and\ courage,\ the\ series\ has\ captivated\ audiences\ worldwide,\ creating\ a\ vast,\ immersive\ lore\ that\ includes\ magical\ creatures,\ ancient\ spells,\ and\ a\ complex\ society\ hidden\ from\ the\ non-magical\ world.\ It\ is\ a\ tale\ of\ good\ versus\ evil,\ personal\ growth,\ and\ the\ power\ of\ love\ and\ friendship. /home/u01/dlworkbench/65976d4563f73eebf594861d
```