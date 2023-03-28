num=int(input("Enter the Number: "))
min_range=int(input("Enter the Minimum Range: "))
max_range=int(input("Enter the Maximum Range: "))
result_start = int(input("Enter the starting range for the result: "))
result_end = int(input("Enter the ending range for the result: "))
for i in range(min_range,max_range+1):
    num,"*",i,"=",num*i
    if result_start<=num*i<=result_end:
        print(num,"*",i,"=",num*i)