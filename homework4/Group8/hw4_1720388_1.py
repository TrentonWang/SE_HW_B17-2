#1720388李东鸿
count = 0
a = 0
b = 0
for a in range(int(100/5)):
    for b in  range(int(100/3)):
        if(5*a+3*b+(100-a-b)/3==100):
            print("公鸡"+str(a)+"只，"+"母鸡"+str(b)+"只，"+"小鸡"+str((100-a-b))+"只")
            count=count+1
print("共有"+str(count)+"种买法")

#公鸡有0只 母鸡有25只 小鸡有75只
#公鸡有4只 母鸡有18只 小鸡有78只
#公鸡有8只 母鸡有11只 小鸡有81只
#公鸡有12只 母鸡有4只 小鸡有84只
#共有4种买法
