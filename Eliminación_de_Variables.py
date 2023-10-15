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
            probabilidad = red[variable]["Probabilidad"][(valor,)]
            probabilidad_conjunta *= probabilidad
        else:
            probabilidad_conjunta *= red[variable]["Probabilidad"]
    return probabilidad_conjunta

# Función para eliminar una variable
def eliminar_variable(red, variable_a_eliminar, evidencia):
    variables = list(red.keys())
    variables.remove(variable_a_eliminar)
    probabilidad_total = 0.0
    for valor in [True, False]:
        evidencia[variable_a_eliminar] = valor
        probabilidad_conjunta = calcular_probabilidad_conjunta(red, evidencia)
        probabilidad_total += probabilidad_conjunta
    return probabilidad_total

# Realizar eliminación de variable para P(A=True|B=True)
variable_objetivo = "A"
variable_a_eliminar = "C"
evidencia = {"B": True}
probabilidad = eliminar_variable(red_bayesiana, variable_a_eliminar, evidencia)
resultado = probabilidad / eliminar_variable(red_bayesiana, variable_a_eliminar, evidencia)

print(f"P({variable_objetivo}=True|B=True) = {resultado}")
