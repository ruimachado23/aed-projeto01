import numpy as np
import matplotlib.pyplot as plt

############################ otimizada ############################
tempo = np.array([
    0.022116,
    0.021905,
    0.022157,
    0.010503,
    0.004536,
    0.004165,
    0.004024,
    0.003486,
    0.003408,
    0.001444,
    0.001315,
    0.001074,
])

pixmem = np.array([
    7680000,
    7680000,
    7680000,
    3534400,
    1407600,
    1228800,
    1228800,
    1048576,
    1048576,
    360000,
    262144,
    192696,
])

############################ não otimizada ############################
tempo1 = np.array([
    10.641445,
    10.613306,
    10.616960,
    4.851716,
    1.906274,
    1.660658,
    1.658858,
    1.413140,
    1.413748,
    0.471385,
    0.339852,
    0.246349,
    ])

pixmem1= np.array([
    3185240400,
    3185240400,
    3185240400,
    1455785200,
    571681500,
    498214800,
    498214800,
    423993616,
    423993616,
    141404400,
    101722384,
    73741836,
    ])


# Plotar os gráficos
plt.figure(figsize=(10, 6))
plt.plot(pixmem, tempo, label='Otimizado', color='blue', linewidth=2)
plt.plot(pixmem1, tempo1, label='Não Otimizado', color='red', linewidth=2)
plt.xlabel('Pixmen')
plt.ylabel('Tempo (s)')
plt.title('Comparação das Funções Otimizada vs Não Otimizada')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Usando escala logarítmica no eixo y
plt.xscale('log')  # Usando escala logarítmica no eixo y

plt.show()
