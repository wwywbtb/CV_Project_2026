import numpy as np

arr1 = np.array([1,2,3,4,5])
print("arr1:",arr1)

arr2 = np.array([[1,2,3],[4,5,6]])
print("arr2:",arr2)

arr3 = np.array([[[1,2],[3,4],[5,6]]])
print("arr3:",arr3)

arr4 = arr2.reshape(-1)
print("arr4:",arr4)

arr5 = np.ones((3,3))
print("arr5:",arr5)

arr6 = np.zeros((3,3))
print("arr6:",arr6)

arr7 = np.full((3,3),5)
print("arr7:",arr7)

arr8 = np.arange(1,10)
print("arr8:",arr8)

arr9 = np.linspace(1,10,5)
print("arr9:",arr9)

arr10 = np.random.random((2,3))
print("arr10:",arr10)

arr11 = 40 * np.random.random(10) + 60
print("arr11:",arr11)

arr12 = np.random.randint(60,100,(10,))
print("arr12:",arr12)

arr13 = np.random.normal(0,1,(5,))
print("arr13:",arr13)

arr14 = np.arange(1,10).reshape(3,3)
print("arr14:",arr14)
cut1 = arr14[[0,1,2],[2,1,0]]
print("cut1:",cut1)
cut1[0] = 100
print("cut1:",cut1)
print("arr14:",arr14)
cut2 = arr14[1:3,:]
print("cut2:",cut2)

arr15 = np.arange(1,10).reshape(3,3)
print("arr15:",arr15)
cut3 = arr15[1:3,1:3]
print("cut3:",cut3)
cut3[0,0] = 100
print("cut3:",cut3)
print("arr15:",arr15)



