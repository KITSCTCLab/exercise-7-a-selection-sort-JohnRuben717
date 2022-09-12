from typing import List

def selectionSort(array, size) -> List[int]:
for i in range(len(data)):
     
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
             
    # Swap the found minimum element with
    # the first element       
    data[i], data[min_idx] = data[min_idx], data[i]
  # Write your code here

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
