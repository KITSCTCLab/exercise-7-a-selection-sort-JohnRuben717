from typing import List

def selectionSort(array, size) -> List[int]:
     size = len(data)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, size):  
            if data[j]<data[minIndex]:  
                minIndex = j  
                  
        data[i], data[minIndex] = data[minIndex], data[i]  
          
          
    return data
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
