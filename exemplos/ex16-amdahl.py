import matplotlib.pyplot as plt

def amdahl(f, p_values):
    result = [(p, 1/((1 - f) + f/p)) for p in p_values]
    return result

f = 0.6
p_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]

speedUps = amdahl(f, p_values)

for p, speedUp in speedUps:
    print(f"{p}\t{speedUp:.3f}")

plt.plot(p_values, [s[1] for s in speedUps], marker = 'o')
plt.xlabel("Número de processadores")
plt.ylabel("SpeedUps")
plt.title(f"SpeedUps vs Processadores para f = {f}")
plt.show()