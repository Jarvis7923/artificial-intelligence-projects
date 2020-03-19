def iter(l, n ):
    if n == 0 : 
        # print(data)
        return
    data = []
    for item in l:
        d = data + [item]
        iter(l, n-1, d) 


def iter(l, n, data):
    if n == 0 : 
        print(data)
        return

    for item in l:
        d = data + [item]
        iter(l, n-1, d) 



a = list(range(4))
print(a)
iter(a,3)

# prefix = []
# for i in a:
#     for j in a:
#         for k in a:
#             prefix = prefix + [j]
#             data = prefix + [j]
#             print(data)
