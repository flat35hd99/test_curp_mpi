from scipy import stats
import matplotlib.pyplot as plt


def load_time(f):
    """Load result of joblog on ims

    Args:
        f (str): file path

    Returns:
        List of seconds of elaps: Unit is second
    """
    time_list = []
    with open(f, mode="r") as f:
        for l in f.readlines():
            time = l.strip()
            hours, minutes, seconds = time.split(":")
            time_list.append(int(hours) * 3600 + int(minutes) * 60 + int(seconds))
    return time_list


def main():
    modes = ["r", "w", "rw"]
    _, ax = plt.subplots()
    ax.grid(which="major", axis="y", alpha=0.8)

    for mode, second_list in [
        (mode, load_time(f"results/t_{mode}_RAM.dat")) for mode in modes
    ]:

        mean = stats.tmean(second_list)
        ax.bar(x=mode, height=mean, label=f"Use RAM for {mode}")
        ax.errorbar(x=mode, y=mean, yerr=stats.sem(second_list), color="black")

    plt.legend()
    plt.savefig("results/barplot.png")


if __name__ == "__main__":
    main()
