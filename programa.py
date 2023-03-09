# programa para identificar de manera ascendente 3 numeros

print("----------------------------------------")
print("----orden ascendente de tres numeros----")
print("----------------------------------------")

# input
n1=int(input("ingrese un digito: "))
n2=int(input("ingrese un digito: "))
n3=int(input("ingrese un digito: "))

# procesing
prueba=n1<n2
if(prueba==True):

    if(n2<n3):
        rta= str(n1) + " " + str(n2) + " " + str(n3)
    else:
        if(n1<n3):
            rta= str(n1) + " " +  str(n3) + " " +  str(n2)
        else:
            rta= str(n3) + " " +  str(n1) + " " +  str(n2)
else:
    if(n1<n3):
        rta= str(n2) + " " +  str(n1)+ " " +  str(n3)
    else:
        if(n2<n3):
            rta =str(n2) + " " + str(n3) + " " +  str(n1)
        else:
            rta = str(n3) + " " +  str(n2) + " " +  str(n1)

# output 
print(rta)

