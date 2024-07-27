#!/usr/bin/env python3
# Student ID: iaoluwajuwon

def function1():
    schoolName = 'SICT'  
    print('print() in function1 on schoolName:', schoolName)
    return schoolName

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)
    return schoolName

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
returned_school1 = function1()  
print('print() in main on schoolName:', returned_school1)  
returned_school2 = function2()  
print('print() in main on schoolName:', returned_school2)  

