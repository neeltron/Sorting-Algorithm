arr = [1, 15, 20, 12, 23, 11]
swap = True

while swap:
  swap = False
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      temp = arr[i]
      arr[i] = arr[i+1]
      arr[i+1] = temp
      swap = True

print("The sorted number are:")
for i in arr:
  print(i)
