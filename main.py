import matplotlib.pyplot as plt
import numpy as np

from interface.plotter import showPattern, showPatterns
from operations.hopfield import learn, searchPattern

def main():
    pattern_width = 2
    pattern_height = 2

    # cada vector(patron) representa una matriz cuadrada
    patterns = np.array([[1,1,-1,-1.],
                     [-1,-1,1,1.],], dtype=np.float)
    showPatterns(pattern_width, pattern_height, patterns)

    patternFail = np.array([[-1,-1,-1,1]])
    showPattern(pattern_width, pattern_height, patternFail, "erróneo")

    generalWeightMatrix = learn(pattern_width, pattern_height, patterns)

    patronAsociado = searchPattern(patternFail, generalWeightMatrix)
    showPattern(pattern_width, pattern_height, patronAsociado, "asociado")



if __name__ == "__main__":
    main()