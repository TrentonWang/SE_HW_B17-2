#1720374�Ƶ���

user = {'����':'','�Ա�':'','����':''}
user['����'] = input('���������������')
user['�Ա�'] = input('����������Ա�')
user['����'] = int(input('������������䣺'))
print(f"�ҵ�����{user['����']}������{user['����']}�꣬�Ա�{user['�Ա�']},ϲ���ô���")
user['���']=input('�����������ߣ�')
user['��ϵ��ʽ']=input('�����������ϵ��ʽ��')
for key in user:
    print(key+':',user[key])
li = [11,22,33,22,22,44,55,77,88,99,11]
lq = list(set(li))
lq.sort(key=li.index)
print(lq)
set1 = set(lq)
dict1 = {}
for item in set1:
    dict1.update({item:lq.count(item)})
print(dict1)
li = [1,2,3,4,5,6,7,8,9]
liq = li[2:9:3]
print(liq)
s = 'python java php'
print(s[7:11])