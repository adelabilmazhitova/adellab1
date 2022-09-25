
import math
# 1problems
# n=int(input())
# for i in range(n+1):
#    print('Number is:',i,'and cube of the',i,'is',i**3)
##############
# 2 problems
# a=[10,20,30,40,50]
# for i in reversed(a):
#    print(i)
##############
# 3 problems
# n=int(input())
# print(math.factorial(n))
##############
# 4 problems
# n=int(input())
# s=0
# for i in range(1, n+1):
#   s+=i
# print(s)
###################
# 5 problems
# s = str(input('x='))
# x = len(s)
# i = 0
# x = x - 1
# k = 0
# while ((x - i) >= i):
#    if s[x - i] == s[i]:
#        i += 1
#    else:
#        k = 1
#        break
# if k == 1:
#  print("false")
# else:
#  print("true")
##############
#####циклы
# 1
# x=int(input())
# for i in range(x+1, 0, -1):
#   for j in range(i, 0, -1):
#      print(j, end=' ')
#   print()
#################
# 2
# x=int(input())
# for i in range(x+1):
#   for j in range(i, 0, -1):
#      print(i, end=' ')
#   print(' ')
#################
# лямда
# 1
# x=int(input())
# y=int(input())
# get_discount=lambda x,y: x-((x*y)/100)
# print(get_discount(x,y))
# 2
# x=int(input())
# S=0
# while x>0:
#   S+=x
#   x-=1
# print('sum_numbers =',S)
##3
is_triplet = lambda a, b, c: print('True') if (a * a + b * b) == c * c else print('False')
is_triplet(3, 4, 5)