1 将给定字符串的PHP替换为Python      

best_language = "PHP is the best programming language in the world! "
'''
best_language = "PHP is the best programming language in the world! "
word=best_language.replace("PHP","Python")

print(word)

'''
Python is the best programming language in the world! 
'''
'''
2 编写代码，提示用户输入1 - 7
七个数字，分别代表周一到周日，打印输出“今天是周几”

print("第二题")
day_num = input('请输入阿拉伯数字1-7：')
dic={'1':'周一','2':'周二','3':'周三','4':'周四','5':'周五','6':'周六','7':'周日'}
print('今天是'+dic.get(day_num))
print()

3 给定一个字符串： Python is the BEST programming Language！
   编写一个正则表达式用来判断该字符串是否全部为小写。
print("第三题")
import re
fyjstr = 'Python is the BEST programming Language！'
fyj = re.search('^[a-z]+$', fyjstr)
if fyj:
    print (fyj.group(), '全为小写!' )
else:
    print (fyjstr, "不全是小写！")
# 测试字符串全为小写的情况
fyjstr = 'python'
fyj = re.search('^[a-z]+$', fyjstr)
if fyj:
    print (fyj.group(), '全为小写!' )
else:
    print (fyjstr, "不全是小写！")
print()

4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：

（xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
import re
word=input("请输入您的个人信息\n")

phone = re.search(r"(\d{3}-\d{3}-\d{4})",word)
if phone=="":
    phone=re.search(r"(\d{3}-\d{4})",word)
    
print(phone)
'''
请输入您的个人信息
123-4567-555-4444-44444-44444
None
请输入您的个人信息
567-555-4444-44444-44444
<re.Match object; span=(0, 12), match='567-555-4444'>

'''
'''

题目<5>
利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
day = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
dateday = re.compile(r'\d{4}-\d{2}-\d{2}')
dateday = dateday.findall(day)
print("".join(dateday))

