import numpy as np
#contineous memory
#no type checking

class NumPyTest:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def FirstTest(self):
        a = np.array([1,2,3])
        print(a)
        twod = np.array(
            [
                [1,2,3,4,5,6,7,8,9,10],
                [11,12,13,14,15,16,17,18,19,20]

            ]
        )
        print(twod[0][0])
        print(twod.ndim)
        print(twod.dtype)
        #Shapre
        print("Shape is %s" % ( twod.shape, ))
        print(f"Shape is {twod.shape}")
        #Get Type
        print(f"Datatype is {twod.dtype}")
        #Get Size
        print(f"itemsize is {twod.itemsize}")
        #Total size
        print(f"size is {twod.size}")
        #nbytes
        print(f"nbytes are {twod.nbytes}")
        #get a specific row
        print(f"{twod[0,0:2]}")
        #Get a specific coloun
        print(f"{twod[:,0]}")

        #init array
        a = np.zeros((2,2),dtype='int32')
        print(f"{a}")
        print('-------------------')

        a = np.full((3,2,2),99)
        print(a)
        a[1,0,1] = 10
        print(f'{a}')

if __name__ == "__main__":
    print("Executing main")
    n = NumPyTest()
    n.FirstTest()
