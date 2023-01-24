#归并排序(lst1，lst2，大到小有序)
def gui_bing(lst):
    for i in range(1,len(lst)-1):
        if lst[i]<lst[i-1] and lst[i]<lst[i+1]:
            lst1,lst2=[],[]
            for j in lst[0:i:1]:
                lst1.append(j)
            for k in lst[i+1:len(lst):1]:
                lst2.append(k)#将lst拆分为lst1,lst2
    lst10=[]
    i,j=0,0
    while i<=len(lst1)-1 and j<=len(lst2)-1:
        if lst1[i]>lst2[j]:
            lst10.append(lst1[i])
            i+=1
        else:
            lst10.append(lst2[j])
            j+=1
    if i!=len(lst1):
        for k in lst1[i+1:len(lst1):1]:
            lst10.append(k)
    if j!=len(lst2):
        for k in lst2[j+1:len(lst2):1]:
            lst10.append(k)
    return lst10

if __name__=="__main__":
    lst=[165, 149, 81, 76, 76, 75, 65, 65, 59, 45, 34, 32, 18,8654, 881, 816, 635, 543, 384, 345, 182, 181]
    print(gui_bing(lst))

print('123')
# 测试分支 归并
