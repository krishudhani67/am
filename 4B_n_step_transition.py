
# ---------------------------------------------------------------
# (7) 4B: n-step Transition Probability of a Markov Chain
# ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def validate_transition_matrix(P):
   	
    P = np.array(P, dtype=float)
    if P.ndim != 2 or P.shape[0] != P.shape[1]:
        raise ValueError("Transition matrix must be square (n x n).")
    if not np.allclose(P.sum(axis=1), 1):
        raise ValueError("Each row of the transition matrix must sum to 1.")
    if np.any(P < 0):
        raise ValueError("Transition matrix cannot have negative entries.")
    if np.any(P > 1):
        raise ValueError("Transition matrix cannot have entries greater than 1.")
    return P

def n_step_transition_probability(P, n):
    
    P = validate_transition_matrix(P)
    return np.linalg.matrix_power(P, n)


P = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.6, 0.3],
    [0.4, 0.2, 0.4],
])
state_names = ["Sunny", "Cloudy", "Rainy"]

for n in [1, 2, 5, 10, 20]:
    Pn = n_step_transition_probability(P, n)
    print(n, "steps:\n", Pn.round(4))

max_n = 20
evolution = np.array([n_step_transition_probability(P, n)[0] for n in range(1, max_n + 1)])

plt.figure(figsize=(8, 5))
for i, name in enumerate(state_names):
    plt.plot(range(1, max_n + 1), evolution[:, i], marker="o", label=f"P(Sunny -> {name})")
plt.xlabel("Number of steps (n)")
plt.ylabel("Transition probability")
plt.title("n-step Transition Probability starting from 'Sunny'")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
