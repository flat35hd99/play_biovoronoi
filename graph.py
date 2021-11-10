import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv("./output.csv")
    plt.plot(df.volume[0:36])
    plt.show()


if __name__ == "__main__":
    main()
