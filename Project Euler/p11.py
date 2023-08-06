GRID = []

with open ('p11_grid.txt') as textFile:
    for line in textFile:
        num_line = [int(item.strip()) for item in line.split(' ')]
        GRID.append(num_line)

height = len(GRID)
width = len(num_line)
ADJACENT = 4

# vertical product
def vertical(r, c):
    v = GRID[r][c]
    for i in range(1, ADJACENT):
        v *= GRID[r + i][c]
    return v

# Horizontal product
def across(r, c):
    h = GRID[r][c]
    for i in range(1, ADJACENT):
        h *= GRID[r][c + i]
    return h

# Diagonal right product
def d_right(r, c):
    dr = GRID[r][c]
    for i in range(1, ADJACENT):
        dr *= GRID[r + i][c + i]
    return dr

# Diagonal left product
def d_left(r, c):
    dl = GRID[r][c]
    for i in range(1, ADJACENT):
        dl *= GRID[r + i][c - i]
    return dl

def compute():
    prod_h  = 1
    prod_v  = 1
    prod_dr = 1
    largest = 1

    for r in range(0, height):
        for c in range(0, width):
            if c + ADJACENT <= width:
                prod_h  = across(r, c)
            if r + ADJACENT <= height:
                prod_v  = vertical(r, c)
            if c + ADJACENT <= width and r + ADJACENT <= height:
                prod_dr = d_right(r, c)
                prod_dl = d_left(r, width - c - 1)
            moving_largest = max(prod_h, prod_v, prod_dr, prod_dl)
            if moving_largest > largest:
                largest = moving_largest
    return largest

max_p = compute()
print(max_p)