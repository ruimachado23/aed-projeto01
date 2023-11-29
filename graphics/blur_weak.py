import numpy as np
import matplotlib.pyplot as plt

# Dados
pixeis = np.array([
    1920000, 1920000, 1920000, 883600, 351900, 307200, 307200, 262144, 
    262144, 90000, 65536, 48174
])


# Iterações para o caso não otimizado
iteracoes1 = np.array([
    3183320400, 3183320400, 3183320400, 1454901600, 571329600, 497907600, 497907600, 423731472,
    423731472,  141314400, 101656848, 73693662
])

# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(pixeis, iteracoes1, color='red', linewidth=2)
plt.scatter(pixeis, iteracoes1, color='red', linewidth=2)
plt.xlabel('Pixeis')
plt.ylabel('Iterações')
plt.title('Função do Algoritmo Básico')
plt.legend()
plt.grid(True)
plt.show()
