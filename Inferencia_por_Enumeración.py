# Definir la estructura de la red bayesiana
red_bayesiana = {
    "A": {"Probabilidad": 0.3},
    "B": {
        "Padres": ["A"],
        "Probabilidad": {(True,): 0.9, (False,): 0.2},
    },
    "C": {
        "Padres": ["A"],
        "Probabilidad": {(True,): 0.8, (False,): 0.1},
    },
}

# Función para calcular la probabilidad conjunta dada una configuración de variables
def calcular_probabilidad_conjunta(red, configuracion):
    probabilidad_conjunta = 1.0
    for variable, valor in configuracion.items():
        if "Padres" in red[variable]:
            padres = red[variable]["Padres"]
            probabilidad = red[variable]["Probabilidad"][(configuracion[padres[0]],)]
            probabilidad_conjunta *= probabilidad
        else:
            probabilidad_conjunta *= red[variable]["Probabilidad"]
    return probabilidad_conjunta

# Función para realizar inferencia por enumeración
def inferencia_por_enumeracion(red, variable_objetivo, evidencia):
    variables = list(red.keys())
    variables.remove(variable_objetivo)
    enumeraciones = []
    for valor in [True, False]:
        evidencia[variable_objetivo] = valor
        probabilidad_conjunta = calcular_probabilidad_conjunta(red, evidencia)
        enumeraciones.append((valor, probabilidad_conjunta))
    return enumeraciones

# Realizar inferencia para P(B|A=True)
variable_objetivo = "B"
evidencia = {"A": True, "B": True, "C": True}
resultados = inferencia_por_enumeracion(red_bayesiana, variable_objetivo, evidencia)

for valor, probabilidad in resultados:
    print(f"P({variable_objetivo}={valor}|A=True, B=True, C=True) = {probabilidad}")
