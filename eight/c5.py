
# 参数 不同在参数的调用上
# 1. 必须参数  按照顺序
# 2. 关键字参数 不用按照顺序，但是用的话必须全部用关键字参数，保持一致，不能混合着用
# 3. 默认参数

def add(x,y):
    return x,y

# c = add(1,2) 1,2

# 关键字参数，提高代码可读性
c = add(y=1,x=2) #2,1

print(c)

# 默认参数
# 1. 非默认参数在前[不用关键字]，默认必须在后
# 2. [可以用关键字，不用按照顺序]
# 3. 可以结合关键字参数用【缺省两个，只用一个关键字写age = 17 AND 若表现三个必须都是关键字参数，不能混合着用】
def add(x=10,y=20):
    return x,y

c = add()

def print_student(name,gender='男',age=18,college='人民路小学'):
    pass