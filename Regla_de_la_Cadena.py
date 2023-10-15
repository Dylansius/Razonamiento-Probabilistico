# Probabilidad P(A, B, C) = P(A) * P(B | A) * P(C | B)
p_a = 0.4
p_b_given_a = 0.7
p_c_given_b = 0.5

p_a_b_c = p_a * p_b_given_a * p_c_given_b

print("P(A, B, C) =", p_a_b_c)

# Probabilidad condicional P(A | B, C) = P(A, B, C) / P(B, C)
p_b_c = p_b_given_a * p_c_given_b
p_a_given_b_c = p_a_b_c / p_b_c

print("P(A | B, C) =", p_a_given_b_c)

