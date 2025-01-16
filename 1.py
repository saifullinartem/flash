mass = []
def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]
for n in range(1, 1000):
    n2 = str(bin(n)[2:])
    if is_palindrome(int(n2, 2)):
        n2 = '1' + n2 + '1'
    else:
        n2 += n2[::-1]
        n2 = '1' + n2 + '1'
    r = int(n2, 2)
    if is_palindrome(r):
        mass.append(r)
mass.sort()
for i in range(len(mass)):
    if mass[i] > 1000:
        print(mass[i])
        break
