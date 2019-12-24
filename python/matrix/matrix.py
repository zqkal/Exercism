class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split('\n')
        self.row_item = []
        for row in self.matrix_string:
            self.row_item.append(row.split(' '))

    def row(self, index):
        return [int(i) for i in self.row_item[index - 1]]

    def column(self, index):
        return [int(self.row_item[i][index - 1]) for i in range(len(self.row_item))]
    

# c = Matrix("89 1903 3\n18 3 1\n9 4 800")
# # c = Matrix("1 2")
# # c = Matrix("1 2 3\n4 5 6\n7 8 9")
# c = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
# print('row: ', c.row(3))
# print('column: ', c.column(4))