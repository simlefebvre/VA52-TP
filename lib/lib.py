import numpy as np
import matplotlib.pyplot as plt

def binarize(img : np.ndarray, seuil = 120):
    imgFinal = []
    minLigne = 5
    maxLigne = 27
    minCol = 35
    maxCol = 105

    for num,ligne in enumerate(img):
        lign = [0 if (i < seuil or num < minLigne or num > maxLigne or col < minCol or col > maxCol) else 255 for col,i in enumerate(ligne)]
        imgFinal.append(lign)
    imgFinal = np.array(imgFinal)
    plt.imshow(imgFinal,cmap='gray')
    return imgFinal