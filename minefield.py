from random import shuffle

def generateMinefield(h,w,m):
    #validate number of mines
    if m > (h*w):
        #throw error
        exit("too many mines requested!")
    
    field = [9 for i in range(m)] #mines
    field += [0 for i in range((h*w)-m)] #non-mines
    shuffle(field) #randomize the mine placements
    
    #convert the single list into a lists of lists representing rows and columns
    grid = []
    for row in range(h):
        grid.append([field[x] for x in range(row*h,(row*h)+w)])
    
    #time to set the non-mines mine counts
    for ri, row in enumerate(grid):
        for ci, cell in enumerate(row):
            if cell == 9:
                continue
                
            for roff in [-1,0,1]:
                for coff in [-1,0,1]:
                    if roff == 0 and coff == 0:
                        continue
                    if ri+roff < 0 or ri+roff >= h or ci+coff < 0 or ci+coff >= w:
                        continue
                    if grid[ri+roff][ci+coff] == 9:
                        grid[ri][ci] += 1
                        
    return grid
    
if __name__ == '__main__':
    for r in generateMinefield(10,10,20):
        print r