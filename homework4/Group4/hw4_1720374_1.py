count = 0
a = 0
b = 0
for a in range(int(100/5)):
    for b in  range(int(100/3)):
        if(5*a+3*b+(100-a-b)/3==100):
print("����"+str(a)+"ֻ��"+"ĸ��"+str(b)+"ֻ��"+"С��"+str((100-a-b))+"ֻ")
          count=count+1
print("����"+str(count)+"����")
