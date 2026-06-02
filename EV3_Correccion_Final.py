print("Bienvenido al sistema de gestion de cupos del Gimnasio Titan!")

cupos = 75
historial = 0 
cant = 0 

while True:
    print(" === Menu principal === ")
    print("1. Cupos disponibles.")
    print("2. Realizar reserva.")
    print("3. Cancelar reserva.")
    print("4. Historial de reservas.")
    print("5. Salir")

    opc = int(input("Seleccione una opcion:  "))
    
    if opc == 1:
        print(f"Los cupos disponibles actuales son: {cupos}")
    
    elif opc == 2: 
        #Guarde el dato ingresado en Historial en vez de usar cant
        cant = int(input("Ingrese la cantidad de cupos que desea reservar:  "))
        
        #Use una variable vacia y no controle que no se pudiera reservar mas del cupo disponible
        if cant <= 0 or cant > cupos:
            print("Error, numeracion invalida")
        else:
            #Hice formulas cruzadas que alteraban mal los cupos y el historial, me ponia los numeros en negativo
            cupos -= cant
            historial += cant
            print("Reserva realizada")

    elif opc == 3:
        cant = int(input("Cuantas reservas deseas cancelar?:  "))
        #Puse mal la condición del if y decia "Exito" cuando se ingresaba un numero invalido
        if cant <= 0 or cant + cupos > 75:
            print("Error, cantidad invalida")
        else: 
        #Reste los cupos en vez de sumarlos para devolverlos
            cupos += cant
            historial -= cant
            print("Reserva cancelada")
    
    elif opc == 4:
        print(f"Historial de reservas actualmente: {historial}  ")

    elif opc == 5:
        print("Gracias por utilizar nuestro Software, hasta la proxima!")
        break

    else:
        print("Numeracion invalida")