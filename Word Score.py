sentence=input()
list_of_words=list(map(str,sentence.split()))
list_of_score=[]
for i in list_of_words:
    temp_sum=0
    for j in range(len(i)):
        if (i[j] == 'a' or i[j] =="e" or i[j] =="o" or i[j]=="u" or i[j]=="y" or i[j] == "i"):
            temp_sum=temp_sum+1
    list_of_score.append(temp_sum)
final_sum=0
for i in list_of_score:
    if(i%2==0):
        final_sum=final_sum+2
    else:
        final_sum=final_sum+1
print(final_sum)
