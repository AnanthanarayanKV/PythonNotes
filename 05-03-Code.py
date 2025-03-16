# # # # # # #Exam 3/5/2025
# # # # # # import numpy as np
# # # # # # ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # # # # # print(ar[1:4,1:4])

# # # # # #------------------------------------------------------
# # # # # #nditer()
# # # # # import numpy as np
# # # # # ar = np.array([[[1,2],[3,4],[5,6],[7,8]]])
# # # # # for x in np.nditer(ar):
# # # # #     print(x)
    
# # # # # ------------------------------------------------------
# # # # #appending a array

# # # # import  numpy as np

# # # # ar = np.array([1,2,3,4,5])
# # # # print("Original array:",ar)

# # # # ar = np.append(ar,[10])
# # # # print(ar)

# # # # --------------------------------------------------------
# # # import numpy as np

# # # ar1 = np.array([1,2,3])
# # # ar2 = np.array([4,5,6])

# # # fullar = np.append(ar1,ar2)

# # # print(ar1)
# # # print(ar2)
# # # print(fullar)

# # # ----------------------------------------------------------
# # import numpy as np

# # ar = np.arange(1,19).reshape(3,6)
# # print("Og array\n",ar,'\n')

# # col = np.arange(5,11).reshape(1,6)
# # print(np.append(ar,col,axis=0),'\n')

# # row = np.arange(1,4).reshape(3,1)
# # print(np.append(ar,row,axis=1),'\n')

# # ------------------------------------------------------------
# import numpy as np

# arr = np.arange(7,16).reshape(3,3)
# row = np.arange(16,22).reshape(3,2)
# print(np.append(arr,row,axis=1))

# --------------------------------------------------------------
import numpy as np

x = np.array([[1,2],[4,5]])
y = np.array([[7,8],[9,10]])

print("Sum of elements\n",np.add(x,y))
print("Difference of elements\n",np.subtract(x,y))
print("Division of elements\n",np.divide(x,y))
print("Multiplication of elements\n",np.multiply(x,y))
print("Multiplication of row and column\n",np.dot(x,y))
print("Square root of elements in x\n",np.dot(x,y))
print("Sum of elements in x\n",np.sum(x))
print("Sum of row elements in x\n",np.sum(x,axis=1))
print("Sum of column elements in x\n",np.sum(x,axis=0))
print("Transpose of x\n",x.T)


