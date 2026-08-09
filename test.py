# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

def simuler():
    t = np.linspace(0, 1, 500)
    y = np.sin(2 * np.pi * 5 * t)
    plt.plot(t, y)
    plt.show()

if __name__ == '__main__':
    # Le code ne s'exécutera qu'une seule fois ici
    simuler()