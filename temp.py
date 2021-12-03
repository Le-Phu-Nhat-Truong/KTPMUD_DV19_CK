# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def KT(arr):
    count =0
    for i in arr:
        if(i<2):
            count=count+1
        else:
            for j in range (2,i-1):
                if(i%j==0 and j<i):
                    count= count+1
                    break
    return len(arr)-count
a= [1,5,6,7,11]
print(KT(a))

#hàm kiểm tra số nguyên tố
def check_prime_number(n):

    flag = 1
    if (n <2):
        flag = 0
        return flag  
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break 
    return flag

check_prime_number(11)

def check_min_2_prime(a):
    
  count=0
  for i in range(0,len(a)):
    if(check_prime_number(a[i])==1):  # nếu a[i ] là số nguyên tố
     count=count+1 # tăng biến đếm
  if count>=2:
    return True
  else :
    return False


#mảng không có số nguyên tố
a=[1,4,6,8]
res=check_min_2_prime(a)
res

#mảng có 1 số nguyên tố
a=[1,2,4,6]
res1=check_min_2_prime(a)
res1

#mảng có phần tử không phải số nguyên
a=[2,4,6,8]
res2=check_min_2_prime(a)
res2

n = float(input("Moi nhap real_number: "))
m = float(input("Moi nhap image_number: "))
class Sothuc :
    def __init__(self,real_number) :
        self.real_number = real_number
    def gttd(self) :
        return (self.real_number *2) * 0.5

class Sophuc(Sothuc) :
    def __init__(self,real_number, image_number) :
        super().__init__(real_number)
        self.image_number = image_number
    def module(self) :
        return (self.image_number**2 + self.real_number**2) ** 0.5

sothuc = Sothuc(n)
print("Tri tuyet doi co gia tri la: ",sothuc.gttd())

sophuc = Sophuc(n,m)
print("module cua so phuc la: ",sophuc.module())

