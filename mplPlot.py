import numpy as np
import matplotlib.pyplot as plt


###########################################################################
# rcParams setting
###########################################################################

# layout
plt.rcParams["figure.figsize"] = [16.0, 12.0]  # [width(inch):height(inch)]
# plt.rcParams["figure.dpi"] = 300
plt.rcParams["figure.subplot.left"] = 0.14     # padding-left
plt.rcParams["figure.subplot.bottom"] = 0.14   # padding-bottom
plt.rcParams["figure.subplot.right"] = 0.90    # padding-right
plt.rcParams["figure.subplot.top"] = 0.91      # padding-top
plt.rcParams["figure.subplot.wspace"] = 0.30   # padding-width-space
plt.rcParams["figure.subplot.hspace"] = 0.30   # padding-height-space

# font
# plt.rcParams["font.family"] = "serif"
# plt.rcParams["font.serif"] = "Times New Roman"
plt.rcParams["font.size"] = 18

# ticks
plt.rcParams["xtick.top"] = True
plt.rcParams["xtick.bottom"] = True
plt.rcParams["ytick.left"] = True
plt.rcParams["ytick.right"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.major.width"] = 1.5
plt.rcParams["ytick.major.width"] = 1.5
plt.rcParams["xtick.minor.width"] = 1.0
plt.rcParams["ytick.minor.width"] = 1.0
plt.rcParams["xtick.major.size"] = 10
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["xtick.minor.size"] = 5
plt.rcParams["ytick.minor.size"] = 5

# axes
plt.rcParams["axes.labelsize"] = 24
plt.rcParams["axes.labelpad"] = 20
plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams["axes.grid"] = False
# grid setting
# plt.rcParams["grid.color"] = "black"
# plt.rcParams["grid.linestyle"] = "--"
# plt.rcParams["grid.linewidth"] = 1.0

# legend
plt.rcParams["legend.loc"] = "best"
plt.rcParams["legend.frameon"] = False
# plt.rcParams["legend.framealpha"] = 1.0
plt.rcParams["legend.fontsize"] = 20
plt.rcParams["legend.borderaxespad"] = 1.0
plt.rcParams["legend.facecolor"] = "white"
plt.rcParams["legend.edgecolor"] = "black"
plt.rcParams["legend.fancybox"] = False
# plt.rcParams["legend.markerscale"] = 2


###########################################################################
# Load data functions
###########################################################################

def loadDataFile(filename, skip):
    data = np.loadtxt(filename, skiprows=skip)
    return data


###########################################################################
# Plot
###########################################################################

# data arrangement
x, y = np.loadtxt("data.dat", unpack=True, skiprows=1)

# example for sorting by x value
# dataList = loadDataFile("data.dat", 1)
# data = dataList[dataList[:, 0].argsort(), :]
# x = []
# y = []
# for i in range(len(data)):
#     x.append(data[i][0])
#     y.append(data[i][1])

# layout
fig = plt.figure()
ax = fig.add_subplot(111)

# plot
ax.plot(x, y, linewidth=3, color="blue", label="Data")

# other settings
ax.set_xlabel("X-label")
ax.set_ylabel('Y-label')
# ax.set_xlim(0, 5)
# ax.set_ylim(0, 25)

# legend
ax.legend()

# save
plt.savefig("plot.png", dpi=300)
