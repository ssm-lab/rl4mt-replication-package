# Replication package

### for the paper _Complex Model Transformations by Reinforcement Learning with Uncertain Human Guidance_.
(Accepted for [MODELS 2025](https://2025.models-conf.com/track/models-2025-research-papers).)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About
Model-driven engineering problems often require complex model transformations (MTs), i.e., MTs that are chained in extensive sequences. Pertinent examples of such problems include model synchronization, automated model repair, and design space exploration. Manually developing complex MTs is an error-prone and often infeasible process. Reinforcement learning (RL) is an apt way to alleviate these issues. In RL, an autonomous agent explores the state space through trial and error to identify beneficial sequences of actions, such as MTs. However, RL methods exhibit performance issues in complex problems. In these situations, human guidance can be of high utility. In this paper, we present an approach and technical framework for developing complex MT sequences through RL, guided by potentially uncertain human advice. Our framework allows user-defined MTs to be mapped onto RL primitives, and executes them as RL programs to find optimal MT sequences. Our evaluation shows that human guidance, even if uncertain, substantially improves RL performance, and results in more efficient development of complex MTs. Through a sensible trade-off between the certainty and timeliness of human advice, our method takes a firm step towards machine learning-driven human-in-the-loop engineering methods.

## Table of contents
- [Content description](README.md#Content-description)
- [Reproduction](README.md#Reproduction)
- [Replication](README.md#Replication)
- [Experiment setup](README.md#Experiment-setup)
- [Results](README.md#Results)

## Content description
- `01-advice` - Contains all the experimental artifacts and visualizations used in our experiments (map, advice files, and advice visualized on the map)
- `02-data` - Contains experimental data produced in accordance with the `Experiment settings`
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
- `03-analysis` - Contains Python analysis scripts to obtain the results in the `04-results` folder
- `04-results` - Contains the plots and statistical significance values that are used in the publication


## Reproduction
That is, repeating the original study's data analysis on the original study's data.

- For the charts, run `python .\03-analysis\plotting.py` from the root and follow the instructions. Results will be generated into `04-results` in two formats, in the respective `pdf` and `png` subfolders.
- For the significance tests, run `python .\03-analysis\t_test.py > 04-results/significance/results.txt` from the root. Results will be generated into `04-results/significance` in a textual tabular format.

**NOTE:** The above steps have been tested with `python>=3.8 && python<=3.13`.


## Replication
That is, repeating the original study by collecting new data and repeating the original study's analysis on the new data.

### Setting up Eclipse
For the following steps, refer to the tool's [official GitHub repository](https://github.com/ssm-lab/rl4mt).
1. Follow the setup steps of the tool.
2. Follow the setup steps of the Lake example.

### Obtaining experimental data
Data can be obtained by running experiments encoded in unit tests. Unit tests are parameterized with human advice found in the `01-advice` folder of this replication package.

To locate the unit tests, navigate to `https://github.com/ssm-lab/rl4mt/tree/main/tests/ca.mcmaster.ssm.rl4mt.examples.lake.tests/src/ca/mcmaster/ssm/rl4mt/examples/lake/tests` in the tool's [official GitHub repository](https://github.com/ssm-lab/rl4mt).

**NOTE:** The following steps take a long time (about half an hour each, depending on the hardware) to compute.

#### Random Agent
1. Run `LakeTestRandom.xtend`
2. Rename `rewardData.csv` to `randomRewardData.csv`

#### Unadvised Agent
1. Run `LakeTestUnadvised.xtend`
2. Rename `rewardData.csv` to `unadvisedRewardData.csv`

#### Oracle - 100% advice quota
In this experiment, a single *oracle* advisor gives advice about every tile.

1. In `LakeTestSingleAdvisor.xtend`, on line 233 change the `SingleExperimentMode` to `All`
	- `runAdvisedAgentSingleAdvisor(SingleExperimentMode.ALL)`
2. Save and run `LakeTestSingleAdvisor.xtend`
3. Rename `rewardData.csv` to `allRewardData.csv`

#### Oracle - 20% advice quota
In this experiment, a single *oracle* advisor gives advice about hole tiles and the goal tile (about 20% of the problem space).

1. In `LakeTestSingleAdvisor.xtend`, on line 233 change the `SingleExperimentMode` to `HOLES_AND_GOAL`
	- `runAdvisedAgentSingleAdvisor(SingleExperimentMode.HOLES_AND_GOAL)`
2. Save and run `LakeTestSingleAdvisor.xtend`
3. Rename `rewardData.csv` to `holesAndGoalRewardData.csv`

#### Single human - 10% advice quota
In this experiment, a single *human* advisor gives advice about 10% of the problem space.

1. In `LakeTestSingleAdvisor.xtend`, on line 233 change the `SingleExperimentMode` to `HUMAN10`
	- `runAdvisedAgentSingleAdvisor(SingleExperimentMode.HUMAN10)`
2. Save and run `LakeTestSingleAdvisor.xtend`
3. Rename `rewardData.csv` to `human10RewardData.csv`

#### Single human - 5% advice quota
In this experiment, a single *human* advisor gives advice about 5% of the problem space.

1. In `LakeTestSingleAdvisor.xtend`, on line 233 change the `SingleExperimentMode` to `HUMAN5`
	- `runAdvisedAgentSingleAdvisor(SingleExperimentMode.HUMAN5)`
2. Save and run `LakeTestSingleAdvisor.xtend`
3. Rename `rewardData.csv` to `human5RewardData.csv`

**NOTE:** The following data is only briefly mentioned in the paper, but not presented in detail due to the page limit.

#### Two cooperating humans - 10% advice quota each (total 20%) - Sequential guidance
In this experiment, two *human* advisors gives advice about 10% of the problem space each. The advisors are located in the top-left corner (start) and the bottom-right corner (goal) and give advice about their local environment. Therefore, the agent is first guided by the first advisor's input, and later, by the second advisor's input -- i.e., guidance is sequential.

1. In `LakeTestCoop.xtend`, on line 333 change the `CoopExperimentMode` to `SEQUENTIAL_10`
	- `runAdvisedAgentCoop(CoopExperimentMode.SEQUENTIAL_10)`
2. Save and run `LakeTestCoop.xtend`
3. Rename `rewardData.csv` to `coop10SequentialRewardData.csv`

#### Two cooperating humans - 10% advice quota each (total 20%) - Parallel guidance
In this experiment, two *human* advisors gives advice about 10% of the problem space each. The advisors are located in the bottom-left and the top-right corner and give advice about their local environment. Therefore, the agent is sometimes guided by the first advisor's input and sometimes, by the second advisor's input -- i.e., guidance is parallel.

1. In `LakeTestCoop.xtend`, on line 333 change the `CoopExperimentMode` to `PARALLEL_10`
	- `runAdvisedAgentCoop(CoopExperimentMode.PARALLEL_10)`
2. Save and run `LakeTestCoop.xtend`
3. Rename `rewardData.csv` to `coop10ParallelRewardData.csv`

#### Two cooperating humans - 5% advice quota each (total 10%) - Sequential guidance
In this experiment, two *human* advisors gives advice about 5% of the problem space each. The advisors are located in the top-left corner (start) and the bottom-right corner (goal) and give advice about their local environment. Therefore, the agent is first guided by the first advisor's input, and later, by the second advisor's input -- i.e., guidance is sequential.

1. In `LakeTestCoop.xtend`, on line 333 change the `CoopExperimentMode` to `SEQUENTIAL_5`
	- `runAdvisedAgentCoop(CoopExperimentMode.SEQUENTIAL_5)`
2. Save and run `LakeTestCoop.xtend`
3. Rename `rewardData.csv` to `coop5SequentialRewardData.csv`

#### Two cooperating humans - 5% advice quota each (total 10%) - Parallel guidance
In this experiment, two *human* advisors gives advice about 5% of the problem space each. The advisors are located in the bottom-left and the top-right corner and give advice about their local environment. Therefore, the agent is sometimes guided by the first advisor's input and sometimes, by the second advisor's input -- i.e., guidance is parallel.

1. In `LakeTestCoop.xtend`, on line 333 change the `CoopExperimentMode` to `PARALLEL_5`
	- `runAdvisedAgentCoop(CoopExperimentMode.PARALLEL_5)`
2. Save and run `LakeTestCoop.xtend`
3. Rename `rewardData.csv` to `coop5ParallelRewardData.csv`


## Experiment setup

### Problem
The map used in the experiments:

![The map used in the experiments](https://github.com/ssm-lab/rl4mt-replication-package/blob/main/01-advice/lake-12x12-seed63.png)

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
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_allRewardData_linear.png" alt="Oracle 100% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_allRewardData_log.png" alt="Oracle 100% - Log scale" width="300">

#### Oracle - 20% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_holesAndGoalRewardData_linear.png" alt="Oracle 20% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_holesAndGoalRewardData_log.png" alt="Oracle 20% - Log scale" width="300">

#### Single human - 10% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_human10RewardData_linear.png" alt="Human 10% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_human10RewardData_log.png" alt="Human 10% - Log scale" width="300">

#### Single human - 5% advice quota
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_human5RewardData_linear.png" alt="Human 5% - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_human5RewardData_log.png" alt="Human 5% - Log scale" width="300">

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
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_coop10RewardData_linear.png" alt="Two coopearting human with 10% each - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_coop10RewardData_log.png" alt="Two coopearting human with 10% each - Log scale" width="300">

#### Two cooperating humans - 5% advice quota each (total 10%)
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_coop5RewardData_linear.png" alt="Two coopearting human with 5% each - Linear scale" width="300">
<img src="https://github.com/ssm-lab/rl4mt-replication-package/blob/main/04-results/png/plot_coop5RewardData_log.png" alt="Two coopearting human with 5% each - Log scale" width="300">
