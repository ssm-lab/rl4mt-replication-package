import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
import os

inputFolder = '../01-data'
outputFolder = '../03-results'
MAX_NUMBER_OF_EXPERIMENTS = 30


class PlotType(Enum):
    ADVISED_ALL = f"{inputFolder}/allRewardData.csv"
    ADVISED_HOLES_AND_GOAL = f"{inputFolder}/holesAndGoalRewardData.csv"
    ADVISED_HUMAN_10 = f"{inputFolder}/human10RewardData.csv"
    ADVISED_HUMAN_5 = f"{inputFolder}/human5RewardData.csv"
    COOP10 = (f"{inputFolder}/coop10SequentialRewardData.csv",
              f"{inputFolder}/coop10ParallelRewardData.csv")
    COOP5 = (f"{inputFolder}/coop5SequentialRewardData.csv",
             f"{inputFolder}/coop5ParallelRewardData.csv")

    def is_synthetic(self):
        return self in {
            PlotType.ADVISED_ALL, PlotType.ADVISED_HOLES_AND_GOAL,
            PlotType.ADVISED_HUMAN_10, PlotType.ADVISED_HUMAN_5
        }

    @staticmethod
    def list_options():
        return [f"{i + 1}. {atype.name}" for i, atype in enumerate(PlotType)]

    @staticmethod
    def get_by_number(number):
        advised_types = list(PlotType)
        if 1 <= number <= len(advised_types):
            return advised_types[number - 1]
        else:
            raise ValueError("Invalid selection number.")


def process_unadvised(df):
    cumulative = df.cumsum(axis=1)
    average = cumulative.mean(axis=0)
    return pd.DataFrame([average])


def process_synthetic(df, u_values):
    total_rows = len(df)
    experiments_per_u = total_rows // len(u_values)

    average_cumulative_reward_dict = {}
    for i, u in enumerate(u_values):
        start_idx = i * experiments_per_u
        end_idx = (i + 1) * experiments_per_u
        group = df.iloc[start_idx:end_idx].reset_index(drop=True)

        cumulative_sum = group.cumsum(axis=1)
        average_cumulative_reward = cumulative_sum.mean(axis=0)
        average_cumulative_reward_dict[u] = average_cumulative_reward

    average_cumulative_reward_df = pd.DataFrame.from_dict(
        average_cumulative_reward_dict, orient='index')
    average_cumulative_reward_df.columns = range(
        average_cumulative_reward_df.shape[1])
    return average_cumulative_reward_df


def process_human(df):
    midpoint = len(df) // 2
    sequential, parallel = df.iloc[:midpoint], df.iloc[midpoint:]

    cumulative_first = sequential.cumsum(axis=1)
    average_sequential = cumulative_first.mean(axis=0)

    cumulative_second = parallel.cumsum(axis=1)
    average_parallel = cumulative_second.mean(axis=0)

    df = pd.DataFrame([average_sequential, average_parallel])
    df.insert(0, 'Type', ['sequential', 'parallel'])

    return df


def plot(random_processed, unadvised_processed, advised_processed, plot_type, save_plot, show_plot):
    if plot_type.is_synthetic():
        title = os.path.splitext(os.path.basename(plot_type.value))[0]
    else:
        title = os.path.splitext(os.path.basename(plot_type.value[0]))[0].replace("Sequential", "")

    def plot_variant(ax, yscale='linear'):
        lines, labels = [], []

        # advised
        if plot_type in [PlotType.ADVISED_ALL, PlotType.ADVISED_HOLES_AND_GOAL, PlotType.ADVISED_HUMAN_10, PlotType.ADVISED_HUMAN_5]:
            x_values = list(advised_processed.columns)
            for u_value, row in advised_processed.iterrows():
                line, = ax.plot(x_values, row.values,
                                label=f'Advised u={u_value:.1f}')
                lines.append(line)
                labels.append(f'Advised u={u_value:.1f}')
        else:
            for _, row in advised_processed.iterrows():
                label = row['Type']
                line, = ax.plot(row.iloc[1:], label=label)
                lines.append(line)
                labels.append(label)

        # unadvised
        line_no_advice, = ax.plot(
            unadvised_processed.columns, unadvised_processed.iloc[0], label='No advice', color='black', linestyle='--')
        lines.append(line_no_advice)
        labels.append('No advice')

        # random
        line_random, = ax.plot(
            random_processed.columns, random_processed.iloc[0], label='Random', color='black', linestyle=':')
        lines.append(line_random)
        labels.append('Random')

        ax.set_xlabel('Episode')
        ax.set_ylabel('Cumulative Reward')
        ax.set_yscale(yscale)
        ax.set_ylim([1 if yscale == 'log' else 0, 10000])
        legend_loc = 'lower right' if yscale == 'log' else 'upper left'
        ax.legend(lines, labels, loc=legend_loc)

    # linear
    fig_linear, ax_linear = plt.subplots(figsize=(8, 6))
    plot_variant(ax_linear, yscale='linear')
    plt.tight_layout()
    if save_plot:
        fig_linear.savefig(f"{outputFolder}/plot_{title}_linear.pdf", bbox_inches='tight')
    if show_plot:
        plt.show()
    else:
        plt.close(fig_linear)

    # log
    fig_log, ax_log = plt.subplots(figsize=(8, 6))
    plot_variant(ax_log, yscale='log')
    plt.tight_layout()
    if save_plot:
        fig_log.savefig(f"{outputFolder}/plot_{title}_log.pdf", bbox_inches='tight')
    if show_plot:
        plt.show()
    else:
        plt.close(fig_log)


def process_and_plot(plot_type: PlotType, save_plot=False, show_plot=True):
    random_data = pd.read_csv(f"{inputFolder}/randomRewardData.csv", header=None)
    random_processed = process_unadvised(random_data)

    unadvised_data = pd.read_csv(f"{inputFolder}/unadvisedRewardData.csv", header=None)
    unadvised_processed = process_unadvised(unadvised_data)

    if plot_type.is_synthetic():
        advised_data = pd.read_csv(plot_type.value, header=None)
        u_values = [0.0, 0.2, 0.4, 0.6, 0.8]
        advised_processed = process_synthetic(advised_data, u_values)
        plot(random_processed, unadvised_processed, advised_processed,
             plot_type, save_plot, show_plot)
    else:
        sequential_data = pd.read_csv(plot_type.value[0], header=None)
        parallel_data = pd.read_csv(plot_type.value[1], header=None)
        advised_data = pd.concat(
            [sequential_data, parallel_data], ignore_index=True)
        advised_processed = process_human(advised_data)
        plot(random_processed, unadvised_processed, advised_processed,
             plot_type, save_plot, show_plot)


if __name__ == "__main__":
    print("Select the advised data CSV file by number:")
    print("\n".join(PlotType.list_options()))

    while True:
        try:
            file_number = int(input("Enter number: "))
            plot_type = PlotType.get_by_number(file_number)
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 6.")

    show_plot = input("Show plots? (y/n): ") == 'y'

    save_plot = input("Save plots? (y/n): ") == 'y'

    try:
        process_and_plot(plot_type, save_plot=save_plot,
                         show_plot=show_plot)
    except FileNotFoundError:
        print(f"Error: File '{plot_type}' not found.")
