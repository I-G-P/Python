import math

l=float(input())
w=float(input())
a=float(input())

area_of_how = (l*100)*(w*100)
area_of_wd = (a*100)**2
area_of_bench = area_of_how/10
free_space = area_of_how-area_of_wd-area_of_bench
number_of_dencer = free_space/(40+7000)
print(math.floor(number_of_dencer))