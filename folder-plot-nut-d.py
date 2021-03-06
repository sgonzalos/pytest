print("==== START ====")
print("==== IMPORT ====")

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

# ====== fn_plot ====== 
def fn_plot(filename):
    #print(filename)
    #print("==== READ CSV ====")
    
    df = pd.read_csv(filename,skiprows=6,nrows=1,header=None)
    ST_ANG_TRQ = df[25][0]
    END_ANG=df[19][0]
    END_TRQ=df[18][0]
    
    df = pd.read_csv(filename,skiprows=8,usecols=[0,2],names=("TRQ","ANG"))
    #MAX_ANG = df.max()["ANG"]
    index = df.query("TRQ == @ST_ANG_TRQ").index[0]
    #df["ANG"][index]
    df["ANG"] = df["ANG"] - df["ANG"][index]
    
    DEL_IND = df.query("TRQ == @END_TRQ").index.max()
    
    df_new = df.drop(df.index[DEL_IND+1:])
    
    #print("==== PLOT ====")
    fig, ax = plt.subplots()
    ax.plot(df_new["ANG"],df_new["TRQ"])
    #ALL file
    axall.plot(df_new["ANG"],df_new["TRQ"])

    ax.set_xlim([-25,45])
    ax.set_ylim([0,80])

    ax.grid()
    ax.set(xlabel = 'Angle(deg)', ylabel = 'Torque(Nm)',
           title = os.path.basename(filename).replace(" ",""))
    fig.savefig(filename.replace(" ","")+".png")
    plt.close(fig)
# ====== fn_plot ====== 



directory = "data-d"

# ====== ALL SETTING ====== 
figall, axall = plt.subplots()
axall.set_xlim([-25,45])
axall.set_ylim([0,80])

axall.grid()
axall.set(xlabel = 'Angle(deg)', ylabel = 'Torque(Nm)',
       title = "ALL")
# ====== ALL SETTING ====== 

for filename in tqdm(glob.glob(directory + '/*.csv')):
    fn_plot(filename)

figall.savefig(directory + "\\" + "all"+".png")

print("==== END SCRIPT ====")
