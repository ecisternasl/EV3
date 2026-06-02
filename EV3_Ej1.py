total_comandantes = 0
total_cadetes = 0
error_contador = 0

print("=== Academia De Pilotos Estelar ===")

while True:
    try:
        cantidad = int(input("¿Cuántos pilotos desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento.")
    except ValueError:
        print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento.")

for i in range(cantidad):
    print("--- Registro del Piloto ---")
    
    while True:
        nombre = input("Ingrese Nombre Cósmico: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Error: El nombre debe tener al menos 6 caracteres y no incluir espacios.")
        
    while True:
        try:
            nivel = int(input("Ingrese Nivel de Vuelo: "))
            if nivel > 0:
                break
            else:
                print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")
        except ValueError:
            print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")

    if nivel > 40:
        print(f"Resultado: El piloto {nombre} es un Comandante Galáctico.")
        total_comandantes += 1
    elif nivel <= 40 or nivel == 40:
        print(f"Resultado: El piloto {nombre} es un Cadete Estelar.")
        total_cadetes += 1
    else:
        error_contador += 1
        print("Nivel no reconocido.")

print(f"¡La flota estelar cuenta con {total_comandantes} Comandantes Galácticos y {total_cadetes} Cadetes Estelares! ¡Prepárense para despegar!")
