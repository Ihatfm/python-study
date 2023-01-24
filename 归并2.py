#归并和递归
def merge(L,R):
    i,j=0,0
    res=[]
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            res.append(L[i])
            i+=1
        else:
            res.append(R[j])
    res+=R[j:] if i==len(L) else L[i:]
    return res#合并 

def merge_sort(lst):
    length = len(lst)
    if length<=1:
        return lst
    else:
        mid = length//2
        left=merge_sort(lst[:mid])
        right=merge_sort(lst[mid:])#递归
        return merge(left,right)

if __name__=="__main__":
    lst=[165, 149, 81, 76, 76, 75, 65, 65, 59, 45, 34, 32, 18,8654, 881, 816, 635, 543, 384, 345, 182, 181]
    print(merge_sort(lst))