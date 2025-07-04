import pandas as pd
from scipy.stats import ttest_ind
from itertools import combinations

inputFolder = '02-data'
U_VALUES = ['0.0', '0.2', '0.4', '0.6', '0.8']
NUMBER_OF_EXPERIMENTS = 30

if __name__ == "__main__":
    unadvised = pd.read_csv(f"{inputFolder}/unadvisedRewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]
    random = pd.read_csv(f"{inputFolder}/randomRewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]
    advised_all = pd.read_csv(f"{inputFolder}/allRewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]
    advised_holes_and_goal = pd.read_csv(f"{inputFolder}/holesAndGoalRewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]
    human_10 = pd.read_csv(f"{inputFolder}/human10RewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]
    human_5 = pd.read_csv(f"{inputFolder}/human5RewardData.csv", header=None).cumsum(axis=1).iloc[:, -1:]

    advised_mode = {
    "advised_all": advised_all,
    "advised_holes_and_goal": advised_holes_and_goal,
    "human_10": human_10,
    "human_5": human_5
    }

    unadvised_mode = {
    "random": random,
    "unadvised": unadvised
    }

    # UNADVISED VS RANDOM
    print("Unadvised vs Random")
    random_data = random.iloc[:, 0].values
    unadvised_data = unadvised.iloc[:, 0].values
    t_stat, p_val = ttest_ind(random_data, unadvised_data, equal_var=False)
    print(f"  p = {p_val:.4f}\n")

    # SYNTHETIC VS UNADVISED & RANDOM
    for advised_name, advised_df in advised_mode.items():
        for unadvised_name, unadvised_df in unadvised_mode.items():
            print(f"{advised_name.replace('_', ' ').title()} vs {unadvised_name.title()}")

            for index, u in enumerate(U_VALUES):
                start = index * NUMBER_OF_EXPERIMENTS
                end = start + NUMBER_OF_EXPERIMENTS

                advised_data = advised_df.iloc[start:end, 0].values
                unadvised_data = unadvised_df.iloc[:, 0].values 

                t_stat, p_val = ttest_ind(advised_data, unadvised_data, equal_var=False)
                print(f"  @u={u}: p = {p_val:.4f}")
            
            print()

    # SYNTHETIC VS SYNTHETIC
    advised_mode_pairs = list(combinations(advised_mode.keys(), 2))

    for advised1, advised2 in advised_mode_pairs:
        print(f"{advised1.replace('_', ' ').title()} vs {advised2.replace('_', ' ').title()}")
        
        for index, u in enumerate(U_VALUES):
            start = index * NUMBER_OF_EXPERIMENTS
            end = start + NUMBER_OF_EXPERIMENTS

            advised1_data = advised_mode[advised1].iloc[start:end, 0].values
            advised2_data = advised_mode[advised2].iloc[start:end, 0].values

            t_stat, p_val = ttest_ind(advised1_data, advised2_data, equal_var=False)
            print(f"  @u={u}: p = {p_val:.4f}")
        
        print()

           
    # SYNTEHTIC VS SYNTHETIC SELF
    for advised_name, advised_df in advised_mode.items():
        print(f"{advised_name.replace('_', ' ').title()}")

        for i, j in combinations(range(len(U_VALUES)), 2):
            u1, u2 = U_VALUES[i], U_VALUES[j]
            start1, end1 = i * NUMBER_OF_EXPERIMENTS, (i + 1) * NUMBER_OF_EXPERIMENTS
            start2, end2 = j * NUMBER_OF_EXPERIMENTS, (j + 1) * NUMBER_OF_EXPERIMENTS

            data_u1 = advised_df.iloc[start1:end1, 0].values
            data_u2 = advised_df.iloc[start2:end2, 0].values

            t_stat, p_val = ttest_ind(data_u1, data_u2, equal_var=False)
            print(f"  @u={u1} vs @u={u2}: p = {p_val:.4f}")
        
        print()
