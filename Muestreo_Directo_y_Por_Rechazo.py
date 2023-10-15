import random

# Distribución de probabilidad P(X)
def p_x(x):
    if x == 0:
        return 0.6
    else:
        return 0.4

# Muestreo directo
num_samples = 1000
direct_samples = random.choices([0, 1], [0.6, 0.4], k=num_samples)

# Muestreo por rechazo
rejection_samples = []
for _ in range(num_samples):
    while True:
        x = random.choices([0, 1], [0.6, 0.4])[0]
        u = random.uniform(0, 1)
        if u < p_x(x) / 0.4:  # Rechazar con probabilidad 0.4
            rejection_samples.append(x)
            break

print("Muestreo directo:", direct_samples)
print("Muestreo por rechazo:", rejection_samples)

