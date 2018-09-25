import matplotlib.pyplot as plt 

# x=[1,2,3,4]
# y=[1,4,9,16]

# plt.plot(x,y)
# plt.show()

th=[12.506,12.253,12.193,16.921,16.995,17.035,21.703,21.568,21.015]

delays=[0,3,5]
plt.ylim(0,25)

plt.plot(delays, th[0:3], label="window size = 5", color="red")
plt.plot(delays, th[3:6], label="window size = 7", color="green")
plt.plot(delays, th[6:9], label="window size = 9", color="blue")


# plt.scatter(delays, th[0:3], label="window size = 5", color="red")
# plt.scatter(delays, th[3:6], label="window size = 7", color="green")
# plt.scatter(delays, th[6:9], label="window size = 9", color="blue")

# x-axis label 
plt.xlabel('Delay (in ms)') 
# frequency label 
plt.ylabel('Throughput (in KBps)')
# plot title 
plt.title('Drop Rate = 1%')
# showing legend 
plt.legend()
  
# function to show the plot 
plt.show()