class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = []  
        for row in self.matrix_string.split('\n'):
            item = row.split(' ')
            item = [int(i) for i in item]
            rows.append(item)
        return rows[index -1]

    def column(self, index):
        columns = []
        for row in self.matrix_string.split('\n'):
            item = row.split(' ')[index - 1]
            columns.append(int(item))
        return columns
