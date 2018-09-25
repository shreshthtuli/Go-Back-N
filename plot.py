import matplotlib.pyplot as plt 

# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.show()

th=[12.506,12.253,12.193,16.921,16.995,17.035,21.703,21.568,21.015]
latency=[10.156,10.397,10.551,7.4269,7.4728,7.4891,5.7986,5.8795,6.0491]

delays=[0,3,5]
# plt.ylim(0,25)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(delays, th[0:3], 'g-')
ax2.plot(delays, latency[0:3], 'b-')

ax1.set_xlabel('Delay (in ms)')
ax1.set_ylabel('Throughput (in KBps)', color='g')
ax2.set_ylabel('Latency (in ms)', color='b')
plt.title('Drop Rate = 1%')

# line plots
# plt.plot(delays, th[0:3], label="window size = 5", color="red")
# plt.plot(delays, th[3:6], label="window size = 7", color="green")
# plt.plot(delays, th[6:9], label="window size = 9", color="blue")

# scatter plots
# plt.scatter(delays, th[0:3], label="window size = 5", color="red")
# plt.scatter(delays, th[3:6], label="window size = 7", color="green")
# plt.scatter(delays, th[6:9], label="window size = 9", color="blue")

# plt.xlabel('Delay (in ms)') 
# plt.ylabel('Throughput (in KBps)')
# plt.title('Drop Rate = 1%')
# showing legend 
plt.legend()
  
# function to show the plot 
plt.show()