import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum

inputFolder = './01-data'
outputFolder = './03-results'

class PlotType(Enum):
    ADVISED_ALL = f"{inputFolder}/advisedAll.csv"
    ADVISED_HOLES_AND_GOAL = f"{inputFolder}/advisedHolesAndGoal.csv"
    ADVISED_HUMAN_10 = f"{inputFolder}/advisedHuman10.csv"
    ADVISED_HUMAN_5 = f"{inputFolder}/advisedHuman5.csv"
    COOP10 = f"{inputFolder}/advisedCoop10.csv"
    COOP5 = f"{inputFolder}/advisedCoop5.csv"

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

def process_advised_synthetic(df, u_values):
    average_cumulative_reward_dict = {}
    for i, u in enumerate(u_values):
        group = df.iloc[i::len(u_values)].reset_index(drop=True)
        cumulative_sum = group.cumsum(axis=1)
        average_cumulative_reward = cumulative_sum.mean(axis=0)
        average_cumulative_reward_dict[u] = average_cumulative_reward
    average_cumulative_reward_df = pd.DataFrame.from_dict(average_cumulative_reward_dict, orient='index')
    average_cumulative_reward_df.columns = range(average_cumulative_reward_df.shape[1])
    return average_cumulative_reward_df

def process_advised_human(df):
    midpoint = len(df) // 2
    sequential, parallel= df.iloc[:midpoint], df.iloc[midpoint:]

    cumulative_first = sequential.cumsum(axis=1)
    average_sequential = cumulative_first.mean(axis=0)

    cumulative_second = parallel.cumsum(axis=1)
    average_parallel = cumulative_second.mean(axis=0)

    df = pd.DataFrame([average_sequential, average_parallel])
    df.insert(0, 'Type', ['sequential', 'parallel'])

    return df

def process_unadvised(df):
    cumulative = df.cumsum(axis=1)
    average = cumulative.mean(axis=0)
    return pd.DataFrame([average])

def plot_synthetic(random_processed, unadvised_processed, advised_processed, title, save, show, titles):
    import matplotlib.pyplot as plt

    def plot_variant(ax, yscale='linear'):
        lines, labels = [], []
        for idx, row in advised_processed.iterrows():
            line, = ax.plot(row, label=f'Advised u={idx}')
            lines.append(line)
            labels.append(f'Advised u={idx}')

        line_no_advice, = ax.plot(unadvised_processed.iloc[0], label='No advice', color='black', linestyle='--')
        lines.append(line_no_advice)
        labels.append('No advice')

        line_random, = ax.plot(random_processed.iloc[0], label='Random', color='black', linestyle=':')
        lines.append(line_random)
        labels.append('Random')

        if titles:
            ax.set_title(f"Synthetic: {title} ({yscale} scale)")
        ax.set_xlabel('Episode')
        ax.set_ylabel('Cumulative Reward')
        ax.set_yscale(yscale)
        ax.set_ylim([1 if yscale == 'log' else 0, 10000])

        legend_loc = 'lower right' if yscale == 'log' else 'upper left'
        ax.legend(lines, labels, loc=legend_loc)

    # Linear plot
    fig_linear, ax_linear = plt.subplots(figsize=(8, 6))
    plot_variant(ax_linear, yscale='linear')
    plt.tight_layout()
    if save:
        fig_linear.savefig(f"{outputFolder}/{title}_synthetic_linear.pdf", bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close(fig_linear)

    # Log plot
    fig_log, ax_log = plt.subplots(figsize=(8, 6))
    plot_variant(ax_log, yscale='log')
    plt.tight_layout()
    if save:
        fig_log.savefig(f"{outputFolder}/{title}_synthetic_log.pdf", bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close(fig_log)


def plot_human(random_processed, unadvised_processed, advised_processed, title, save, show, titles):
    import matplotlib.pyplot as plt

    def plot_variant(ax, yscale='linear'):
        lines, labels = [], []
        for _, row in advised_processed.iterrows():
            label = row['Type']
            line, = ax.plot(row[1:], label=label)
            lines.append(line)
            labels.append(label)

        line_no_advice, = ax.plot(unadvised_processed.iloc[0], label='No advice', color='black', linestyle='--')
        lines.append(line_no_advice)
        labels.append('No advice')

        line_random, = ax.plot(random_processed.iloc[0], label='Random', color='black', linestyle=':')
        lines.append(line_random)
        labels.append('Random')

        if titles:
            ax.set_title(f"Human: {title} ({yscale} scale)")
        ax.set_xlabel('Episode')
        ax.set_ylabel('Cumulative Reward')
        ax.set_yscale(yscale)
        ax.set_ylim([1 if yscale == 'log' else 0, 10000])

        legend_loc = 'lower right' if yscale == 'log' else 'upper left'
        ax.legend(lines, labels, loc=legend_loc)

    # Linear plot
    fig_linear, ax_linear = plt.subplots(figsize=(8, 6))
    plot_variant(ax_linear, yscale='linear')
    plt.tight_layout()
    if save:
        fig_linear.savefig(f"{outputFolder}/{title}_human_linear.pdf", bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close(fig_linear)

    # Log plot
    fig_log, ax_log = plt.subplots(figsize=(8, 6))
    plot_variant(ax_log, yscale='log')
    plt.tight_layout()
    if save:
        fig_log.savefig(f"{outputFolder}/{title}_human_log.pdf", bbox_inches='tight')
    if show:
        plt.show()
    else:
        plt.close(fig_log)


def process_and_plot(plot_type: PlotType, save=False, show=True, titles=True):
    random_data = pd.read_csv(f'{inputFolder}/random.csv', header=None) 
    random_processed = process_unadvised(random_data)

    unadvised_data = pd.read_csv(f'{inputFolder}/unadvised.csv', header=None) 
    unadvised_processed = process_unadvised(unadvised_data)

    if plot_type in [PlotType.ADVISED_ALL, PlotType.ADVISED_HOLES_AND_GOAL, PlotType.ADVISED_HUMAN_10, PlotType.ADVISED_HUMAN_5]:
        advised_data = pd.read_csv(plot_type.value, header=None)
        u_values = [0.0, 0.2, 0.4, 0.6, 0.8]
        advised_processed = process_advised_synthetic(advised_data, u_values)
        plot_synthetic(random_processed, unadvised_processed, advised_processed, plot_type.name, save=save, show=show, titles=titles)
    else:
        advised_data = pd.read_csv(plot_type.value, header=None)
        advised_processed = process_advised_human(advised_data)
        plot_human(random_processed, unadvised_processed, advised_processed, plot_type.name, save=save, show=show, titles=titles)

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

    show = input("Show plots? (y/n): ") == 'y'

    save = input("Save plots? (y/n): ") == 'y'

    titles = input("Show plot titles? (y/n): ") == 'y'

    try:
        process_and_plot(plot_type, save=save, show=show, titles=titles)
    except FileNotFoundError:
        print(f"Error: File '{plot_type}' not found.")

