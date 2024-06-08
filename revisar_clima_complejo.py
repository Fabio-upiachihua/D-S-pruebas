def revisar_clima(clima, dia, hora):
    """
    Determina si necesitas llevar un paraguas según el clima, el día y la hora.
    
    Parámetros:
    clima (str): El clima actual, puede ser "lluvioso", "nublado" o "soleado".
    dia (str): El día de la semana.
    hora (int): La hora del día en formato 24 horas.
    
    Retorna:
    str: Un mensaje indicando si necesitas llevar un paraguas o no.
    """
    if clima == "lluvioso":
        if dia in ["sábado", "domingo"]:
            return "Es fin de semana y está lloviendo, lleva un paraguas."
        else:
            return "Está lloviendo, lleva un paraguas."
    elif clima == "nublado":
        if hora < 12:
            return "Está nublado por la mañana, podría llover, lleva un paraguas por si acaso."
        else:
            return "Está nublado por la tarde, no necesitas paraguas."
    else:
        return "No necesitas paraguas."


# Pruebas de Cobertura de Sentencia
def pruebas_cobertura_sentencia():
    """
    Ejecuta pruebas para asegurar que todas las sentencias del código se ejecuten al menos una vez.
    """
    # Prueba cuando el clima es lluvioso y es fin de semana
    print(revisar_clima("lluvioso", "sábado", 10))  # "Es fin de semana y está lloviendo, lleva un paraguas."

    # Prueba cuando el clima es lluvioso y no es fin de semana
    print(revisar_clima("lluvioso", "lunes", 10))  # "Está lloviendo, lleva un paraguas."

    # Prueba cuando el clima es nublado por la mañana
    print(revisar_clima("nublado", "lunes", 9))  # "Está nublado por la mañana, podría llover, lleva un paraguas por si acaso."

    # Prueba cuando el clima es nublado por la tarde
    print(revisar_clima("nublado", "lunes", 15))  # "Está nublado por la tarde, no necesitas paraguas."

    # Prueba cuando el clima es soleado
    print(revisar_clima("soleado", "lunes", 10))  # "No necesitas paraguas."


# Pruebas de Cobertura de Decisión
def pruebas_cobertura_decision():
    """
    Ejecuta pruebas para asegurar que todas las decisiones (condiciones) se evalúen como verdaderas y falsas.
    """
    # Prueba cuando el clima es lluvioso y es fin de semana (if clima == "lluvioso" y if dia in ["sábado", "domingo"] son verdaderos)
    print(revisar_clima("lluvioso", "sábado", 10))  # "Es fin de semana y está lloviendo, lleva un paraguas."

    # Prueba cuando el clima es lluvioso y no es fin de semana (if clima == "lluvioso" es verdadero, if dia in ["sábado", "domingo"] es falso)
    print(revisar_clima("lluvioso", "lunes", 10))  # "Está lloviendo, lleva un paraguas."

    # Prueba cuando el clima es nublado por la mañana (if clima == "nublado" y if hora < 12 son verdaderos)
    print(revisar_clima("nublado", "lunes", 9))  # "Está nublado por la mañana, podría llover, lleva un paraguas por si acaso."

    # Prueba cuando el clima es nublado por la tarde (if clima == "nublado" es verdadero, if hora < 12 es falso)
    print(revisar_clima("nublado", "lunes", 15))  # "Está nublado por la tarde, no necesitas paraguas."

    # Prueba cuando el clima es soleado (if clima == "lluvioso" y if clima == "nublado" son falsos)
    print(revisar_clima("soleado", "lunes", 10))  # "No necesitas paraguas."


# Ejecución de las pruebas
if __name__ == "__main__":
    print("Pruebas de Cobertura de Sentencia:")
    pruebas_cobertura_sentencia()
    
    print("\nPruebas de Cobertura de Decisión:")
    pruebas_cobertura_decision()
