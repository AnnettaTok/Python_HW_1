# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("ВВедите число n: "))
m = int(input("ВВедите число m: "))
c = int(input("ВВедите число k: "))

if c%2==0 and c<m*n:
    print("yes")
else:
    print("no")