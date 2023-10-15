# Crear una red bayesiana simple
red_bayesiana = {
    'A': {
        'Padres': [],
        'Cardinalidad': 2,
        'Valores': [0.7, 0.3]
    },
    'B': {
        'Padres': [],
        'Cardinalidad': 2,
        'Valores': [0.8, 0.2]
    },
    'C': {
        'Padres': ['A', 'B'],
        'Cardinalidad': 2,
        'Valores': [0.9, 0.6, 0.7, 0.1, 0.1, 0.4, 0.3, 0.9]
    }
}

# Evidencia para la inferencia
evidencia = {
    'A': 1,
    'B': 0
}

# Realizar inferencia utilizando ponderación de verosimilitud
def weighted_inference(red, variable_objetivo, evidencia):
    probabilidad = 1.0
    for variable, valor in evidencia.items():
        probabilidad *= red[variable]['Valores'][valor]
    variable_padres = [variable for variable in red[variable_objetivo]['Padres']]
    idx = sum([evidencia[variable] * 2 ** variable_padres.index(variable) for variable in variable_padres])
    probabilidad *= red[variable_objetivo]['Valores'][idx]
    return probabilidad

resultado = weighted_inference(red_bayesiana, 'C', evidencia)
print("Resultado de la inferencia:", resultado)
