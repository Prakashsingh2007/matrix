class Math:
    def __init__(self):
        self.matrix = []

    def block(self, row, col):
        print("\nEnter matrix values:")
        self.matrix = []
        for i in range(row):
            row_data = []
            for j in range(col):
                val = int(input(f"Enter value at ({i}, {j}): "))
                row_data.append(val)
            self.matrix.append(row_data)

    def display_matrix(self):
        print()
        for row in self.matrix:
            for val in row:
                print(f"{val:4}", end="")
            print()

    def add_matrix(self, other):
        if not self._same_size(other):
            print("Addition failed: Matrices must have the same size.")
            return None
        result = Math()
        for i in range(len(self.matrix)):
            row = [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            result.matrix.append(row)
        return result

    def subtract_matrix(self, other):
        if not self._same_size(other):
            print("Subtraction failed: Matrices must have the same size.")
            return None
        result = Math()
        for i in range(len(self.matrix)):
            row = [self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))]
            result.matrix.append(row)
        return result

    def multiply_matrix(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            print("Multiplication failed: Columns of A must equal rows of B.")
            return None
        result = Math()
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                val = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(other.matrix)))
                row.append(val)
            result.matrix.append(row)
        return result

    def transpose(self):
        result = Math()
        result.matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return result

    def _same_size(self, other):
        return (len(self.matrix) == len(other.matrix) and
                len(self.matrix[0]) == len(other.matrix[0]))


# Input matrices
print("Matrix A:")
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
A = Math()
A.block(row, col)

print("\nMatrix B:")
B = Math()
B.block(row, col)

# Display
print("\nMatrix A:")
A.display_matrix()
print("\nMatrix B:")
B.display_matrix()

# Addition
print("\nA + B:")
C = A.add_matrix(B)
if C:
    C.display_matrix()

# Subtraction
print("\nA - B:")
D = A.subtract_matrix(B)
if D:
    D.display_matrix()

# Multiplication (only if dimensions allow)
print("\nA x B:")
E = A.multiply_matrix(B)
if E:
    E.display_matrix()

# Transpose
print("\nTranspose of A:")
TA = A.transpose()
TA.display_matrix()

print("\nTranspose of B:")
TB = B.transpose()
TB.display_matrix()

