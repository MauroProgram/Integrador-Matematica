# Programa para realizar operaciones con DNIs: conjuntos, frecuencias, sumas y condiciones lógicas

def obtener_digitos_unicos(dni):
    """
    Convierte un DNI en un conjunto de dígitos únicos.
    
    Args:
        dni (str): Número de DNI como cadena de texto.
    
    Returns:42
        set: Conjunto de dígitos únicos del DNI.
    """
    return set(str(dni))

def contar_frecuencia_digitos(dni):
    """
    Cuenta la frecuencia de cada dígito en un DNI usando un bucle.
    
    Args:
        dni (str): Número de DNI como cadena de texto.
    
    Returns:
        dict: Diccionario con los dígitos como claves y sus frecuencias como valores.
    """
    frecuencia = {}
    for digito in str(dni):
        if digito in frecuencia:
            frecuencia[digito] += 1
        else:
            frecuencia[digito] = 1
    return frecuencia

def suma_digitos(dni):
    """
    Calcula la suma total de los dígitos de un DNI.
    
    Args:
        dni (str): Número de DNI como cadena de texto.
    
    Returns:
        int: Suma de todos los dígitos del DNI.
    """
    return sum(int(digito) for digito in str(dni))

def main():
    """
    Función principal que coordina la entrada de DNIs, realiza operaciones de conjuntos,
    calcula frecuencias, sumas y evalúa condiciones lógicas.
    """
    # Ingreso de DNIs
    print("Ingrese los DNIs (ingrese 'fin' para terminar):")
    dnis = []
    while True:
        entrada = input("DNI: ")
        if entrada.lower() == 'fin':
            break
        if entrada.isdigit():
            dnis.append(entrada)
        else:
            print("Por favor, ingrese un DNI válido (solo números).")

    # Validar que se ingresaron al menos 2 DNIs
    if len(dnis) < 2:
        print("Se necesitan al menos 2 DNIs para realizar las operaciones.")
        return

    # Generación de conjuntos de dígitos únicos para cada DNI
    conjuntos = [obtener_digitos_unicos(dni) for dni in dnis]

    # Mostrar los conjuntos de dígitos únicos
    for i, (dni, conjunto) in enumerate(zip(dnis, conjuntos)):
        print(f"\nDNI {i+1}: {dni}")
        print(f"Conjunto de dígitos únicos: {conjunto}")

    # Operaciones de conjuntos
    print("\nOperaciones de conjuntos:")
    # Unión: combina todos los dígitos únicos de los DNIs
    union = set.union(*conjuntos)
    print(f"Unión: {union}")
    
    # Intersección: identifica los dígitos comunes a todos los DNIs
    interseccion = set.intersection(*conjuntos)
    print(f"Intersección: {interseccion}")
    
    # Diferencia: calcula los dígitos exclusivos de cada DNI respecto a los demás
    for i, conjunto in enumerate(conjuntos):
        diferencia = conjunto - set.union(*(conjuntos[:i] + conjuntos[i+1:]))
        print(f"Diferencia (DNI {i+1} - resto): {diferencia}")
    
    # Diferencia simétrica: calcula dígitos exclusivos entre dos DNIs (solo para 2 conjuntos)
    diferencia_simetrica = set.symmetric_difference(*conjuntos) if len(conjuntos) == 2 else "No disponible para más de 2 conjuntos"
    print(f"Diferencia simétrica: {diferencia_simetrica}")

    # Frecuencia de dígitos por DNI
    print("\nFrecuencia de dígitos por DNI:")
    for i, dni in enumerate(dnis):
        frecuencia = contar_frecuencia_digitos(dni)
        print(f"DNI {i+1}: {frecuencia}")

    # Suma total de dígitos por DNI
    print("\nSuma total de dígitos por DNI:")
    for i, dni in enumerate(dnis):
        suma = suma_digitos(dni)
        print(f"DNI {i+1}: {suma}")

    # Evaluación de condiciones lógicas
    print("\nEvaluación de condiciones:")
    # Verificar si hay dígitos comunes en todos los DNIs
    if interseccion:
        print("Dígito compartido")
    
    # Verificar si algún DNI tiene más de 6 dígitos únicos
    for i, conjunto in enumerate(conjuntos):
        if len(conjunto) > 6:
            print(f"Diversidad numérica alta en DNI {i+1}")

if __name__ == "__main__":
    """
    Punto de entrada del programa. Ejecuta la función principal.
    """
    main()