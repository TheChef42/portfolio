
from min_heap import MinHeap
from max_heap import MaxHeap

n = input('input number of days: ')
numberOfDays = (float(n))*24
days = []
inputPrice = []
inputUsage = []
array = []
array2 = []
array3 = []
for i in range(int(numberOfDays)):
    inputtedData = tuple(input().split())
    array.append(inputtedData)
    array2.append(inputtedData[:2])
    array3.append(int(inputtedData[1]))
    inputUsage.append(float(inputtedData[2]))
    inputPrice.append(int(inputtedData[1]))

minHeapPrice = MinHeap(inputPrice)
minHeapPrice.build_min_heap()

maxHeapUsage = MaxHeap(inputUsage)
maxHeapUsage.build_max_heap()

optimalcost = 0
for k in range(int(numberOfDays)):
    max = maxHeapUsage.get_array()[0]
    maxHeapUsage.swap(0, maxHeapUsage.get_heap_size()-1)
    maxHeapUsage.set_heap_size(maxHeapUsage.get_heap_size()-1)
    maxHeapUsage.max_heapify(0)
    min = minHeapPrice.get_array()[0]
    minHeapPrice.swap(0, minHeapPrice.get_heap_size() - 1)
    minHeapPrice.set_heap_size(minHeapPrice.get_heap_size() - 1)
    minHeapPrice.min_heapify(0)
    optimalcost += int(min) * float(max)

    i = array3.index(int(min))
    array2[i] = f"{array2[i][0]}  {array2[i][1]}  {max}"



for x in array2:
    print(x)

inputcost = 0

for item in array:
    inputcost += int(item[1]) * float(item[2])

print('Input cost')
print(round(inputcost, 2))
print('Optimal cost:')
print(optimalcost)