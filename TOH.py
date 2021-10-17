li=[]
def toh(n, fromm, to, aux):
    if n == 1:
        li.append('move disk '+str(n)+' from rod '+fromm+' to rod '+to)
        return 1
    ans = 1
    ans += toh(n - 1, fromm, aux, to)
    li.append('move disk '+str(n)+' from rod '+fromm+' to rod '+to)
    ans += toh(n - 1, aux, to, fromm)
    return ans
n=int(input('Enter No Of Disks: '))
res=toh(n, 'A', 'B', 'C')
print('******* Lets Start Game *******')
print('-> '+li[len(li)-res])
res-=1
while(res>0):
    print('1.Next Move')
    print('0.Exit')
    choice=int(input())
    if(choice):
        print('-> '+li[len(li)-res])
        res-=1
    else:
        break
print()
print('******* You Winner Game Over *******')