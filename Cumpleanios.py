# Programa para operaciones con años de nacimiento: conteo, condiciones y producto cartesiano

def es_bisiesto(anio):
    """
    Verifica si un año es bisiesto.
    
    Args:
        anio (int): Año a evaluar.
    
    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def calcular_edad(anio_nacimiento, anio_actual=2025):
    """
    Calcula la edad actual basada en el año de nacimiento.
    
    Args:
        anio_nacimiento (int): Año de nacimiento.
        anio_actual (int): Año actual (por defecto 2025).
    
    Returns:
        int: Edad calculada.
    """
    return anio_actual - anio_nacimiento

def producto_cartesiano(conjunto1, conjunto2):
    """
    Calcula el producto cartesiano entre dos conjuntos.
    
    Args:
        conjunto1 (set): Primer conjunto (ej. años de nacimiento).
        conjunto2 (set): Segundo conjunto (ej. edades).
    
    Returns:
        set: Conjunto de tuplas representando el producto cartesiano.
    """
    return {(x, y) for x in conjunto1 for y in conjunto2}

def main():
    """
    Función principal que coordina la entrada de años de nacimiento, realiza cálculos
    y evaluaciones, y genera el producto cartesiano.
    """
    # Ingreso de años de nacimiento
    print("Ingrese los años de nacimiento (ingrese 'fin' para terminar):")
    anios_nacimiento = []
    anios_set = set()  # Para verificar duplicados
    while True:
        entrada = input("Año de nacimiento: ")
        if entrada.lower() == 'fin':
            break
        if entrada.isdigit():
            anio = int(entrada)
            if anio in anios_set:
                print("Año repetido, por favor ingrese un año ficticio diferente.")
            elif 1900 <= anio <= 2025:  # Validar rango razonable
                anios_nacimiento.append(anio)
                anios_set.add(anio)
            else:
                print("Por favor, ingrese un año entre 1900 y 2025.")
        else:
            print("Por favor, ingrese un año válido (solo números).")

    if not anios_nacimiento:
        print("No se ingresaron años de nacimiento.")
        return

    # Contar años pares e impares
    pares = 0
    impares = 0
    for anio in anios_nacimiento:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"\nAños pares: {pares}")
    print(f"Años impares: {impares}")

    # Verificar si todos nacieron después del 2000
    if all(anio > 2000 for anio in anios_nacimiento):
        print("Grupo Z")

    # Verificar si algún año es bisiesto
    if any(es_bisiesto(anio) for anio in anios_nacimiento):
        print("Tenemos un año especial")

    # Calcular edades actuales
    edades = [calcular_edad(anio) for anio in anios_nacimiento]
    print("\nEdades actuales (en 2025):")
    for i, (anio, edad) in enumerate(zip(anios_nacimiento, edades)):
        print(f"Persona {i+1} (nacida en {anio}): {edad} años")

    # Producto cartesiano entre años y edades
    anios_conjunto = set(anios_nacimiento)
    edades_conjunto = set(edades)
    prod_cartesiano = producto_cartesiano(anios_conjunto, edades_conjunto)
    print("\nProducto cartesiano (años, edades):")
    print(prod_cartesiano)

if __name__ == "__main__":
    """
    Punto de entrada del programa. Ejecuta la función principal.
    """
    main()