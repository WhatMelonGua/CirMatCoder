from CirMatCoder import *


#I give a Func like Mask in PhotoShop-'FilterIO'

Mask = CirMapping(list(range(1,15)),10,1,[5,5],[0])
Mask.ShowCir()
#Firstly,we need have a Mask

Cir = CirMapping(list(range(1,100)),10,1,[1,1])
Cir.ShowCir()
#Then,give a CirMap with data,Now we can use FilterIO

Result = FilterIO(Cir,Mask,'Mask')
#Please place data CirMap in front of Mask CirMap,and the'Mask' means element filled in Blank<0'position in Mask>
#And In Mask,if the elements is not 0, then it represent the data in this position can be showed after.

Result.ShowCir()
#FilterIO return a CirMap,Let's have a look


A=CirMapping([],10)
B=CirMapping([],6)
Maskand = Cirand(A,B,3,'D')
#Func Maskand return a Mask CirMap with 1 & 0,element in intersection will be 1 and other 0
#emmm... But look like the result can be a little not good
print('Intersection Mask CirMap')
Maskand.ShowCir()
#Then you can use the Mask to other CirMap,or look below,use it to creat a Matrix,As Mask Matrix

#Use Func Mat(CirMap,x) to turn CirMap to MatMap,Also Cir(MatMap,D,d,x) to turn MatMap to CirMap,you should give diameter and d<2 characters distance>
#x always means the list to fill the Blank character/element

MaskMat=Mat(Maskand,[1])
print('now,Cir to Mat,I fill Blank with 1 to make it more complex<Maybe>')
MaskMat.Show()

Mat = MatMapping(list(range(50,200)),10,10)
Result = FilterIO(Mat,MaskMat,'Mask')


#Now,another things-Insert your data by angle
print('Insert data by an vector')
data=['A','B','C']
Vec=CirMapping([],10,1,[1,1],['M'])
Vec.model='Debug'
#Set Map's model as Debug to show some result on time<Maybe useless>
#Now we set it just now,so it won't work before we operate more,So I have to Show it
Vec.ShowCir()
pi_6=0.5235988
Vec.AngleSet(pi_6,data)
#Now because of model-Debug,We needn't to ShowCir again,'ABC' has been inserted in vector (pi/6,3)
get = Vec.AngelGet(pi_6)[0:3]
#Also we can get by angle-vector with [0:4] to get element in order you want<Like what a list do>
print('This is not model-Debug print')
print(get)
