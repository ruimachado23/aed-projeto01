import numpy as np
import matplotlib.pyplot as plt

pixeis = np.array([
    1920000, 883600, 1920000, 1920000,  307200, 307200, 262144, 262144, 
    48174, 65536
])
################################## melhor caso ##################################
iteracoes = np.array([
    76801, 35345, 76801, 76801, 12289, 12289, 10405, 10405, 1893, 2602
])

################################## pior caso ##################################
iteracoes1 = np.array([
    3087126, 1310036, 3077747, 3090881, 494680, 492436, 389528, 390070, 109832, 97179
])

################################## cenário médio ##################################
iteracoes2 = (iteracoes1 + iteracoes) / 2


# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(sorted(pixeis), sorted(iteracoes), label='Melhor Caso', color='blue', linewidth=2)
plt.plot(sorted(pixeis), sorted(iteracoes1), label='Pior Caso', color='red', linewidth=2)
plt.plot(sorted(pixeis), sorted(iteracoes2), label='Cenário Médio', color='green', linewidth=2)


plt.xlabel('Pixeis')
plt.ylabel('Iterações')
plt.title('Diferentes Cenários')
plt.legend()
plt.grid(True)
plt.show()
