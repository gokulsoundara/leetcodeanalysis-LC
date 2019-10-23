class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        r=len(board)-1
        c=len(board[0])-1
        def neighbours(cell):
            row = cell[0]
            col = cell[1]
            res = [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),
                  (row+1,col-1),(row+1,col),(row+1,col+1)]
            return [v for v in res if v[0]>=0 and v[0]<=r and v[1]>=0 and v[1]<=c]


        d = {}
        for i,row in enumerate(board):
            for j,col in enumerate(row):
                n = neighbours((i,j))
                liv = col
                tot = 0
                for val in n:
                    if val not in d:
                        tot += board[val[0]][val[1]]
                    else:
                        tot += d.get(val)
                if liv:
                    if tot<2 or tot>3:
                        board[i][j]=0
                        d[(i,j)] = 1
                else:
                    if tot==3:
                        board[i][j]=1
                        d[(i,j)]=0

                        
