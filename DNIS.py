def obtenerDigitosUnicos(dni):
    return set(str(dni))

def contarFrecuenciaDigitos(dni):
    frecuencia = {}
    for i in str(dni):
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1
    return frecuencia

def sumaDigitos(dni):
    return sum(int(i) for i in str(dni))

def main():
    print("Ingrese los números de documento o ingrese 'fin' para terminar:")
    dnis = []
    while True:
        entrada = input("DNI: ")
        if entrada.lower() == 'fin':
            break
        if entrada.isdigit():
            dnis.append(entrada)
        else:
            print("Por favor, ingrese un DNI válido solo números")

    # Validar que se ingresaron al menos 2 DNIs
    if len(dnis) < 2:
        print("Se necesitan al menos dos números de documento para realizar las operaciones")
        return

    # Generación de conjuntos de dígitos únicos para cada DNI
    conjuntos = [obtenerDigitosUnicos(dni) for dni in dnis]

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
    diferenciaSimetrica = set.symmetric_difference(*conjuntos) if len(conjuntos) == 2 else "No disponible para más de 2 conjuntos"
    print(f"Diferencia simétrica: {diferenciaSimetrica}")

    # Frecuencia de dígitos por DNI
    print("\nFrecuencia de dígitos por DNI:")
    for i, dni in enumerate(dnis):
        frecuencia = contarFrecuenciaDigitos(dni)
        print(f"DNI {i+1}: {frecuencia}")

    # Suma total de dígitos por DNI
    print("\nSuma total de dígitos por DNI:")
    for i, dni in enumerate(dnis):
        suma = sumaDigitos(dni)
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
    main()