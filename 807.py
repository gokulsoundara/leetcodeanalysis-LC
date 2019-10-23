class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        table = {}
        for idy,row in enumerate(grid):
            table["row"+str(idy)] = row[0]
            for idx,col in enumerate(row):
                table["row"+str(idy)] = max(table["row"+str(idy)], row[idx])
                table["col"+str(idx)] = max(table.get("col"+str(idx),0),col)

        tot = 0
        for i,j in enumerate(grid):
            for k,l in enumerate(j):
                val = min(table["row"+str(i)],table["col"+str(k)])
                tot += abs(l - val)

        return (tot)
