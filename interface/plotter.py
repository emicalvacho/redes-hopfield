import matplotlib.pyplot as plt
import numpy as np

# Graficar patrones asociados
def showPatterns(pw, ph, patterns):
    fig, ax = plt.subplots(1, patterns.shape[0], figsize=(10, 4))
    fig.canvas.set_window_title('Redes de hopfield')
    for i in range(patterns.shape[0]):
        setAxis(pw, ph, patterns[i], str(i), ax[i])
    plt.show()

# Graficar un único patron
def showPattern(pw, ph, pattern, name):
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Redes de hopfield')
    setAxis(pw, ph, pattern, name, ax)
    plt.show()

# Configurar ejes
def setAxis(pw, ph, pattern, name, ax):
    ax.set_title("Patrón " + name)
    ax.matshow(pattern.reshape((pw, ph)), cmap='binary')
    ax.set_xticks(np.arange(0.5,1,1))
    ax.set_yticks(np.arange(0.5,1,1))
    ax.grid()