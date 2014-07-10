A = []
l = open('text19.txt').readlines()
for w in l:
    ll = w.split()
    ll[1] = int(ll[1])
    A.append(ll)
print A