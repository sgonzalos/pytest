print("==== START ====")
print("==== IMPORT ====")

import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# ====== fn_plot ====== 
def fn_plot(filename):
    print(filename)
    print("==== READ CSV ====")
    
    df = pd.read_csv(filename,skiprows=6,nrows=1,header=None)
    ST_ANG_TRQ = df[25][0]
    END_ANG=df[19][0]
    END_TRQ=df[18][0]
    
    df = pd.read_csv(filename,skiprows=8,usecols=[0,2],names=("TRQ","ANG"))
    MAX_ANG = df.max()["ANG"]
    
    df["ANG"] = df["ANG"] - (MAX_ANG - END_ANG)
    MAX_ANG = df.max()["ANG"]
    
    index = df.query("TRQ == @END_TRQ and ANG == @MAX_ANG").index[0]
    
    df_new = df.drop(df.index[index+1:])
    
    print("==== PLOT ====")
    fig, ax = plt.subplots()
    ax.plot(df_new["ANG"],df_new["TRQ"])
    #ALL file
    axall.plot(df_new["ANG"],df_new["TRQ"])

    ax.set_xlim([-10,30])
    ax.set_ylim([0,80])

    ax.grid()
    ax.set(xlabel = 'Angle(deg)', ylabel = 'Torque(Nm)',
           title = filename)
    fig.savefig(filename+".png")
    plt.close(fig)
# ====== fn_plot ====== 



directory = "data2"

# ====== ALL SETTING ====== 
figall, axall = plt.subplots()
axall.set_xlim([-10,30])
axall.set_ylim([0,80])

axall.grid()
axall.set(xlabel = 'Angle(deg)', ylabel = 'Torque(Nm)',
       title = "ALL")
# ====== ALL SETTING ====== 

for filename in glob.glob(directory + '/*.csv'):
    fn_plot(filename)

figall.savefig(directory + "\\" + "all"+".png")

print("==== END SCRIPT ====")
