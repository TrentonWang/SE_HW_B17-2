#2.鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

for ji in range(0,31):
    if 2*i+(30-i)*4==90:
        print("鸡有:",i,"兔有:",30-i
