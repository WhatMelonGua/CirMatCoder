# -*- coding: utf-8 -*-
# @Time    : 2021/11/12/21:40:30
# @Author  : Vater Hu
# @FileName: CirMatCoder
# @Software: Pycharm
# @QQ: 1107818699

import math

def CirxData(col,Num):
    '''
    x填充手段生成器，用于圆阵
    :param col: 列数数组，包含圆阵每行的列数
    :param Num: 默认填充数值int
    :return: 填充列表
    '''
    TNum=0
    r=[]
    for colNum in col:
        TNum+=colNum
    for i in range(TNum):
        r.append(Num)
    return r

def MatxData(D,H,Num):
    '''
    x填充手段生成器，用于矩阵
    :param D: 矩阵的宽[列数]
    :param H: 矩阵的高[行数]
    :param Num: 默认填充数值int
    :return: 填充列表
    '''
    r=[]
    for time in range(D*H):
        r.append(Num)
    return r

def StrRow(row):
    '''
    用于阵列Show方法的行标注<br>将行数[三位数以内]表示长度统一化，如1转为001，10转为010，999不变
    :param row: 行数
    :return: 返回Str格式的行数
    '''
    row+=1
    if row < 10:
        r='00'+str(row)
    elif row < 100:
        r='0'+str(row)
    else:
        r=str(row)
    return r

def Mat(C,x=[0]):
    '''
    将圆阵矩阵化，并返回一个矩阵MatMap
    :param C: 需转换的圆阵
    :param x: 转化后的矩阵数据空白处的填充手段[为list传入]
    :return: 返回转换后的矩阵类
    '''
    r=[]
    if len(x)==1:
        x=MatxData(C.row,C.row,x[0])
    for row in range(C.row):
        Jumper=0
        Keeper=[]
        n=C.row-C.col[row]
        if n>0:
            left=math.ceil(n/2)
            right=int(n/2)
        elif n==0:
            left=right=0
        else:
            pass
        for time in range(left):
            Keeper.append(x[Jumper+time])
        Jumper+=left
        for time in C.cir[row]:
            Keeper.append(time)
        Jumper+=C.col[row]
        for time in range(right):
            Keeper.append(x[Jumper+time])
        r+=Keeper
    r = MatMapping(r,C.row,C.row)
    return r

def Cir(M,D,d,x=[0]):
    '''
    将矩阵圆阵化，并返回一个圆阵CirMap
    :param M:需转换的矩阵
    :param D: 转化圆阵的目标直径
    :param d: 转换圆阵后字符间距
    :param x: 转化后的圆阵数据空白处的填充手段[为list传入]
    :return: 返回转换后的圆阵类
    '''
    p=[1,1]
    r=CirMapping(M.data,D,d,p,x)
    r.Blank()
    if M.H>r.row:
        up=math.ceil((M.H-r.row)/2)
        down=up+r.row
    else:
        up = 0
        down = M.H
    left=[]
    right=[]
    for col in r.col[0:M.H]:
        if M.D > col:
            left.append(math.ceil((M.D-col)/2))
            right.append(math.ceil((M.D-col)/2)+col)
        else:
            left.append(0)
            right.append(M.D)
    if M.H>r.row:
        crow=0
        for row in range(up,down):
            if M.D>r.col[crow]:
                ccol = 0
            else:
                ccol=int((r.col[crow]-M.D)/2)
            for col in range(left[crow],right[crow]):
                print(range(left[ccol],right[ccol]))
                r.cir[crow][ccol]=M.mat[row][col]
                ccol+=1
            crow+=1
    else:
        crow=math.ceil((r.row-M.H)/2)
        for row in range(up,down):
            if M.D > r.col[crow]:
                ccol = 0
            else:
                ccol = int((r.col[crow] - M.D) / 2)
            for col in range(left[crow],right[crow]):
                r.cir[crow][ccol]=M.mat[row][col]
                ccol+=1
            crow+=1
    return r

def Axes(C):
    '''
    将CirMap的文字坐标以Tuple[float,float]返回一个CirMap，一一对应
    :param C: 查询坐标的圆阵
    :return: 返回一个圆阵，内含Tuple表示的(x,y)坐标
    '''
    r=[]
    for row in range(C.row):
        Keeper=[]
        y=((C.row-1)/2-row)*C.d
        for col in range(C.col[row]):
            x=(col-(C.col[row]-1)/2)*C.d
            Keeper.append((x,y))
        r+=Keeper
    r=CirMapping(r,C.D,C.d)
    return r

def FilterIO(A,B,x):
    a = A
    b = B
    if type(A) == 'CirMap':
        for row in range(b.row):
            for col in range(b.col[row]):
                if b.cir[row][col]==0:
                    a.cir[row][col]=x
                else:
                    pass
    elif type(A) == 'MatMap':
        for row in range(b.H):
            for col in range(b.D):
                if b.cir[row][col] == 0:
                    a.cir[row][col] = x
                else:
                    pass
    return a

def ProtectCir(C,x):
    data=C.Line()
    D=C.D+2*C.d
    d=C.d
    r=CirMapping([],D,d)
    Kni=CirIn(r,C)
    for row in range(Kni.row):
        n = 0
        for col in range(Kni.col[row]):
            if Kni.cir[row][col] == 0:
                r.cir[row][col] = x
            else:
                if row <= C.row:
                    if n < C.col[row-1]:
                        r.cir[row][col]=data[n]
                        n+=1
                    else:
                        pass
    return r

def MatMapping(data: list, D: int, H: int, p=[1,1], x=[0]):
    '''
    矩阵绘图器，将传入data绘制为矩阵
    :param data: 传入需要转换的数据列表
    :param D: 传入矩阵长
    :param H: 传入矩阵高
    :param p: 传入数据开始储存的位置，默认为[1,1]
    :param x: 传入非数据区的填充手段，将根据顺序填充[为list]
    :return: 返回矩阵
    '''
    class MatMap():
        def __init__(self,data,D,H,p,x):
            self.model = 'M'
            self.data = data
            self.D = D
            self.H = H
            self.prow = p[0]
            self.pcol = p[1]
            self.mat=[]
            self.x = x
            if len(x)==1:
                self.x = MatxData(self.D,self.H,self.x[0])
            else:
                pass
        def Blank(self):
            self.mat=[]
            Jumper=0
            for row in range(H):
                Keeper=[]
                for col in range(D):
                    Keeper.append(self.x[Jumper+col])
                Jumper+=D
                self.mat.append(Keeper)
        def Draw(self):
            if not self.data and self.model=='Debug':
                print('\033[1:33m There is no data input!\033[0m')
            else:
                Jumper = 0
                Rprow = self.prow-1
                for row in range(Rprow,self.H):
                    if row == Rprow:
                        Rpcol=self.pcol-1
                    else:
                        Rpcol=0
                    for col in range(Rpcol,self.D):
                        if Jumper < len(self.data):
                            self.mat[row][col]=self.data[Jumper]
                            Jumper += 1
                        else:
                            break
                    pass
                if Jumper < len(self.data):
                    print('\033[1:31m Warning - The Circle may be too small,Data overflow!\033[0m')
                else:
                    pass
            if self.model=='Debug':
                self.Show()
            pass
        def Rotate(self):
            r=[]
            for row in range(self.H):
                Keeper = []
                for col in range(self.D):
                    Keeper.append(self.mat[col][row])
                r.append(Keeper)
            for row in r:
                row.reverse()
            self.mat=r
            if self.model=='Debug':
                self.Show()
            pass
        def Count(self):
            return self.D*self.H
        def Line(self):
            r=[]
            for row in range(self.H):
                for colobj in self.mat[row]:
                    r.append(colobj)
            return r
        def Show(self):
            print('\033[1:30m —————————————————————Mat————————————————————— \033[0m')
            for row in range(self.H):
                Space = '\033[1:33m' + StrRow(row) + '-\033[0m'
                print(Space, end='')
                print(self.mat[row])
            print('\033[1:30m —————————————————————END————————————————————— \033[0m')
    r=MatMap(data,D,H,p,x)
    r.Blank()
    r.Draw()
    return r



def CirMapping(data: list, D: int, d=1, p=[1,1], x=[0]):
    '''
    圆阵绘图器，将传入data绘制为圆形阵列
    :param data: 传入需要转换的数据列表
    :param D: 传入直径长度期望包含的字符数
    :param p: 传入数据开始储存的位置，默认为[1,1]
    :param x: 传入非数据区的填充手段，将根据顺序填充[为list]
    :return: 返回圆阵
    '''
    class CirMap():
        def __init__(self,data,D,d,p,x):
            self.model='C'
            self.data=data
            self.D=D
            self.r=D/2
            self.d=d                  #行间隔长度
            self.prow=p[0]
            self.pcol=p[1]
            self.x=x
            self.row=int(self.D/self.d)
            self.cir=[]                 #储存圆阵
            self.col=[]                 #储存圆阵每行的字符数
            for row in range(self.row):
                y = ((self.row-1)/2-row)*self.d  # 求行坐标y
                self.col.append(int(2*(self.r**2-y**2)**(1/2)/self.d))
            if len(x)==1:
                self.x = CirxData(self.col,self.x[0])
            else:
                pass
        def Blank(self):
            self.cir=[]
            Jumper = 0
            for row in range(self.row):
                if self.col[row]>0:
                    Keeper=[]
                    for col in range(self.col[row]):
                        Keeper.append(self.x[Jumper+col])
                    self.cir.append(Keeper)
                    Jumper += self.col[row]
                else:
                    print('\033[1:33m Exsit Blank Line!\n In row: \033[0m'+str(row))
            pass
        def Draw(self):
            if not self.data and self.model=='Debug':
                print('\033[1:33m There is no data input!\033[0m')
            else:
                Jumper = 0
                Rprow = self.prow-1
                Rpcol = self.pcol-1
                for row in range(Rprow,self.row):
                    if row == Rprow:
                        Rpcol = self.pcol - 1
                    else:
                        Rpcol = 0
                    for col in range(Rpcol,self.col[row]):
                        if Jumper < len(self.data):
                            self.cir[row][col]=self.data[Jumper]
                            Jumper += 1
                        else:
                            break
                    pass
                if Jumper < len(self.data):
                    print('\033[1:31m Warning - The Circle may be too small,Data overflow!\033[0m')
                else:
                    pass
            if self.model =='Debug':
                self.ShowCir()
        def Count(self):
            TNum = 0
            for colNum in self.col:
                TNum += colNum
            return TNum
        def AngelGet(self,angle:float):
            r=[]
            for n in range(math.ceil(self.r)):
                py = int(self.r - math.sin(angle) * n * self.d)
                px = int(self.col[py]/2 + math.cos(angle) * n * self.d)
                try:
                    r.append(self.cir[py][px])
                    if self.model == 'Debug':
                        print('Value- ' + str(self.cir[py][px]) + ' in Column:' + str(px + 1), ' Row:' + str(py + 1))
                except:
                    pass
            return r
        def AngleSet(self,angle:float,set:list):
            r = []
            for n in range(math.ceil(self.r)):
                if n < len(set):
                    py = int(self.r - math.sin(angle) * n * self.d)
                    px = int(self.col[py] / 2 + math.cos(angle) * n * self.d)
                    self.cir[py][px]=set[n]
                else:
                    pass
            if self.model =='Debug':
                self.ShowCir()
            return r
        def Line(self):
            r=[]
            for row in range(len(self.cir)):
                for ele in self.cir[row]:
                    r.append(ele)
            if self.model =='Debug':
                print(r)
            return r
        def LR(self):
            for row in self.row:
                row.reverse()
            if self.model == 'Debug':
                self.ShowCir()
        def Rotate(self):
            mat=Mat(self)
            mat.Rotate()
            r=Cir(mat,self.D,self.d)
            self.cir=r.cir
            if self.model == 'Debug':
                self.ShowCir()
        def ShowCir(self):
            print('\033[1:30m —————————————————————Cir————————————————————— \033[0m')
            for row in range(self.row):
                Space = '\033[1:33m' + StrRow(row) + '-\033[0m'
                for blank in range(math.ceil((self.D-(self.col[row]-1)*self.d)/2)):
                    Space = Space + ' . '
                print(Space,end='')
                print(self.cir[row])
            print('\033[1:30m —————————————————————END————————————————————— \033[0m')
    r = CirMap(data,D,d,p,x)
    r.Blank()
    r.Draw()
    return r


def Cirand(A,B,d,forward):
    '''
    获取两圆阵A对B的交集(保留B值)
    :param A: 圆阵A
    :param B: 圆阵B
    :param d: 两圆阵中心间距d
    :param forward: 取交方向W,A,S,D分别对应A于上、左、下、右交B
    :return: 返回交集圆阵的蒙版阵列，非交区域以0表示，交集区域以1表示
    '''
    divX=(A.r**2-B.r**2+d**2)/2*d
    if divX<=0:
        print('\033[1:31m There is no points find!Set 2 tangent \033[0m')
    def Judge(pos):
        x=pos[0]
        y=pos[1]
        if x<=divX:
            if y**2<B.r**2-(x-d)**2:
                return 1
            else:
                return 0
        elif x>divX:
            if y ** 2 < A.r ** 2 - x ** 2:
                return 1
            else:
                return 0
    Cir=Axes(A)
    r=[]
    for row in range(Cir.row):
        for col in range(Cir.col[row]):
            r.append(Judge(Cir.cir[row][col]))
    r=CirMapping(r,A.D,A.d)
    if forward == 'D':
        pass
    elif forward == 'A':
        for row in r.cir:
            row.reverse()
    elif forward == 'S':
        r.Rotate()
    elif forward == 'W':
        for row in r.cir:
            row.reverse()
        r.Rotate()
    return r

def CirIn(A,B):
    Cir=Axes(A)
    Limit=B.r
    r=[]
    def Judge(pos):
        x=pos[0]
        y=pos[1]
        if x**2+y**2<=Limit**2:
            return 1
        else:
            return 0
    for row in range(Cir.row):
        for col in range(Cir.col[row]):
            r.append(Judge(Cir.cir[row][col]))
    r = CirMapping(r, A.D, A.d)
    return r