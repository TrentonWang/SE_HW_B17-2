#   鸡兔同笼问题
#   假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只？
#   假设鸡有 a 只 ， 兔子是 （30-a）只
a = 0
for a in range (1,30,1):
    if (2*a+(30-a)*4 == 90):
        print("鸡有"+str(a)+"只"+" 兔子有"+str((30-a))+"只")
#   程序运行结果：
#   鸡有15只 兔子有15只
