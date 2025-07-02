# row = int(input("enter the row no."))
# col = int(input("enter the col no."))

# matrix=[]
# for i in range(row):
#     row=[]
#     for j in range(col):
#         val=int(input(f"enter val {i},{j}: "))
#         row.append(val)
#     matrix.append(row)
# for row in matrix:
#     for element in row:
#         print(element , end=" ")
#     print()



class Math:
    def __init__(self):
        self.matrix=[]

    def block(self,row,col):
        for i in range(row):
            a_row=[]
            for j in range(col):
                val=int(input(f"enter val {i},{j}: "))
                a_row.append(val)
            self.matrix.append(a_row)

    def display_matrix(self):
        for row in self.matrix:
            for element in row:
                print(element,end=" ")
            print()
row = int(input("enter the row no."))
col = int(input("enter the col no."))
m=Math() 
m.block(row, col)
m.display_matrix()

