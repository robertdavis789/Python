print("Input a number")
input1 = input()
print("Input another number")
input2 = input()
print(input1 + "+" + input2 + "=")
userSum = int(input())
sum = int(input1) + int(input2)

if sum == userSum:
    print("Correct")
else :
    print("Wrong Answer")