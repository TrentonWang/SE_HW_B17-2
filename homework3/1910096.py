# 指出一下程序的错误之处,并修改正确。
# 2k = -9     ---变量命名格式错误，以数字开头
#   if 2k>= 0:  ---if前方有空格
#     with = 2k +"正数"   ----with为内置关键字with更改为with1即可
#                         ----- 且字符串(str)与数字(int)不能使用+进行拼接，应该将k转换类型为字符串
#         print(with)     ----更改为print(with1)
#     else:              -----同一级别的代码，缩进必须一致。这里if与else是同一级别代码
#     print(2K+ '负数")   -----1.python对字符串的表示方法有单引号'' 双引号" " 三引号 """ """ ''' '''，但没有' "
#                         -----2.字符串(str)与数字(int)不能使用+进行拼接，应该将k2转换类型为字符串
#                         -----3.变量名字没有区分大小写以及使用数字开头，错误，将2K改为k


k = -9
if k >= 0:
    with1=str(k)+"正数"
    print(with1)
else:
    print(str(k)+"负数") 