#program to print largest number

def largest_number(fn,sn,tn):
    if fn>sn and fn > tn :
        print(fn)
    if sn> fn and sn > tn:
        print(sn)
    if tn > fn and tn > sn:
        print(tn)

fn = 28
sn = 21
tn = 20
largest_number(fn,sn,tn)