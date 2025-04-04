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
  - `randomRewardData.csv` - Cumulative rewards of a random-walk agent
  - `unadvisedRewardData.csv` - Cumulative rewards of an unadvised (but not random) agent
  - `allRewardData.csv` - Cumulative rewards of an agent advised by information about every state
  - `holesAndGoalRewardData.csv` - Cumulative rewards of an agent advised by information about terminating states (negative termination and positive termination, i.e., goal)
  - `human10RewardData.csv` - Cumulative rewards of an agent advised by a single human advisor about 10% of the states
  - `human5RewardData.csv` - Cumulative rewards of an agent advised by a single human advisor about 5% of the states
  - `coop10SequentialRewardData.csv` - Cumulative rewards of an agent advised by two cooperating human advisors (one located at top left, one located at bottom right) who each advise about 10% of the states 
  - `coop10ParallelRewardData.csv` - Cumulative rewards of an agent advised by two cooperating human advisors (one located at top right, one located at bottom left) who each advise about 10% of the states
  - `coop5SequentialRewardData.csv` - Cumulative rewards of an agent advised by two cooperating human advisors (one located at top left, one located at bottom right) who each advise about 5% of the states
  - `coop5ParallelRewardData.csv` - Cumulative rewards of an agent advised by two cooperating human advisors (one located at top right, one located at bottom left) who each advise about 5% of the states
- `02-scripts` - Contains a Python script to generate the plots in the `03-results` folder
- `03-results` - Contains plots that are used in the publication

## Experiment setup

### Problem
The map used in the experiments:

![The map used in the experiments](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/00-settings/lake-12x12-seed63.png)

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

### Oracle and single human

<table>
    <thead>
        <tr>
            <th></th>
            <th colspan="2">Oracle</th>
            <th colspan="2">Single human</th>
        </tr>
        <tr>
            <th>u</th>
            <th>100%</th>
            <th>20%</th>
            <th>10%</th>
            <th>5%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>0.0</td>
            <td>9900.100</td>
            <td>9914.900</td>
            <td>9768.000</td>
            <td>8051.300</td>
        </tr>
        <tr>
            <td>0.2</td>
            <td>9685.900</td>
            <td>8948.933</td>
            <td>8538.266</td>
            <td>5287.833</td>
        </tr>
        <tr>
            <td>0.4</td>
            <td>7974.066</td>
            <td>5216.433</td>
            <td>6121.033</td>
            <td>2134.966</td>
        </tr>
        <tr>
            <td>0.6</td>
            <td>5094.333</td>
            <td>2177.633</td>
            <td>3488.700</td>
            <td>2246.733</td>
        </tr>
        <tr>
            <td>0.8</td>
            <td>1502.500</td>
            <td>523.633</td>
            <td>1126.300</td>
            <td>1108.666</td>
        </tr>
    </tbody>
</table>



#### Oracle - 100% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_allRewardData_linear.png" alt="Oracle 100% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_allRewardData_log.png" alt="Oracle 100% - Log scale" width="300">

#### Oracle - 20% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_holesAndGoalRewardData_linear.png" alt="Oracle 20% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_holesAndGoalRewardData_log.png" alt="Oracle 20% - Log scale" width="300">

#### Single human - 10% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_human10RewardData_linear.png" alt="Human 10% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_human10RewardData_log.png" alt="Human 10% - Log scale" width="300">

#### Single human - 5% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_human5RewardData_linear.png" alt="Human 5% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_human5RewardData_log.png" alt="Human 5% - Log scale" width="300">

### Two cooperating humans

<table>
    <thead>
        <tr>
            <th></th>
            <th>10%</th>
            <th>5%</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sequential</td>
            <td>8078.366</td>
            <td>5037.066</td>
        </tr>
        <tr>
            <td>Parallel</td>
            <td>5429.466</td>
            <td>4130.666</td>
        </tr>
    </tbody>
</table>

#### Two cooperating humans - 10% advice quota each (total 20%)
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_coop10RewardData_linear.png" alt="Two coopearting human with 10% each - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_coop10RewardData_log.png" alt="Two coopearting human with 10% each - Log scale" width="300">

#### Two cooperating humans - 5% advice quota each (total 10%)
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_coop5RewardData_linear.png" alt="Two coopearting human with 5% each - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/03-results/png/plot_coop5RewardData_log.png" alt="Two coopearting human with 5% each - Log scale" width="300">
