# -*- coding: utf-8 -*-
"""
默认情况：
输入类型为列表，元素为字符串
输出为字符串
"""
def longest_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    #单独处理空字符串
    if not strs:
        return ""
    #初始化前缀
    str_min = strs[0]
    #遍历整个列表的字符串
    for str in strs[1:]:
        #遍历字符串的每一个字符
        for i,ch in enumerate(str):
            #如果字符串的长度超过储存的前缀长度，跳出循环，否则会报错，如["a","ab"]
            if i == len(str_min):break
            #如果遇到字符串的字符与前缀的字符不符，刷新前缀，跳出循环，如["ab","ac"]
            elif ch != str_min[i]:
                str_min = str_min[:i]
                break
        #如果被遍历的字符串包含于前缀，则把前缀刷新为被遍历的字符串，如["abc","ab"]
        if len(str_min) > len(str): str_min = str
        #如果是空字符串，直接返回空字符串
        if str_min == "": return ""
    #如果不是空字符串，返回前缀
    return str_min

#test1 = ["a","b","c"]
#test2 = []
#test3 = [""]
#test4 = ["abc","ab"]
#test5 = ["a","abc","ab"]
