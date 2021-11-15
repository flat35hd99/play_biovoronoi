import pandas as pd
from canalyse.parser import VldpVolumeParser, VldpVolumeFormatter

def main():
    voronoi_df = pd.read_csv("./output.csv")[0:36]
    vldp_df = VldpVolumeParser().run("./vldp.dat")
    vldp_df = VldpVolumeFormatter().run(vldp_df)
    
    print("sum of voronoi volume: ", voronoi_df["volume"].sum())
    print("sum of vldp server volume: ", vldp_df["volume"].sum())

if __name__ == '__main__':
    main()
    