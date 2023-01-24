#希尔排序
import time 
def f_xier(lst):
    for i in range(4,len(lst),4):
        for j in range(i,0,-4):
            if lst[j]>lst[j-4]:
                lst[j],lst[j-4]=lst[j-4],lst[j]
    for i in range(2,len(lst),2):
        for j in range(i,0,-2):
            if lst[j]>lst[j-2]:
                lst[j],lst[j-2]=lst[j-2],lst[j]
    for i in range(1,len(lst)):
        for j in range(i,0,-1):
            if lst[j]>lst[j-1]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
    return lst

if __name__=="__main__":
    lst=[543,45,32,65,345,75,8654,76,635,76,34,65,881,165,81,18,181,182,816,149,384,59]
    t1=time.time()
    print(f_xier(lst))
    t2=time.time()
    print(t2-t1)