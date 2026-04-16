class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        colMap = set()
        rowMap = set()
        squareMap = set()

        for row in board: # for every row
            rowMap = set()
            for c in row: # for every char in row
                if c == ".":
                    continue
                if c in rowMap:
                    return False
                else:
                    rowMap.add(c)
        
        for i in range(9):
            colMap = set()
            for x in range(9):
                if board[x][i] == ".":
                    continue
                if board[x][i] in colMap:
                    return False
                else:
                    colMap.add(board[x][i])

        for colOffset in range(0, 9, 3):
            for rowOffset in range(0, 9, 3):
                squareMap = set()
                for row in range(3):
                    for col in range(3):
                        car = board[row + rowOffset][col + colOffset]
                        if car == ".":
                            continue
                        if car in squareMap:
                            return False
                        else:
                            squareMap.add(car)
            
        return True
                
                
                








        