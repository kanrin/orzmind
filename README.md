# OrzMind

> based by [minimind](https://github.com/jingyaogong/minimind)  
> thanks everyone  

# About this repo
This repository is an engineering project I use to practice training LLMs. If needed, I recommend using [minimind](https://github.com/jingyaogong/minimind), which contains a lot of my personal thoughts and ideas.

In addition, this repository still follows the Apache License 2.0.

# Train Flow
Minimize the training.
```mermaid
graph LR

S(Start) --> P1[Pretrain]
P1 --> P2[SFT Train]
P2 --> E(End)
```
