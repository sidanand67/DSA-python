# Linear Search 
def linear_search(arr, target): 
  for i in range(len(arr)): 
    if arr[i] == target: 
      return i 
  return -1 

if __name__ == "__main__": 
  arr = [5,7,7,8,8,10] 
  target = 8
  result = linear_search(arr, target) 
  print(result)