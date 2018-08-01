def nwscore(seq1, seq2):
    
    def prnt(grid):
        for x in grid:
            print (x)
    def backtrack(grid, lseq1, lseq2):
        tempa = ''
        tempb = ''
        aligna = []
        alignb = []
        i, j = len(lseq1), len(lseq2)
        astring = ''
        bstring = ''
        strings = [('', '')]
        branches = [(i, j)]
        def initcheckarr(i, j):
            checkarr = []
            if (grid[i-1][j-1] + match == grid[i][j] and lseq1[i-1] == lseq2[j-1]) or grid[i-1][j-1] + mismatch == grid[i][j]:
                checkarr.append(1)
            if grid[i][j-1] + indel == grid[i][j]: 
                checkarr.append(3)
            if grid[i-1][j] + indel == grid[i][j]: 
                checkarr.append(2)
            return checkarr
        checkarrs = [initcheckarr(i, j)]
        def score(i, j, checkarr, stringa, stringb):
            m, n = i, j
            print ('GP:', '[%s, %s]' % (m, n))
            while len(strings) != 0:
                if len(checkarr) > 1: #diag
                    print ('BRANCH') #diag
                if len(checkarr) > 0:
                    print ('Current String: %s, %s' % (stringa, stringb)) #diag
                    branches.insert(0, (i, j))
                    for x in checkarr:
                        print (x)
                    if checkarr[0] == 1:
                        print ('Diagonal') #diag
                        stringa = lseq1[m-1] + stringa
                        stringb = lseq2[n-1] + stringb
                        m = branches[0][0] - 1
                        n = branches[0][1] - 1
                        checkarr.remove(1)
                    elif checkarr[0] == 2:
                        print ('Vertical') #diag
                        stringa = lseq1[m-1] + stringa
                        stringb = "-" + stringb
                        print (branches[0][0])
                        m = branches[0][0] - 1
                        checkarr.remove(2)
                    elif checkarr[0] == 3:
                        print ('Horizontal') #diag
                        stringa = "-" + stringa
                        stringb = lseq2[n-1] + stringb
                        n = branches[0][1] - 1
                        checkarr.remove(3)
                    checkarrs.insert(0, checkarr)
                    strings.insert(0, (stringa, stringb))
                    score(m, n, initcheckarr(m,n), strings[0][0], strings[0][1])
                else:
                    #if len(strings[0][0]) == max(len(grid), len(grid[0])):
                    if m==0 and n==0:
                        aligna.append(strings[0][0])
                        alignb.append(strings[0][1])
                        nonlocal tempa
                        nonlocal tempb
                        #tempa = strings[0][0]
                        #tempb = strings[0][1]
                        #print ('TEMPS', tempa, tempb)
                    del(strings[0])
                    del(branches[0])
                    del(checkarrs[0])
                    print (branches)
                    print (checkarrs)
                    print (strings)
                    if len(strings) != 0:
                        if 1 in checkarrs[0] or 2 in checkarrs[0] or 3 in checkarrs[0]:
                            print ('halp', max(branches[0][0], branches[0][1]) + 1)
                            #tempa = tempa[max(branches[0][0], branches[0][1]) + 1:]
                            #tempb = tempb[max(branches[0][1], branches[0][0]) + 1:]
                            print('flG', branches[0][0], branches[0][1])
                            #print ('TEMPS2', tempa, tempb)
                            score(branches[0][0], branches[0][1], checkarrs[0], strings[1][0], strings[1][1])
                        else:
                            score(branches[0][0], branches[0][1], checkarrs[0], strings[0][0], strings[0][1])
                        
        score(i, j, checkarrs[0], astring, bstring)
        for x in range(len(aligna)):
            print ('a', aligna[x],'b', alignb[x])
                    
    lseq1, lseq2 = list(seq1), list(seq2)
    rows, cols = lseq1[:], lseq2[:]
    rows.insert(0, 0)
    cols.insert(0,0)
    grid = []
    ####INITIALIZE####
    grid = [[0 for j in range(len(cols))] for i in range(len(rows))]
    count = 0
    for x in range(len(cols)):
        grid[0][x] = count 
        count -= 1
    count = 0
    for x in range(len(rows)):
        grid[x][0] = count
        count -= 1
    prnt(grid)

    ####SCORE####
    match = 1
    mismatch = -1
    indel = -1
    for row in range(1, len(rows)):
        for col in range(1, len(cols)):
            opts = []
            if lseq1[row-1] == lseq2[col-1]:
                opts.append(grid[row-1][col-1] + match)
            else:
                opts.append(grid[row-1][col-1] + mismatch)
            opts.append(grid[row-1][col] + indel)
            opts.append(grid[row][col-1] + indel)
            grid[row][col] = max(opts)
    prnt(grid)
    backtrack(grid, lseq1, lseq2)
    
    #example
    nwscore('COELACANTH', 'PELICAN')
