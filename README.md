# CirMatCoder
A python package for secret coding

  You can find 3 folders In 'CirMarCoder'，and the package installer is in folder 'dist'
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
      CirxData(col,Num)
      ----For filling a list for a CirMap's Blank elements/area
          col : is one CirMap's attribute CirMap.col , a list with column number of every row of the CirMap 
          Num : an element,can be chr,int,float or any other class/type.The result return will fill with this element-Num
