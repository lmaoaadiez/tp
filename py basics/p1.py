# greeting='hello'
# name='michael'
# person2='aadi'
# message=f'{greeting}, {name.replace('chael','dick')}. This is {person2}!'
# print(name)
# print(message)
# num=1;
# num+=3
# num*=10      
# print(num)
# num=3.75
# print(round(3.65,1))
# num1='400'
# num2='500'
# print(int(num1)+int(num2))
# c=['u','1uh','hu2','du45','ji4tg']
# c1=sorted(c)   
# print(c[0:])
# print(c1[0:])
# print('u ' in c)
# for darsh,aadi in enumerate(c,start=-2):
#     print(darsh,aadi) 
# cstr='-'.join(c)
# new=cstr.split('-')
# print(cstr)
# print(new)
# cs1={'his','math','phy','compsci'}
# art1={'his','math','des','art'}
# print(cs1.union(art1))
# student={'name': 'Aaditya','age':25,'c':['Math','Comp']}
# print(student.items())
# for key,value in student.items():
#     print(key,value)
# user = 'adminia'
# logged_in =True
# if user=='admin'or not logged_in :
#     print('Admin page')
# else:
#     print('Invalid login')
# def student(*args,**kwargs):
#     print(args)
#     print(kwargs)
# c=['math','art','science']   
# info={'name':'john','age':22} 
# student(*c,**info)
# from p2 import find,test
# import sys
# index= find('abracdabragiligilichoo','g')
# print(index)    
# print(test)
# print(sys.path)
# import calendar
# import datetime
# c=['his','math','phy','compsci']
# today=datetime.date.today()
# print(today)
# print(calendar.isleap(2020))
import os
print(os.getcwd())
os.chdir('C:\Users\Aaditya Gupta\OneDrive - Indian Institute of Technology Guwahati\Desktop')
print(os.getcwd())