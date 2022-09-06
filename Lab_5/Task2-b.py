import numpy as np
import matplotlib.pyplot as plt

#array 1D
data = np.array([1, 2, 3, 4, 5])
print("Original data: ",data)

#discrete fourier transform (fast)
dft = np.fft.fft(data)
print("DFT: ",dft)

#inverse the FT.
result = np.fft.ifft(dft)
print("Inverse result:",result) 
