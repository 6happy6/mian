"""
@Anthor: freya.yang
@Time: 2022/4/27 2:35 下午
@File: try..else和for..else.py
@description:
"""

# try else
try:
    raise ValueError
except Exception as e:
    print("error")
else:
    print("no error")
finally:
    print("finally")


# for else
for i in range(5):
    if i == 3:
        print(i)
        continue
else:
    print("for没有异常，进入else")


# for里有break，不能进入else
for i in range(5):
    if i == 3:
        break
else:
    print("for没有异常，进入else")