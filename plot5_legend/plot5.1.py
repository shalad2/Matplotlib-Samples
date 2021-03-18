import numpy as np
import matplotlib.pyplot as plt

# layout
plt.rcParams["figure.figsize"] = [16.0, 12.0]  # [width(inch):height(inch)]
# plt.rcParams["figure.dpi"] = 300
plt.rcParams["figure.subplot.left"] = 0.14     # padding-left
plt.rcParams["figure.subplot.bottom"] = 0.14   # padding-bottom
plt.rcParams["figure.subplot.right"] = 0.90    # padding-right
plt.rcParams["figure.subplot.top"] = 0.91      # padding-top
plt.rcParams["figure.subplot.wspace"] = 0.30   # padding-width-space
plt.rcParams["figure.subplot.hspace"] = 0.20   # padding-height-space

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

# data
data = np.loadtxt("../sample.dat", skiprows=1)
data_T = data.T
x = data_T[0]
y1 = data_T[1]
y2 = data_T[2]

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(x, y1, color='green', linewidth=3, label='sin(x)')
ax2.plot(x, y2, color='blue', linewidth=3, label='cos(x)')
# labels
ax1.set_ylabel('Amplitude')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Amplitude')
# xlim, ylim
ax1.set_ylim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
# ticks
ticks=np.linspace(-1.0, 1.0, 3)
ax1.set_yticks(ticks)
ax2.set_yticks(ticks)
# legend
ax1.legend(loc='upper right', frameon=True, borderaxespad=1)
ax2.legend(loc='upper right', frameon=True, borderaxespad=1)

plt.savefig("plot5.1.png", dpi=300)
