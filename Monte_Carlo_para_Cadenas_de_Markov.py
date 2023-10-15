import random

# Transiciones de la cadena de Markov
transitions = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

# Estado inicial
current_state = 'A'

# Número de iteraciones MCMC
num_iterations = 10000

# Inicializa el contador de estados
state_counts = {'A': 0, 'B': 0}

# Realiza el muestreo de Monte Carlo para cadenas de Markov
for _ in range(num_iterations):
    # Realiza una transición según las probabilidades de transición
    next_state = random.choices(list(transitions[current_state].keys()), 
                                weights=list(transitions[current_state].values()))[0]

    # Actualiza el estado actual
    current_state = next_state

    # Registra el estado actual
    state_counts[current_state] += 1

# Calcula las probabilidades estimadas de estar en cada estado
estimated_probabilities = {state: count / num_iterations for state, count in state_counts.items()}

# Imprime las probabilidades estimadas
print("Probabilidad de estar en el estado 'A':", estimated_probabilities['A'])
print("Probabilidad de estar en el estado 'B':", estimated_probabilities['B'])
