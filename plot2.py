import matplotlib.pyplot as plt 

# th=[12.506,12.253,12.193,16.921,16.995,17.035,21.703,21.568,21.015]
# latency=[10.156,10.397,10.551,7.4269,7.4728,7.4891,5.7986,5.8795,6.0491]

# th=[8.573,8.329,8.270,9.980,10.074,10.075,12.030,11.776,11.446]
# latency=[15.207,15.141,16.072,12.592,12.895,13.268,10.362,10.713,11.034]

th=[5.710,5.624,5.568,6.365,6.288,6.224,7.241,7.237,7.127]
latency=[22.867,23.070,23.408,19.986,20.352,20.797,17.155,17.471,18.276]

winsize=[5,7,9]
# plt.ylim(0,25)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(winsize, [th[0],th[3],th[6]], 'r-', alpha=0.3, label="delay=0ms", marker='o', markersize=8)
# plt.legend()
ax1.plot(winsize, [th[1],th[4],th[7]], 'r-', alpha=0.7, label="delay=3ms", marker='o', markersize=8)
# plt.legend()
ax1.plot(winsize, [th[2],th[5],th[8]], 'r-', alpha=1, label="delay=5ms", marker='o', markersize=8)
# ax1.legend()
ax2.plot(winsize, [latency[0],latency[3],latency[6]], 'b-', alpha=0.3, label="delay=0ms", marker='o', markersize=8)
# ax2.legend()
ax2.plot(winsize, [latency[1],latency[4],latency[7]], 'b-', alpha=0.7, label="delay=3ms", marker='o', markersize=8)
# ax2.legend()
ax2.plot(winsize, [latency[2],latency[5],latency[8]], 'b-', alpha=1, label="delay=5ms", marker='o', markersize=8)
# ax2.legend()


ax1.set_xlabel('Window Size')
ax1.set_ylabel('Throughput (in KBps)', color='r')
ax2.set_ylabel('Latency (in ms)', color='b')
ax1.legend(loc='upper right', framealpha=0.8)
ax2.legend(loc='lower right', framealpha=0.8)
plt.title('Drop Rate = 10%')

# line plots
# plt.plot(winsize, th[0:3], label="window size = 5", color="red")
# plt.plot(winsize, th[3:6], label="window size = 7", color="green")
# plt.plot(winsize, th[6:9], label="window size = 9", color="blue")

# scatter plots
# plt.scatter(winsize, th[0:3], label="window size = 5", color="red")
# plt.scatter(winsize, th[3:6], label="window size = 7", color="green")
# plt.scatter(winsize, th[6:9], label="window size = 9", color="blue")

# plt.xlabel('Delay (in ms)') 
# plt.ylabel('Throughput (in KBps)')
# plt.title('Drop Rate = 1%')
# showing legend 
# plt.legend()
  
# function to show the plot 
plt.show()