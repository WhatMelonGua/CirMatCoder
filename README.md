# CirMatCoder
A python package for secret coding or some operation for a round shape object -<Maybe>-

  You can find 3 folders In 'CirMarCoder'，and the package installer is in folder 'dist'
  How to install?
  1-Select the CirMatCoder-0.2.tar and unzip it,you will get a folder named 'CirMatCoder-0.2'
  2-open the folder,and you'll find a python file named 'setup.py'
  3-Open the Cmd and use the command cd <path> (<path>means the path of 'setup.py')
  Then,command'python setup.py install'
  4-Cmd will show the result,and setup successful
  
  Then you can scan the folder named 'Demo',it includes 2 demos,for class and func of the package
  
  Class:
  1- CirMap : Like Matrix,but in a round shape
  2- MatMap : Matrix
  No more now
  
  Func:
  1- Func of CirMap
  .Blank()
      ----For filling the CirMap with list 'x' <The list is just the attribute 'x' of CirMap,you can show 'x' by             print(CirMap.x)>,and if the elements of x is too many for the CirMap's index,they'll overflow,won't store in CirMap
      no return,change the CirMap.cir
  
  .Draw()
      ----To Draw data in the CirMap<Show data by print(CirMap.data)>,at [CirMap.prow,CirMap.pcol],Also,too many data will cause overflow
      no return,change the CirMap.cir
  
  .Count()
      ----To count how many elements are in the CirMap
      return the number of elements,Integer
  
  .AngleGet(angle)       !-express angle like pi/6,not 60°
      ----Get elements in line of the vector (depend on the angle you input),this may be not so good as we think,some time the result can return elements in the same position's for twice
      return a list fill with the elements in the vector of CirMap

  .AngleSet(angle,set: list)       !-express angle like pi/6,not 60°
      ----Discovet elements in line of the vector(the same compute form of AngleGet) with set list input
      no return,change the CirMap.cir
 
  .Line()
      ----Return a list in line,elements from CirMap.cir's start to end
      return a list<list CirMap.cir's elements by row to a line>

  .LR()
      ----Mirror the CirMap,just reverse every row
      no return,change the CirMap.cir

  .Rotate()       !-to understand its work form,you can look Mat() in 3-Func to use
       ----Rotate the CirMap for pi/2(90°) clockwise,by transform CirMap to MatMap,then Rotate,then MatMap to CirMap,then data of upper edge lost!!!
       no return,change the CirMap.cir <if the CirMap full with data,no Blank,use Func 'ProtectCir(CirMap,x) to protect the data'>

  .ShowCir()
        ----Print the CirMap in a beautiful way,to show CirMap.cir in a round Shape,but not a line with many lists.
        no return,just print print print.

  2- Func of MatMap
  .Blank()
      ----For filling the MatMap with list 'x'<Just like CirMap's one>
      no return,change the MatMap.mat
  
  .Draw()
      ----To Draw data in the MatMap<Show data by print(MatMap.data)>,at [MatMap.prow,MatMap.pcol],Also,too many data will cause overflow<Just like CirMap's one>
      no return,change the MatMap.mat
  
  .Count()
      ----To count how many elements are in the MatMap
      return the number of elements,Integer
  
  .Line()
      ----Return a list in line,elements from MatMap.mat's start to end
      return a list<list CirMap.cir's elements by row to a line>

  .Rotate()      
       ----Rotate the MatMap for pi/2(90°) clockwise,MatMap won't lost data...   maybe not a pround thing
       no return,change the MatMap.mat

  .Show()
        ----Print the MatMap in a beautiful way,to show MatMap.mat in a matrix's Shape
        no return,just print print.  

  3- Func to use
  CirxData(col,Num)
      ----For filling a list for a CirMap's Blank elements/area <To understand the Blank,you can firstly see the Func named 'Blank' below>
            col : is one CirMap's attribute CirMap.col , a list with column number of every row of the CirMap 
            Num : an element,can be chr,int,float or any other class/type.The result return will fill with this element<the Num>
            return list for Blank 'x'

  MatxData(D,H,Num)
      ----Like CirxData,for a MatMap, row H, column D,fill with Num<any type>
            return list for Blank 'x'

  StrRow(row)
      ----For CirMap.ShowCir(),the yellow light row number,1 turn to 001,99 turn to 099,100 keep it self.
            row : the row number, a int type.
            return a char,or str len 1
  
  Mat(C,x=[0])
      ----Turn CirMap to MatMap,just keep CirMap.cir elements in their position for its Matrix,then fill Blank with x,a list<give a list just 1 element,will fill all with that element>
            C : a CirMap
            x : Blank list x
            return a MatMap
 
  Cir(M,x=[0])
      ----Turn MatMap to CirMap,won't directly cause lost of part of data,but when the MatMap rotate then turn to CirMap,data lost!!!
            M : a MatMap
            x : uh,you know ,Blank
            return a CirMap
  
  Axes(C)
      ----Get every elements' position [x,y] in a axes whose zero point is the center of the CirMap
            return a CirMap     < CirMap.data = [] , D,d equal to C.D,C.d, every element turn to its position >
 
  FilterIO(A,B,x)
       ----Like Mask function in Photoshop,B is Mask Map,A is Data Map, A and B shold have the same row,column number and Map type,x to fill Blank
             Tip<All Blank form is like CirMap.Blank(),Blank firstly,then we draw data of A to discover x>
             A : Data CirMap
             B : Mask Map
             x : uh,you know ,Blank
             return A after Mask function,won't change A self <For Mask Map, only the element in the position = 0,the Data Map's position's element turn to x>

  ProtectCir(C,x)
        ----To protect a full data CirMap before rotate,use it to return a new CirMap,bigger,2 rows , 2 columns more than before one,front and behind. 
              C : The data CirMap to protect
              x : Blank list
              return a bigger CirMap

  MatMapping(data: list, D: int, H: int, p=[1,1], x=[0]):
        ----Create a MatMap with data, column - D,row - H, data start position - p,and Blank list x
              p[0:1] is a list,but store to MatMap.prow & MatMap.pcol
               return a MatMap

  CirMapping(data: list, D: int, d=1, p=[1,1], x=[0]):
         ----Create a CirMap diameter - D(Axes), distance between 2 elements - d(Axes),and the same  to MatMapping's p , x
               return a CirMap


  Attribute:
  --CirMap
     {model, data, D, r=D/2, d, prow, pcol, x, row, cir, col]
  --MatMap
     {model, data, D, H, prow, pcol, x, mat]

  when Map.model = 'Debug', after you define it,some Func of it like \.Draw() .Rotate() .LR() .AngleSet() .AngleGet() .Line()/
  after use these func upper,the Map will Show itself for once
