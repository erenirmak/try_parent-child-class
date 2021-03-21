from Mat_Parent_Child import *

a1 = int(input("Enter two numbers:\n"))
a2 = int(input())
p = input("Enter the symbol of your operation:\n")

mat = Mat_Islemleri(a1, a2, p)
print("Result: ", mat.result)

artm = Aritmetik(a1, a2)
print("\nArithmetic average of your values: ", artm.ave)
