arr = []
nums = int(input("Enter the number of items: "))
for iter in range(nums):
  tmp = int(input("Enter a number: "))
  arr.append(tmp)

swap = True

while swap:
  swap = False
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      temp = arr[i]
      arr[i] = arr[i+1]
      arr[i+1] = temp
      swap = True


print("The sorted numbers are:")
for i in arr:
  print(i)
