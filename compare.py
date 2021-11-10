import matplotlib.pyplot as plt
import pandas as pd


def main():
    voronoi_df = pd.read_csv("./output.csv")[0:36]
    vldp_df = pd.read_table("./vldp.dat", delim_whitespace=True, header=8)
    vldp_df.columns = [
        "MOL",
        "NUMMOL",
        "ATM",
        "NUMATM",
        "X",
        "Y",
        "Z",
        "AREA",
        "VOLUME",
        "LOCUS",
        "empty"
    ]
    vldp_df = vldp_df.groupby("NUMMOL", as_index=False).sum()
    
    residue_id = voronoi_df["residue_id"]

    fig, ax = plt.subplots()
    ax.plot(residue_id, voronoi_df["volume"], label="voronoi")
    ax.plot(residue_id, vldp_df["VOLUME"], label="vldp")
    ax.legend()
    
    plt.savefig("real.png")

    fig1, ax1 = plt.subplots()
    ax1.plot(residue_id, (voronoi_df["volume"] - vldp_df["VOLUME"])/vldp_df["VOLUME"], label="vldp")
    ax1.legend()
    
    plt.savefig("ratio.png")

if __name__ == "__main__":
    main()
