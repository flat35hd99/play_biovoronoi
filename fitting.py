import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def fitting(a, b, start=-200, step_width=1, last=+200):
    """Fitting two data by up/down

    Args:
        a (array like): array like data
        b (array like): array like data
    """
    best_shift = None
    best_rms = None
    history = []
    print("original RMS is:", np.average(np.sqrt(np.absolute(a - b))))
    for shift in range(start, last, step_width):
        rms = np.average(np.sqrt(np.absolute(a - b + shift)))
        if best_rms is None or rms < best_rms:
            best_shift = shift
            best_rms = rms
            history.append(rms)
    return best_shift, best_rms, history

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
    
    shift, rms, history = fitting(vldp_df["VOLUME"].values, voronoi_df["volume"].values)
    print(f"Best rms is {rms}")
    print(f"History is {history}")
    voronoi_df["volume"] = voronoi_df["volume"] + shift
    
    fig, ax = plt.subplots()
    ax.plot(residue_id, voronoi_df["volume"], label="voronoi")
    ax.plot(residue_id, vldp_df["VOLUME"], label="vldp")
    ax.legend()
    

    plt.savefig("fitting.png")

    fig, ax = plt.subplots()
    ax.set_title("Absolute ratio")
    ax.plot(residue_id, np.absolute((vldp_df["VOLUME"] - voronoi_df["volume"])/vldp_df["VOLUME"]), label="raio")
    ax.legend()

    plt.savefig("fitting_ratio.png")

if __name__ == "__main__":
    main()