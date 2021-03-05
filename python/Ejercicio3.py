
A = input("Ingrese un valor: ")
B = input("Ingrese un valor: ")

print(" A   B :  Q ")
print(" 0   0 : ",int(A==B or A==B))
print(" 0   1 : ",int(A==B or A==A))
print(" 1   0 : ",int(B==B or A==B))
print(" 1   1 : ",int(A==A or A==A))



