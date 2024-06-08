def hacer_pastel():
    """
    Simula el proceso de hacer un pastel asegurándose de que cada paso se haga al menos una vez.
    """
    # Paso 1: Precalentar el horno
    print("Precalentando el horno...")

    # Paso 2: Mezclar los ingredientes secos
    print("Mezclando los ingredientes secos...")

    # Paso 3: Mezclar los ingredientes húmedos
    print("Mezclando los ingredientes húmedos...")

    # Paso 4: Combinar los ingredientes secos y húmedos
    print("Combinando los ingredientes secos y húmedos...")

    # Paso 5: Hornear el pastel
    print("Horneando el pastel...")

    return "Pastel listo!"


# Pruebas de Cobertura de Sentencia
def pruebas_cobertura_sentencia():
    """
    Ejecuta la prueba para asegurar que todas las sentencias del código se ejecuten al menos una vez.
    """
    resultado = hacer_pastel()
    print(resultado)


if __name__ == "__main__":
    pruebas_cobertura_sentencia()
