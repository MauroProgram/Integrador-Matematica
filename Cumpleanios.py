# Programa para operaciones con años de nacimiento: conteo, condiciones y producto cartesiano

def esBisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def calcularEdad(anioNacimiento, anioActual=2025):
    return anioActual - anioNacimiento

def productoCartesiano(conjunto1, conjunto2):
    return {(x, y) for x in conjunto1 for y in conjunto2}

def main():
    # Ingreso de años de nacimiento
    print("Ingrese los años de nacimiento (ingrese 'fin' para terminar):")
    aniosNacimiento = []
    aniosSet = set()  # Para verificar duplicados
    while True:
        entrada = input("Año de nacimiento: ")
        if entrada.lower() == 'fin':
            break
        if entrada.isdigit():
            anio = int(entrada)
            if anio in aniosSet:
                print("Año repetido, por favor ingrese un año ficticio diferente.")
            elif 1900 <= anio <= 2025:  # Validar rango razonable
                aniosNacimiento.append(anio)
                aniosSet.add(anio)
            else:
                print("Por favor, ingrese un año entre 1900 y 2025.")
        else:
            print("Por favor, ingrese un año válido (solo números).")

    if not aniosNacimiento:
        print("No se ingresaron años de nacimiento.")
        return

    # Contar años pares e impares
    pares = 0
    impares = 0
    for anio in aniosNacimiento:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"\nAños pares: {pares}")
    print(f"Años impares: {impares}")

    # Verificar si todos nacieron después del 2000
    if all(anio > 2000 for anio in aniosNacimiento):
        print("Grupo Z")

    # Verificar si algún año es bisiesto
    if any(esBisiesto(anio) for anio in aniosNacimiento):
        print("Tenemos un año especial")

    # Calcular edades actuales
    edades = [calcularEdad(anio) for anio in aniosNacimiento]
    print("\nEdades actuales (en 2025):")
    for i, (anio, edad) in enumerate(zip(aniosNacimiento, edades)):
        print(f"Persona {i+1} (nacida en {anio}): {edad} años")

    # Producto cartesiano entre años y edades
    aniosConjunto = set(aniosNacimiento)
    edadesConjunto = set(edades)
    prodCartesiano = productoCartesiano(aniosConjunto, edadesConjunto)
    print("\nProducto cartesiano (años, edades):")
    print(prodCartesiano)

if __name__ == "__main__":
    main()