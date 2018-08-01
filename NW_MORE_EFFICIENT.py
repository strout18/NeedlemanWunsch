def nwscore(seq1, seq2): #see https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm for algorithm explanation
    
    def prnt(grid): #prints the N-W grid of scores 
        for x in grid:
            print (x)
    def backtrack(grid, lseq1, lseq2): #uses the score grid to find and create best alignments
        aligna = [] #list of possible final aligned forms of sequence 1
        alignb = [] #list of possible final aligned forms of sequence 2
        i, j = len(lseq1), len(lseq2)
        astring = '' #string containing current part of aligned form of seq 1
        bstring = '' #string containing current part of aligned form of seq 2
        strings = [('', '')] #used for cases where > 1 direction is possible
        branches = [(i, j)] #used for cases where > 1 direction is possible
        def initcheckarr(i, j): #creates list of possible directions for backtracking (see wiki page)
            #each number corresponds to a direction
            #'1' in checkarr = diagonal arrow = match/mismatch 
            #'2' in checkarr  = vertical arrow =  indel
            #'3' in checkarr = horizontal arrow = indel
            checkarr = []
            if (grid[i-1][j-1] + match == grid[i][j] and lseq1[i-1] == lseq2[j-1]) or grid[i-1][j-1] + mismatch == grid[i][j]:
                checkarr.append(1)
            if grid[i-1][j] + indel == grid[i][j]: 
                checkarr.append(2)
            if grid[i][j-1] + indel == grid[i][j]: 
                checkarr.append(3)
            return checkarr
        checkarrs = [initcheckarr(i, j)] #list of list of possibilities for positions in grid 
        def score(i, j, checkarr, stringa, stringb): #does most of the actual work 
            #i, j = coords        stringa, stringb = the current parts of the seqs that have been aligned
            m, n = i, j
            while len(strings) != 0: #strings = 0 is equiv to having reached top left corner of grid and finishing
                if len(checkarr) > 1: #if more than one possible direction, make note of this for revisiting later
                    branches.insert(0, (i, j)) #record position
                    checkarrs.insert(0, checkarr[1:]) #record directions
                    strings.insert(0, (stringa, stringb)) #record current progress in alignments
                if len(checkarr) > 0: #finds the correct direction (or the first if multiple) stored in checkarr
                    if checkarr[0] == 1:
                        stringa = lseq1[m-1] + stringa
                        stringb = lseq2[n-1] + stringb
                        m -= 1
                        n -= 1
                        checkarr.remove(1) #removes entry from directions
                    elif checkarr[0] == 2:
                        stringa = lseq1[m-1] + stringa
                        stringb = "-" + stringb #inserts gap
                        m -= 1
                        checkarr.remove(2)
                    elif checkarr[0] == 3:
                        stringa = "-" + stringa #gap
                        stringb = lseq2[n-1] + stringb
                        n -= 1
                        checkarr.remove(3)
                    score(m, n, initcheckarr(m,n), stringa, stringb) #recursively makes note of > 1 directions 
                else: #if all possibilities have been recorded or followed up on
                    if m==0 and n==0: #if full alignment has been reached (reached top left corner of grid)
                        aligna.append(stringa) #add to list of final alignments
                        alignb.append(stringb)
                    if len(strings) != 0: #if branches need to be followed up on
                        tempstringa, tempstringb = strings[0][0], strings[0][1]
                        tempi, tempj = branches[0][0], branches[0][1]
                        tempcheckarr = checkarrs[0]
                        del (strings[0]) #delete the branch that's about to be followed up on
                        del (branches[0])
                        del (checkarrs[0])
                        score (tempi, tempj, tempcheckarr, tempstringa, tempstringb) #follow up on stored branch
                        
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
    
