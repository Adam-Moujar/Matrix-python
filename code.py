class matrix:

    def __init__(self):
        self.dimensions = 0
        self.grid = []
        
    def setDimension(self):
        nsize = int(input("What is the matrix dimensions?: "))
        self.dimensions = nsize

    def initMatrix(self):
        self.grid = []
        print("Setting up Matrix: ")
        print(" ")
        for i in range(0,self.dimensions * self.dimensions):
            val = int(input("What is the next element in the matrix?: "))
            self.grid.append(val)
        print(" ")

    def printMatrix(self):
        for y in range(0,self.dimensions):
            string = ""
            for x in range(0,self.dimensions):
                string = string + " " + str(self.grid[y*self.dimensions + x])
            print(string)
        print(" ")


def matrixDet(matrix): # this takes a matrix grid (e.g if matrix1 is your object, you will use matrixDet(matrix1.grid) to compute matrix1 determinant) as a parameter

    try: # the reason for this try and except is that there's only 1 possible error this could throw (apart from a syntax error if your elements are nonsense) in which 
         # the program tries to  divide by zero if any of the middle diagonal elements are 0, 
         # in which case the determinant will always be zero so that's why i simply print out det = 0
        
        length = int(len(matrix)**0.5)
        currentPos = 0
        iteration = 0
        scalarList = []
     
        while(True):
            if(currentPos == length**2 -1):
                break
            else:
                for i in range(0,length - (iteration +1)):
                    scalarList.append(matrix[(i+1)*length + currentPos] / matrix[currentPos])
                    

                for y in range(iteration,length -1):
                    for x in range(0,length):
                        matrix[(y+1)*length + x] =  matrix[(y+1)*length + x] - scalarList[0]* matrix[iteration*length + x]
                    scalarList.pop(0)

                iteration = iteration +1
                currentPos = currentPos + length + 1

        val = 1
        
        for i in range(0,length):
            val = val * matrix[i*length + i]

        print("determinant =", val )
        print(" ")

    except:
        print("determinant = 0")
        print(" ")

    

def matrixProduct(matrix1, matrix2): # this takes the matrix object completely and gives the product 
    if(matrix1.dimensions != matrix2.dimensions):
        print("you cant do matrix product of these 2!!")
    else:
        matrixProd = []
        for y in range(0,matrix1.dimensions):
            for x1 in range(0,matrix1.dimensions):
                val = 0
                for x2 in range(0,matrix1.dimensions):
                    val = val + matrix1.grid[y*matrix1.dimensions + x2] * matrix2.grid[x2*matrix1.dimensions + x1]
                        
                matrixProd.append(val)


            
        for y in range(0,matrix1.dimensions):
            string = ""
            for x in range(0,matrix1.dimensions):
                 string = string + " " + str(matrixProd[y*matrix1.dimensions + x])
            print(string)

    print(" ")
            

def main():

    #example of code you might want to run
    
    matrix1 = matrix() #creates first matrix
    matrix1.setDimension() # sets dimensions you want
    matrix1.initMatrix() # initialises it and asks you for inputs
    matrix1.printMatrix() # prints it for you to see

    matrix2 = matrix() # creates a second one using the same process
    matrix2.setDimension()
    matrix2.initMatrix()
    matrix2.printMatrix()

    matrixProduct(matrix1,matrix2) # returns the multiplication of matrix1 x matrix2

    matrixDet(matrix1.grid) # returns det of matrix1

    matrixDet(matrix2.grid) # returns det of matrix2

        
if(__name__ == "__main__"):
    main()
