# sudoku problem working

import sys

sudoku_size = 9
sorted_line = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def failed_constraints():
    print "Constraints failed"
    sys.exit(1)

def is_valid_sudoku(M):
    is_valid=True
    # check horiz and vert lines
    for i in xrange(0,sudoku_size):
        horz_line = M[i]
        vert_line = [M[x][i] for x in xrange(0,sudoku_size)]
        if sorted_line != sorted(horz_line) or sorted_line != sorted(vert_line):
            is_valid=False
            break

    # check squares
    if is_valid:
        for i in xrange(0,sudoku_size,3):
            for j in xrange(0,sudoku_size,3):
                small_square = []
                for x in xrange(0,3):
                    small_square.append(M[i+x][j])
                    small_square.append(M[i+x][j+1])
                    small_square.append(M[i+x][j+2])
                if sorted_line != sorted(small_square):
                    is_valid=False
                    break
            if not is_valid:
                break

    return is_valid

def fix_sudoku(M):
    for i1 in xrange (0,sudoku_size):
        for j1 in xrange (0,sudoku_size):
            for i2 in xrange (0,sudoku_size):
                for j2 in xrange (0,sudoku_size):
                    if i1<i2 or (i1==i2 and j1<j2):
                        # switch two cells
                        tmp = M[i1][j1]
                        M[i1][j1] = M[i2][j2]
                        M[i2][j2] = tmp
                        # check if valid now?
                        if is_valid_sudoku(M):
                            print "(%d,%d) <-> (%d,%d)" % (i1+1,j1+1,i2+1,j2+1)
                        # swap them back
                        tmp = M[i2][j2]
                        M[i2][j2] = M[i1][j1]
                        M[i1][j1] = tmp

T = int(raw_input())
(T < 1 or T > 1000) and failed_constraints()
M = [[]]*sudoku_size

# populate the sudoku
for i in xrange(T):
    for j in xrange(sudoku_size):
        M [j] = map(int,raw_input().split())
    print "Case #%d:" % (i+1)
    if is_valid_sudoku(M):
        print "Serendipity"
    else:
        fix_sudoku(M)

