##Proyecto
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
    if T == "1" :
            Precio = 90
            Suma = Suma + Precio 
            return Suma
    
    else:
           if T == "2" :
                  Precio = 90
                  Suma = Suma + Precio 
                  return Suma
           else :
                  if T == "3" :
                         Precio = 100
                         Suma = Suma + Precio 
                         return Suma
                  return 0

## Esta función sirve para calcular que whisky quieren y darles el precio 
def Whisky (W):
    Suma = 0
    if W == "1":
            Precio = 90
            Suma = Suma + Precio 
            return Suma
    
    else:
           if W == "2":
                  Precio = 100
                  Suma = Suma + Precio 
                  return Suma
           else :
                  if W == "3":
                         Precio = 170
                         Suma = Suma + Precio 
                         return Suma
                  return 0
## Función de Cervezas para calcular su precio y sumarlo 
def Cerveza (C):
      Suma = 0
      if C == "1":
            Precio = 55
            Suma = Suma + Precio 
            return Suma
      else :
            if C == "2":
                  Precio = 55
                  Suma = Suma + Precio
                  return Suma
            else : 
                  if C == "3":
                        Precio = 60
                        Suma = Suma + Precio
                        return Suma
                  else : 
                        if C == "4":
                              Precio = 60
                              Suma = Suma + Precio
                              return Suma 
## Funión para calcular el precio del Ron
def Ron (R):
      Suma = 0
      if R == "1":
            Precio = 90
            Suma = Suma + Precio
            return Suma
      else : 
            if R == "2":
                  Precio = 90
                  Suma = Suma + Precio 
                  return Suma 
            else:
                  if R == "3":
                        Precio = 90
                        Suma = Suma + Precio 
                        return Suma
                  else : 
                        if R == "4":
                              Precio = 95
                              Suma = Suma + Precio 
                              return Suma 
                                   
## Estos valores se los puse para lograr saber de cuales han consumido y si tienen una 
## queja que vayam a barra a preguntar
W = 0
C = 0
T = 0
ror = 0
SumaT=0
R = input ("Quiere registrar una bebida? (S/N): ")

while R == "S":
        print ("\nQue bebida quieres?")
        print ("Tequila\nCerveza\nWhisky\nRon\nBrandy\n")
        bebida = input()
    
        if bebida == "Tequila":
              print("\nQue tequila quieres?")
              print("1)Centenario plata\n2)Cuervo especial\n3)Tradicional reposado")
              Teq = input()
              Precio = Tequilas (Teq)
              SumaT = SumaT + Precio 
              T = T + 1
        
        else:
            if bebida == "Cerveza":
                print("\nQue cerveza quieres?")
                print("1)Corona\n2)Victoria\n3)Pacifico\n4)Ultra")
                Cer = input()
                Precio = Cerveza (Cer)
                SumaT = SumaT + Precio
                C = C + 1
        
            else:
                if bebida == "Whisky":
                    print("\nQue Whisky quieres?")
                    print("1)Etiqueta roja\n2)Etiqueta negra\n3)Black and White")
                    Wh = input()
                    Precio = Whisky (Wh)
                    SumaT = SumaT + Precio
                    W = W + 1
            
                else:
                    if bebida == "Ron":
                          print("\nQue ron quieres?")
                          print("1)Bacardi\n2)Potosi\n3)Matusalen Clasico\n4)Flor de Caña 7")
                          Ro = input ()
                          Precio = Ron (Ro)
                          SumaT = SumaT + Precio 
                          ror = ror  + 1
                    else:
                          print("Bebida no registrada")
                    
        
            
        Respuesta = input("\nQuiere registrar otra bebida? (S/N): ")
        
        if Respuesta == "N":
            break
if R == "N":
      print ("No debes nada")
else:
    print("Consumo total \n", T , "Tequila(s)\n", W , "Whisky(s)\n", C,"Cerveza(s)\n", ror , "Ron" )
    res = input("\nEs correcto (S/N)")
    if res =="N":
          print ("\nCheque con barra")
    else:      
        print("Quiere dejar propina? (S/N)")
        Res = input()
        if Res == "S" :
            Prop = int(input("Cuanto porcentaje de propina quiere dejar?"))
            P = propina (Prop,SumaT)
            print("Tu total sin propina es", SumaT)
            print("La propina es de ", P)
            print ("Tu total a pagar con propina es:",Total(P,SumaT))
        else :
            print ("Tu total a pagar es:", SumaT)
