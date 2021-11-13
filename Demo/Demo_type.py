from CirMatCoder import *

data=list('this is a key')

DC = CirMapping(data,11,1,[1,1],['-'])
'''
First,Let's Creat a CirMap by Func CirMapping
-data: Your data to store in the CirMap
-11: The CirMap's diameter,will influnce the content to store character——the number of row and column
-1: The distance between 2 characters,with diameter,it just work like an Axes,to ensure the x,y of the character in the CieMap.
    And the Zero Point is decided in the center of the CirMap
-[2,2]: Which positon<row column> your data start to store,ensure the length of your data.Or the data may overflow
-['-']: What to store in the blank area<the character in CirMap which is not defined will be placed in order of the content in list['-']>
        if you input a list just with an element,Blank will be all placed by the element,or you can give a long list,Blank will placed by index
'''
#Tip - The CirMap will first Blank all character with ['-']<or other list you input>,Then draw your data in position you input
#And your data will undiscover parts of Blank list elements you give, so pay attention to this situation!

print('It\'s DC')
DC.ShowCir()
'''
Now,We get a variable named 'DC',whose type is CirMap!
CirMap have some functions,For example-using CirMap.ShowCir() to print the Map in your Console<I don't know how to name it>
'''

Cir = CirMapping([],11,1,[1,1],[0])
#Now we get a new CirMap named 'Cir',Full of zero,with no data<a hollow list,can't be null!>
print('It\'s Cir')
#This CirMap's appearnce is more likely to a circular
Cir.ShowCir()

Cir.data=list(range(0,10))
#We can give a new data list<[0,1,...,9]>,and  assign it to Cir's attribute - data
Cir.Draw()
print('update the data now!')
#After update your data,you should use Func CirMap.Draw() to draw data on your CirMap,then show it!Find differements.
Cir.ShowCir()

#Also,There have Matrix,too;but I don't give MatMap so many Func now...
M = MatMapping(data,10,5,[5,2])
'''
Like Func CirMapping,give data,column,row & position to it
return a MatMap type Structrue
'''
print('There are a matrix!')
M.Show()
#you can see the 'Warning',the position is so big that the data can't be stored competely