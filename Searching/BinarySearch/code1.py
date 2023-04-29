# Binary Search (Iterative)
# Time Complexity: O(logn) 

def binary_search(arr, target):
  low = 0 
  high = len(arr)-1 
  while low <= high: 
    mid = (low+high)//2 
    if arr[mid] == target: 
      return mid 
    elif arr[mid] > target: 
      high = low-1 
    else: 
      low = mid+1 
  return -1 


if __name__ == "__main__": 
  arr = [5,7,7,8,8,10]
  target = 10
  result = binary_search(arr, target) 
  print(result) 