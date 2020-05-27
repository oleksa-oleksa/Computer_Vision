import numpy as np

def correlation(a, b):
	nom = a * b
	a_2 = np.sum(a**2)
	b_2 = np.sum(b**2)
	dem = np.sqrt(a_2 * b_2)
	return np.sum(nom)/dem


sig1 = np.array([1, 2, -3])
sig2 = np.array([1, 3, -2])
sig3 = np.array([50, -25, 0])
sig4 = sig1 * (-1)

print(correlation(sig1, sig2))
print(correlation(sig1, sig3))
print(correlation(sig1, sig4))
