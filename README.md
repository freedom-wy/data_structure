# data_structure
## 数据结构与算法
### 1、算法的引入
#### （1）、如果a+b+c=1000，且a^2+b^2=c^2，(a,b,c为自然数)，求出所有a,b,c可能的组合
##### 01.py
```python
import time

start_time = time.time()

for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c==1000 and a**2+b**2==c**2:
                print("a,b,c的值为:a=%d,b=%d,c=%d"%(a,b,c))

end_time = time.time()
time_value = end_time-start_time
print("程序耗时:%d"%time_value)
```
```text
a,b,c的值为:a=0,b=500,c=500
a,b,c的值为:a=200,b=375,c=425
a,b,c的值为:a=375,b=200,c=425
a,b,c的值为:a=500,b=0,c=500
程序耗时:160
```
##### 对上面的代码进行优化
```python
import time

start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
            c = 1000-a-b
            if a**2+b**2==c**2:
                print("a,b,c的值为:a=%d,b=%d,c=%d"%(a,b,c))

end_time = time.time()
time_value = end_time-start_time
print("程序耗时:%d"%time_value)
```
```text
a,b,c的值为:a=0,b=500,c=500
a,b,c的值为:a=200,b=375,c=425
a,b,c的值为:a=375,b=200,c=425
a,b,c的值为:a=500,b=0,c=500
程序耗时:1
```
***
#### (2)、时间复杂度:
```text
假定计算机执行算法每个基本操作的时间是固定的一个时间单位，那么有多少个基本操作就代表会花费多少时间单位.
虽然对于不同的机器环境而言，确切的单位时间是不同的，但是对于算法进行多少个基本操作（即花费多少时间单位）在规模数量及上却是相同的。
由此可以忽略机器环境的影响而客观的反应算法的时间效率。
```
最优时间复杂度，算法完成工作最少需要多少基本操作，即最优时间复杂度。  
最坏时间复杂度，算法完成工作最多需要多少基本操作，即最坏时间复杂度。  
平均时间复杂度，算法完成工作平均需要多少基本操作，即平均时间复杂度。  
**主要关注最坏时间复杂度。**
#### （3）、时间复杂度计算
1、对于基本步骤来说，时间复杂度为O(1)  
2、对于顺序结构来说，时间复杂度要采用加法来计算  
3、对于循环结构来说，时间复杂度要采用乘法来计算  
4、对于条件分支结构来说，时间复杂度要采用最大值来计算
```python
import time

start_time = time.time()
for a in range(0,1001):
    for b in range(0,1001):
            c = 1000-a-b
            if a**2+b**2==c**2:
                print("a,b,c的值为:a=%d,b=%d,c=%d"%(a,b,c))

end_time = time.time()
time_value = end_time-start_time
print("程序耗时:%d"%time_value)
# 时间复杂度为T(n) = O(n^2)
```