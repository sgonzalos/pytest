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
    
    df = pd.read_csv(filename,skiprows=8)
    df = df[df.LoadcellData !=0 ]
    df.No = df.No / 100
    df.LoadcellData = df.LoadcellData / 100

    print("==== PLOT ====")
    fig, ax = plt.subplots()
    ax.plot(df.No, df.LoadcellData)
    #ALL file
    axall.plot(df.No, df.LoadcellData)

    ax.set_xlim([0,3])
    ax.set_ylim([0,4.5])

    ax.grid()
    ax.set(xlabel = 'length(mm)', ylabel = 'Loadcel(kN)',
           title = os.path.basename(filename))
    fig.savefig(filename+".png")
    plt.close(fig)
# ====== fn_plot ====== 



directory = "data"

# ====== ALL SETTING ====== 
figall, axall = plt.subplots()
axall.set_xlim([0,3])
axall.set_ylim([0,4.5])

axall.grid()
axall.set(xlabel = 'length(mm)', ylabel = 'Loadcel(kN)',
       title = "ALL")
# ====== ALL SETTING ====== 

for filename in glob.glob(directory + '/*.csv'):
    fn_plot(filename)

figall.savefig(directory + "\\" + "all"+".png")

print("==== END SCRIPT ====")
