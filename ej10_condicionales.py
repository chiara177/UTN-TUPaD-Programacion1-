hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").strip().upper()
mes = int(input("Ingrese el mes en el que se encuentra (1,12): "))
dia = int(input("Ingrese el dia que es hoy (1,31): "))




if (dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia <= 20 and mes == 3):
    
    match hemisferio:
    
        case "S" :
            print("verano")
            
        case "N" :
            print("Invierno")
            
        case _ :
            print("Hemisferio invalido")

elif (dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia <= 20 and mes == 6):
    
    match hemisferio:
        
        case "S" :
            print("Otoño")
            
        case "N" :
            print("Primavera")
        
        case _ :
            print("Hemisferio invalido") 
                
elif (dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia <= 20 and mes == 9):
    
    match hemisferio:
    
        case "S" :
            print("Invierno") 
            
        case "N" :
            print("Verano")
            
        case _ :
            print("Hemisferio invalido") 

elif (dia >= 21 and mes == 9) or mes == 10 or mes == 11 or (dia <= 20 and mes == 12):
    
    match hemisferio:
        
        case "S" :
            print("Primavera")
            
        case "N" :
            print("Otoño") 
            
        case _ :
            print("Hemisferio invalido")