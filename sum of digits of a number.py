number=int(input("Enter the  digits you want to calculate the sum for"))
sum=0
while (number>0):
    remainder=number%10
    sum=remainder+sum
    number=int(number/10)
print(sum)