class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False

        def rcbFinder(cell):
            d = {(0,0):0,(0,1):1,(0,2):2,(1,0):3,(1,1):4,(1,2):5,(2,0):6,(2,1):7,(2,2):8,}
            row = cell[0]
            col = cell[1]
            box = d.get((row//3,col//3))
            return (row,col,box)

        nums = ('1','2','3','4','5','6','7','8','9')
        drow,dcol,dbox = {},{},{}

        for i,r in enumerate(board):
            for j,c in enumerate(r):
                row,col,box = rcbFinder((i,j))
                val = c
                if val in nums:
                    if row not in drow:
                        drow[row] = set()
                    if col not in dcol:
                        dcol[col] = set()
                    if box not in dbox:
                        dbox[box] = set()
                    if val in drow[row] or val in dcol[col] or val in dbox[box]:
                        return False
                    else:
                        drow[row].add(val)
                        dcol[col].add(val)
                        dbox[box].add(val)

        return True

                
