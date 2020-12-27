user_input = input('insert Yr code! (must be a single word) >>>')


first = "abcdefghijklmABCDEFGHIJKLM"
second = "nopqrstuvwxyzNOPQRSTUVWXYZ"

a = list(first)
b = list(second)

def tostr(result):  
    str1 = ""  
     
    for i in result:  
        str1 += i 
      
    return str1

char = list(user_input)
result = []
str1 = ""
for i in char:
    if i in a:
        d = a.index(i)
        result.append(b[d])
    elif i in b:
        s = b.index(i)
        result.append(a[s])
    else:
        result.append(i)


print(tostr(result))