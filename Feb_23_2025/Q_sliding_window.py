#given 2 arrays num1 and num2 
#return an array of their intersection 
def intersection(num1,num2):     
    num1.sort()
    num2.sort() 
    ans = []
    pointer1 = 0
    pointer2 = 0

    while (pointer1 < len(num1) and pointer2 < len(num2)): 
        if num1[pointer1] == num2[pointer2]: 
            ans.append(num1[pointer1]) 
            pointer1 += 1
            pointer2 += 1
        if num1[pointer1] < num2[pointer2]: 
            pointer1 += 1
        if num2[pointer2] < num1[pointer1]: 
            pointer2 += 1
  
#4,4,5,9
#4,4,8,9,9
num1 = [4,4,9,5]
num2 = [9,4,9,8,4]
ans = intersection(num1, num2) 
print(ans) 




