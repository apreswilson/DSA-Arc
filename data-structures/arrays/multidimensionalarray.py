def search(matrix):
   for x in range(3):
      for y in range(3):
         if matrix[x][y] == 4:
            print("Found 4")

def traverse(matrix):
   for x in range(3):
      for y in range(3):
         print(matrix[x][y])

def sortRowWise(matrix):
   for x in range (len(matrix)):
      matrix[x] = sorted(matrix[x])
   return matrix

#Transpose just means all columns become the rows and vice versa
def transpose(mat, row, column):
   transposeMatrix = [[0 for i in range(row)] for i in range(column)]
   for x in range(row):
      for y in range(column):
         transposeMatrix[y][x] = mat[x][y]
   return transposeMatrix

def sortCol(mat, row, column):
   B = transpose(mat, row, column)
   B = sortRowWise(B)
   mat = transpose(B, column, row)
   return mat



def main():
   cols = 3
   rows = 3
   array = [[0] * cols] * rows
   print(f"Hollow Matrix: {array}")   

   normalMatrix = [[1,2,3],[4,5,6],[7,8,9]]
   print(f"Normal Matrix: {normalMatrix}")

   print("One element at a time:")
   traverse(normalMatrix)

   print("Search for element");
   search(normalMatrix)

   unsortedMatrix = [[3, 1, 4],[2, 10, 6],[5, 8, 4], [12, 1, 13]]
   rowSorted = sortRowWise(unsortedMatrix)
   print(f"Row Sorted: ")
   for x in rowSorted:
      print(x)
   
   N = len(unsortedMatrix)
   M = len(unsortedMatrix[0])
   colsort = sortCol(unsortedMatrix, N, M)
   print("Column Sorted:")
   for x in colsort:
      print(x)

if __name__ == "__main__":
   main()