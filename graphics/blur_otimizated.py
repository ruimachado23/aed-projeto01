import numpy as np
import matplotlib.pyplot as plt

# Dados
pixeis = np.array([
    1920000, 883600, 1920000, 1920000, 307200, 307200, 262144, 
    262144, 351900, 48174, 90000, 65536
])

# Iterações para o caso otimizado
iteracoes = np.array([
    3840000, 1767200, 3840000, 3840000, 614400, 614400, 524288,
    524288, 703800, 96348, 180000, 131072
])

# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(pixeis, iteracoes, label='Otimizado', color='blue', linewidth=2)
plt.scatter(pixeis, iteracoes, color='blue', linewidth=2)
plt.xlabel('Pixeis')
plt.ylabel('Iterações')
plt.title('Função do Algortimo Melhorado')
plt.legend()
plt.grid(True)
plt.show()