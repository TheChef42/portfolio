import matplotlib.pyplot as plt



x = [0, 1]
y1 = [2, 3]
y2 = [5, 8]
y3 = [3, 7]
z1 = [1, 2]

plt.xlabel("Time")
plt.ylabel("Data")

#remove the x ticks
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

plt.plot(x, y1, marker='.', color='r', label='line 1')
plt.plot(x, y2, marker='+', color='g', label='line 2')
plt.plot(x, y3, marker='*', color='b', label='line 3')
plt.legend()
plt.show()
plt.savefig('fig.png')