lst=[165, 149, 81, 76, 76, 75, 65, 65, 59, 45, 34, 32, 18,8654, 881, 816, 635, 543, 384, 345, 182, 181]
for i in range(1,len(lst)-1):
    if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
        lst1 , lst2 = [] , []
        for j in lst[0:i:1]:
            lst1.append(j)
        for k in lst[i+1:len(lst):1]:
            lst2.append(k)
print(lst1)
print(lst2)
print('123')
