#1720374�Ƶ���

# 1 �������ַ�����PHP�滻ΪPython
# best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
print('�滻ǰ��'+best_language)
best_language = best_language.replace('PHP',"Python")
print("�滻��"+best_language)

# 2 ��д���룬��ʾ�û�����1 - 7
# �߸����֣��ֱ������һ�����գ���ӡ������������ܼ���

number=input('����1-7�߸����֣��ֱ������һ�����գ�')
#print(type(number))
if number=='1':
    print('��������һ')
elif number=='2':
    print('�������ܶ�')
elif number == '3':
    print('����������')
elif number == '4':
    print('����������')
elif number=='5':
    print('����������')
elif number=='6':
    print('����������')
else:
    print('����������')

# 3 ����һ���ַ����� Python is the BEST programming Language��
#   ��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��

 import re
 s1 = 'Python is the BEST programming Language'
 an = re.search('^[a-z]+$', s1)
 if an:
 print ('s1:', an.group(), 'ȫΪСд')
 else:
 print (s1,"��ȫΪСд��")

# 4 ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ����xxx�� xxx - xxxx��xxx - xxx - xxxx��

 import re
 str = "(021) 887 7654 010-556-6789 (025) 845-3362 05718472048 837922740"
 m = re.findall('((\d{3}\-|\(\d{3}\) )(\d{3})\-(\d{4}))', str)
 if m:
 for item in m:
 print (item[0])
 else:
 print('not match')

# 5 ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy - mm - dd��
# '������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',

str = '������2022/9/24,������2017/09/25,������2012-07-25,������2020��04��25'
ymd = re.compile(r'\d{4}-\d{2}-\d{2}')
ymd = ymd.findall(str)
print("".join(ymd))