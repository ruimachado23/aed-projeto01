import numpy as np
import matplotlib.pyplot as plt

# Dados
pixeis = np.array([
    1920000, 1920000, 1920000, 883600, 351900, 307200, 307200, 262144, 
    262144, 90000, 65536, 48174
])

# Iterações para o caso otimizado
iteracoes = np.array([
    3840000, 3840000, 3840000, 1767200, 703800, 614400, 614400, 524288,
    524288, 180000, 131072, 96348
])

# Iterações para o caso não otimizado
iteracoes1 = np.array([
    3183320400, 3183320400, 3183320400, 1454901600, 571329600, 497907600, 497907600, 423731472,
    423731472,  141314400, 101656848, 73693662
])

# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(pixeis, iteracoes, label='Otimizado', color='blue', linewidth=2)
plt.plot(pixeis, iteracoes1, label='Não Otimizado', color='red', linewidth=2)
plt.xlabel('Pixeis')
plt.ylabel('Iterações')
plt.title('Comparação das Funções Otimizada vs Não Otimizada')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Usando escala logarítmica no eixo y

plt.show()
