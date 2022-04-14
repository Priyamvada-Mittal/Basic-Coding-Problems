number=int(input())
numbers=input()
list_of_numbers=list(map(int, numbers.split()))
sum_palindrome=0
sum_not_palindrome=0
negative_sum=0
for j in list_of_numbers:
    if j>=0:
        if (j == int(str(j)[::-1])):
            sum_palindrome=sum_palindrome+1
        else:
            sum_not_palindrome=sum_not_palindrome+1
    else:
        negative_sum=negative_sum-1
if negative_sum<=-1:
    print("False")
elif sum_palindrome>1:
    print("True")
else:
    print("False")

