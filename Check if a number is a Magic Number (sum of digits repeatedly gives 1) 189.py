num = int(input("Enter the number: "))
while num > 9:
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit 
        num = num  // 10
    num = total 
if num == 1:
      print("Magic number: ")
else:
      print("Non Magic number: ")