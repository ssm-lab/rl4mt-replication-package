# Replication package

### for the paper _Complex Model Transformations by Reinforcement Learning with Uncertain Human Guidance_.

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## About
Model-driven engineering problems often require complex model transformations (MTs), i.e., MTs that are chained in extensive sequences. Pertinent examples of such problems include model synchronization, automated model repair, and design space exploration. Manually developing complex MTs is an error-prone and often infeasible process. Reinforcement learning (RL) is an apt way to alleviate these issues. In RL, an autonomous agent explores the state space through trial and error to identify beneficial sequences of actions, such as MTs. However, RL methods exhibit performance issues in complex problems. In these situations, human guidance can be of high utility. In this paper, we present an approach and technical framework for developing complex MT sequences through RL, guided by potentially uncertain human advice. Our framework allows user-defined MTs to be mapped onto RL primitives, and executes them as RL programs to find optimal MT sequences. Our evaluation shows that human guidance, even if uncertain, substantially improves RL performance, and results in more efficient development of complex MTs. Through a sensible trade-off between the certainty and timeliness of human advice, our method takes a firm step towards machine learning-driven human-in-the-loop engineering methods.

## Table of contents
- [Content description](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/README.md#Content-description)
- [Experiment setup](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/README.md#Experiment-setup)
- [Data replication steps](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/README.md#Data-replication-steps)
- [Results](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/README.md#Results)

## Content description
- `00-settings` - ${\color{red}\textbf{TODO}}$ this should be figured out
- `01-data` - Contains experimental data produced in accordance with the `Experiment settings`
  - `random.csv` - Cumulative rewards of a random-walk agent
  - `unadvised.csv` - Cumulative rewards of an unadvised (but not random) agent
  - `advisedAll.csv` - Cumulative rewards of an agent advised by information about every state
  - `advisedHolesAndGoal.csv` - Cumulative rewards of an agent advised by information about terminating states (negative termination and positive termination, i.e., goal)
- `02-scripts` - Contains a Python script to generate the plots in the `03-results` folder
- `03-results` - Contains plots that are used in the publication

## Experiment setup

### Problem
The map used in the experiments:

![The map used in the experiments](https://github.com/ssm-lab/rl4mt-replication-package/tree/main/00-settings/lake-12x12-seed63.png)

### Advice files
${\color{red}\textbf{TODO}}$

### Settings and hyperparameters

| Parameter  | Value |
| ------------- | ------------- |
| RL method | Discrete policy gradient |
| Learning rate ($\alpha$) | 0.9 |
| Discount factor ($\gamma$) | 1.0 |
| Number of episodes | 10000 |
| SL fusion operator | BCF |
| State-action space | 12x12x4 |
| Evaluated agent | {Random, Unadvised, Advised} |
| Source of advice | {Oracle, Single human, Cooperating humans} |
| Advice quota – Oracle | {100% ("All"), 20% ("Holes&Goal")} |
| Advice quota – Single human | {10%, 5%} |
| Advice quota – Cooperating humans | {10% each, 5% each} |
| Uncertainty - Oracle and Single human) | {0.2k ∣ k $\in$ 0..4} |
| Uncertainty – Cooperating humans | 2D Manhattan distance |
| Cooperative advice type | {Sequential cooperation, parallel cooperation} |

## Data replication steps
Run `python .\02-scripts\plotting.py` from the root and follow the instructions. Results will be generated into `03-results`.

## Results
