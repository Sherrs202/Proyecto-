## esta función la hago para caulcular la propina que van a dejar 
def propina (Prop,SumaT):
        P = Prop * SumaT/100
        return P


## Aqui logro calcular el total de toda la compra
def Total(P,SumaT) :
        Total = P + SumaT
        return Total

## Esta función sirve para saber que tequila quiere y dependiendo del tequila 
# el precio se ajusta 

def Tequilas (T):
    Suma = 0
    if T == "centenario plata":
            Precio = 90
            Suma = Suma + Precio 
            return Suma
    
    else:
           if T == "cuervo especial":
                  Precio = 90
                  Suma = Suma + Precio 
                  return Suma
           else :
                  if T == "Tradicional reposado":
                         Precio = 100
                         Suma = Suma + Precio 
                         return Suma
                  return 0


SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")

while R == "S":
        print ("Ingresa tu bebida")
        bebida = input()
    
        if bebida == "Tequila":
              Teq = input("Que tequila quieres?")
              Precio = Tequilas (Teq)
              SumaT = SumaT + Precio 
        
        else:
            if bebida == "Cerveza":
                Precio = 55
                SumaT = SumaT + Precio
        
            else:
                if bebida == "Whisky":
                    Precio = 100
                    SumaT = SumaT + Precio
            
                else:
                    print("Bebida no registrada")
        
            
        Respuesta = input("Quiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break

print("quiere dejar propina? (S/N)")
R = input()
if R == "S" :
     Prop = int(input("Cuanto porcentaje de propina quiere dejar?"))
     P = propina (Prop,SumaT)
     print("Tu total sin propina es", SumaT)
     print("La propina es de ", P)
     print ("Tu total a pagar con propina es:",Total(P,SumaT))
else :
    print ("Tu total a pagar es:", SumaT)
