a = int(input('Ведите продолжительность в секундах: '))
d = a//86400
h = (a//3600)%24
m = (a//60)%60
s = a%60
if h<10:
    h = str('0' + str(h))
else:
    h = str(h)
if m<10:
    m = str('0' + str(m))
else:
    m = str(m)
if s<10:
    s = str('0' + str(s))
else:
    s = str(s)
print(str(d) + ':' + str(h) + ':' + str(m) + ':' + str(s) + ':')
