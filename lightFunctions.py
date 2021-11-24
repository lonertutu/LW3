import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.imread(photoName)
    background = photo[900:1500, 1500:1800].swapaxes(0, 1)
    background = background[:, ::-1, :]
    
    cut = photo[900:1500, 1500:1800].swapaxes(0, 1)
    cut = cut[:, ::-1, :]
    rgb = np.mean(cut, axis=(0))
    
    if photoName == "mercury_white.jpg":
        file = open("mean.txt", "w")
        file.write(str(np.argmax(rgb[:, 0])) + "\n")
        file.write(str(np.argmax(rgb[:, 1])) + "\n")
        file.write(str(np.argmax(rgb[:, 2])))
    luma = 0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2]

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=100)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'w', label='I')
    plt.legend()
    
    plt.imshow(background, origin='lower')
    
    
    plt.savefig(plotName)
    plt.show()
    return luma