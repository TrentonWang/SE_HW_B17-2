
#   编写程序，计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？
#   设a为公鸡 b为母鸡 100-a-b为小鸡的数量 count为购买方法次数
x = 0
y = 0
count = 0

for x in range(int(100/5)):

    for y in  range(int(100/3)):

        if(5*x+3*y+(100-x-y)/3==100):

            print("公鸡有"+str(x)+"只"+" 母鸡有"+str(y)+"只"+" 小鸡有"+str((100-x-y))+"只")

            count=count+1

print("一共有"+str(count)+"种买法")

# 公鸡有0只 母鸡有25只 小鸡有75只
# 公鸡有4只 母鸡有18只 小鸡有78只
# 公鸡有8只 母鸡有11只 小鸡有81只
# 公鸡有12只 母鸡有4只 小鸡有84只
# 一共有4种买法
