# Definir la estructura de la red bayesiana
red_bayesiana = {
    "Lluvioso": {"Probabilidad": 0.2},
    "Paraguas": {
        "Padres": ["Lluvioso"],
        "Probabilidad": {(True,): 0.9, (False,): 0.1},
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

# Calcular la probabilidad P(Paraguas=True|Lluvioso=True)
configuracion = {"Lluvioso": True, "Paraguas": True}
probabilidad_conjunta = calcular_probabilidad_conjunta(red_bayesiana, configuracion)

# Calcular la probabilidad P(Lluvioso=True|Paraguas=True)
configuracion_inversa = {"Paraguas": True, "Lluvioso": True}
probabilidad_conjunta_inversa = calcular_probabilidad_conjunta(red_bayesiana, configuracion_inversa)

# Calcular la probabilidad marginal P(Lluvioso=True)
configuracion_marginal = {"Lluvioso": True}
probabilidad_conjunta_marginal = calcular_probabilidad_conjunta(red_bayesiana, configuracion_marginal)

# Calcular la probabilidad condicional P(Paraguas=True|Lluvioso=True)
probabilidad_condicional = probabilidad_conjunta / probabilidad_conjunta_marginal

# Calcular la probabilidad condicional P(Lluvioso=True|Paraguas=True)
probabilidad_condicional_inversa = probabilidad_conjunta / probabilidad_conjunta_inversa

print("Probabilidad P(Paraguas=True|Lluvioso=True):", probabilidad_condicional)
print("Probabilidad P(Lluvioso=True|Paraguas=True):", probabilidad_condicional_inversa)

