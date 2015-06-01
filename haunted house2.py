import sys
import time

def failed_constraints():
    print "Constraints failed"
    sys.exit(1)

def get_max(ar):
    m=0
    for i in sorted(ar.keys(),reverse=True):
        if ar[i]>=i:
            m=i
            break
    return m

def purge_dict(ar, max, ppl):
    for k in ar.keys():
        if k < max:
            del ar[k]
        elif k > max and k > ar[k] + ppl:
            del ar[k]

# Vars
ar = {}  # information about people preferences
max = 0  # max number or people allowed

# Get number of people
N = int(raw_input())
(N < 1 or N > 300000) and failed_constraints()

start = time.time()
# populate array
for i in xrange(0,N):
    if i%5000==0:
        print i
        end = time.time()
        print end - start
        start = time.time()

    L,H = map(int,raw_input().split())
    ((0 <= L) and (L <= H) and (H < 300000)) or failed_constraints()
    if L>N or H>=max:
        for j in xrange(L,H+1):
            if (j+1) in ar:
                ar[j+1]+=1
            else:
                ar[j+1]=1

    max = get_max(ar)
    people_left=N-i
    purge_dict(ar, max, people_left)

max = get_max(ar)
print max

