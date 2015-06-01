import sys

def failed_constraints():
    print "Constraints failed"
    sys.exit(1)

def check_people(prefs,max):
    count = 0
    found = False
    print "checking", max
    for i in xrange(0,N):
        L,H = map(int, prefs[i])
        print L,H
        if (L<=max-1) and (H>=max-1):
            count+=1
            print "OK", count
            if count >= max:
                found = True
                break

    if not found and max>0:
        print "not possible for", max
        max=check_people(prefs,max-1)
    return max

N = int(raw_input())
(N < 1 or N > 300000) and failed_constraints()

prefs = []
for i in xrange(N):
    L,H = map(int,raw_input().split())
    ((0 <= L) and (L <= H) and (H < 300000)) or failed_constraints()
    prefs.append([L,H])

# check if max people would be OK
max = N # we start checking N people and keep going down
print check_people(prefs,max)