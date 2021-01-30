from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt


def standard_score(data):
    data = np.array(data)
    return (data - data.mean()) / data.std()


def initalise_data(fn):
    '''
    x = horizontal slice
    y = vertical sclice
    z = time
    '''

    data = loadmat(fn)
    print(data.keys())
    vmag = data['ebm2Mm']

    return vmag[62, 1:62, :500]


def fft_transform(data):
    fig, axs = plt.subplots(2)

    axs[0].set_xlabel('Time ($s$)')
    axs[0].set_ylabel('Amplitude ($Unit$)')
    axs[0].plot(data)

    Y = np.fft.fft(data)
    N = len(Y) / 2 + 1
    X = np.linspace(0, 1. / 2., N, endpoint=True)
    X = np.reciprocal(X)

    axs[1].set_xlabel('Period ($s$)')
    axs[1].set_ylabel('Amplitude ($Unit$)')
    return axs[1].plot(X, 2.0 * np.abs(Y[:N]) / N)


# Read the data, 2d matrix
vmag = initalise_data('bzvtime.mat')

# Generate 1 dmeinsional slices at 10, 20 ,30, 40, 50
y = [standard_score(vmag[(x * 10), :]) for x in range(1, 6)]

plt.figure(1)
plt.imshow(vmag, origin='lower')


plt.figure(2)
fft_transform(y[0])
fft_transform(y[1])
fft_transform(y[2])
fft_transform(y[3])
fft_transform(y[4])
plt.tight_layout()
plt.show()