mass=[]
def is_palindrome(n):
    str_n = str(n)
    left = 0
    right = len(str_n) - 1
    cnt = 0
    while left < right:
        if str_n[left] != str_n[right]:
            cnt += 1
            if cnt > 1:
                return False
        left += 1
        right -= 1
    return True
for n in range(1, 1000):
    n2=str(bin(n)[2:])
    if is_palindrome(int(n2, 2)) == True:
        n2 =  '10' + n2 + '1'
    if is_palindrome(int(n2, 2))==False:
        n2+=n2[::-1]
        n2='10' + n2 + '1'
    r=int(n2, 2)
    print(r)
    if (is_palindrome(r)==True):
        mass.append(r)
mass.sort(reverse=True)
for i in range(len(mass)):
    if mass[i]<1000 and str(mass[i])==str(mass[i])[::-1]:
        print(mass[i])
        break
