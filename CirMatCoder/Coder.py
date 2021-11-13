# -*- coding: utf-8 -*-
# @Time    : 2021/11/12/21:40:30
# @Author  : Vater Hu
# @FileName: CirMatCoder
# @Software: Pycharm
# @QQ: 1107818699

def NumToChr(data: list):
    '''
    将数组列表成组转化为UTF8编码的字符[推荐转为英文，多编码适用]
    :param data: 数组
    :return: 返回字符数组
    '''
    r=[]
    for n in data:
        r.append(chr(n))
    return r
