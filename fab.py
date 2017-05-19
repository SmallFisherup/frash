def fab(n):
    n1=1
    n2=1
    n3=1
    if n<1:
        print("输入有误！")
        return -1
    "发现规律，并应用规律"
    "递进的次数"
    "向前递进的过程"
    while (n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3
        n-=1        
    return n3

result=fab(5)
if result!=-1:
    print("通过迭代计算总共有%d对小兔子诞生！"%result)
def fabr(n):
    if n<1:
        print("输入有误！")
        return -1
    if n==1 or n==2:
        return 1
    else:
        return fabr(n-1)+fabr(n-2)
results=fabr(5)
if results!=-1:
    print("通过递归计算总共有%d对小兔子诞生！"%results)
