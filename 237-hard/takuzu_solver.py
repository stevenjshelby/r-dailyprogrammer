#!/usr/bin/python

#https://www.reddit.com/r/dailyprogrammer/comments/3pwf17/20151023_challenge_237_hard_takuzu_solver/

import sys
import os
from pprint import pprint
from time import sleep

history = []
made_change = False

def solve(grid):
    global made_change

    print 'Solving grid....'
    pprint(grid)

    made_change = False


    #check doubles
    grid = process_doubles(grid)

    #check counts
    grid = process_row_counts(grid)

    #similar line checks
    grid = process_similar_lines(grid)


    if not is_solved(grid):
        if not made_change:
            grid = flip_grid(grid)
        solve(grid)
    else:
        print 'Grid Solved!'
        pprint(grid)


def process_similar_lines(grid):
    global made_change

    for ri in range(len(grid)):
        row = grid[ri]
        for ri2 in range(len(grid)):
            if ri == ri2:
                continue
            compare_row = grid[ri2]

            match = True
            for ci in range(len(row)):
                if row[ci] != '.' and row[ci] != compare_row[ci]:
                    match = False
                    break
            if match:
                pass
                # perms = get_available_perms_for_match(row, compare_row)
                # if len(perms) == 1:
                #     made_change = True
                #     grid[ri] = perms[0]

    return grid


def process_doubles(grid):
    global made_change

    rows = len(grid)
    cols = len(grid[0])
    for ri in range(rows):
        for ci in range(cols):
            val = grid[ri][ci]

            if val != '.':
                continue

            b1 = grid[ri][ci-1] if ci >= 1 else 'x'
            b2 = grid[ri][ci-2] if ci >= 2 else 'x'
            f1 = grid[ri][ci+1] if ci <= cols - 2 else 'x'
            f2 = grid[ri][ci+2] if ci <= cols - 3 else 'x'

            if b1 == b2 and b1 in ['0', '1']:
                grid[ri][ci] = opposite_value(b1)
                made_change = True
            elif f1 == f2 and f1 in ['0', '1']:
                grid[ri][ci] = opposite_value(f1)
                made_change = True
            elif b1 == f1 and b1 in ['0', '1']:
                grid[ri][ci] = opposite_value(b1)
                made_change = True

    return grid


def process_row_counts(grid):
    global made_change

    max_row_0,max_row_1 = get_max_row_count(grid)

    for ri in range(len(grid)):
        row = grid[ri]

        c_0, c_1 = get_row_counts(row)
        total = len(row)

        nval = False
        if max_row_0 - c_0 == total - c_0 - c_1:
            #remaining values should be 0
            nval = '0'
        elif max_row_1 - c_1 == total - c_0 - c_1:
            #remaining values should be 1
            nval = '1'

        if nval:
            for ci in range(len(row)):
                if row[ci] == '.':
                    grid[ri][ci] = nval
                    made_change = True

    return grid


def get_max_row_count(grid):
    max_count_0 = 0
    max_count_1 = 0

    for row in grid:
        c_0, c_1 = get_row_counts(row)

        if c_0 > max_count_0:
            max_count_0 = c_0
        if c_1 > max_count_1:
            max_count_1 = c_1

    return (max_count_0, max_count_1)


def get_row_counts(row):
    c_0 = 0
    c_1 = 0

    for col in row:
        if col == '0':
            c_0 += 1
        elif col == '1':
            c_1 += 1

    return (c_0, c_1)


def opposite_value(val):
    if val == '1':
        return '0'
    elif val == '0':
        return '1'

    return False


def flip_grid(grid):
    new_grid = zip(*grid)
    for i in range(len(new_grid)):
        new_grid[i] = list(new_grid[i])

    return new_grid


def is_solved(grid):
    for row in grid:
        for col in row:
            if col != '0' and col != '1':
                return False
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Please supply an input file.')

    fn = sys.argv[1]

    if not os.path.isfile(fn):
        sys.exit('Invalid file name.')

    with open(fn) as file:
        grid = file.read().splitlines()
        grid = [list(line) for line in grid]

    solve(grid)
