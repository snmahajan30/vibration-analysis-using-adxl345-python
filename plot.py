from scipy import fftpack
import numpy as np
import string
import matplotlib.pyplot as plt

sample_rate = 1030    # Sampling frequency.

def simpleParse(mainString, beginString, endString ):
    #Search for a substring between beginString and endString
    posBeginString = string.find(mainString, beginString) + len(beginString)
    posEndString = string.find(mainString, endString)
    result = mainString[posBeginString:posEndString]
    return result

def extract_int_tag(data_arch, tag):
    #Extracts data from string data_str, delimited by <tag> y </tag> and converts it to integer numbers.
    str_channel = ''
    beginString = '<' + tag + '>'
    endString = '</'+ tag + '>'
    str_parse = simpleParse(data_arch, beginString, endString )
    str_channel = str_parse.split(',')    
    channel = []
    n = len(str_channel)
    for i in range(n):
        channel.append(float(str_channel[i]))
    return channel
	
name_archive = raw_input('File to open: ')
name_archive += ".txt"
print 'Opening file: ' + name_archive
archive = name_archive

# Open file for reading
arch = open(archive, "r")
data_arch = arch.read()

channel_1 = extract_int_tag(data_arch, 'L1')
channel_2 = extract_int_tag(data_arch, 'L2')
channel_3 = extract_int_tag(data_arch, 'L3')

print("Amount of samples in channel 1: %s" %len(channel_1))
print("Amount of samples in channel 2: %s" %len(channel_2))
print("Amount of samples in channel 3: %s" %len(channel_3))

num_data = len(channel_1)
X = range(0, num_data, 1)

# Calculate medium value for each channel.
vdc_channel_1 = 0
vdc_channel_2 = 0
vdc_channel_3 = 0
for indice in X:
    vdc_channel_1 += channel_1[indice]
    vdc_channel_2 += channel_2[indice]
    vdc_channel_3 += channel_3[indice]
vdc_channel_1 = vdc_channel_1 / num_data
vdc_channel_2 = vdc_channel_2 / num_data
vdc_channel_3 = vdc_channel_3 / num_data
print("Vdc Channel 1: {0}, Vdc Channel 2 {1}, Vdc Channel 3 {2}".format(vdc_channel_1, vdc_channel_2, vdc_channel_3))

# Subtract DC offset
for indice in X:
    channel_1[indice] -= vdc_channel_1
    channel_2[indice] -= vdc_channel_2
    channel_3[indice] -= vdc_channel_3

#----------------- Plotting -----------------
stime = sample_rate/1000;
X1 = np.linspace(0, num_data/stime, num=num_data) 
fig1 = plt.figure(num=1, figsize=(10,7))
fig1.suptitle('Sampled signal - Acceleration')

# Figure 1. Sampled signals.

# Channel X
ax = fig1.add_subplot(3,1,1)
ax.plot(X1,channel_1)
ax.set_title("Channel X")
ax.set_xlabel('ms')
ax.set_ylabel('g')
ax.grid()

#Channel Y
ax = fig1.add_subplot(3,1,2)
ax.plot(X1,channel_2)
ax.set_title("Channel Y")
ax.set_xlabel('ms')
ax.set_ylabel('g')
ax.grid()

#Channel Z
ax = fig1.add_subplot(3,1,3)
ax.plot(X1,channel_3)
ax.set_title("Channel Z")
ax.set_xlabel('ms')
ax.set_ylabel('g')
ax.grid()

# Figure 2. FFT from signals.
fig2 = plt.figure(num=2, figsize=(10,7))
fig2.suptitle('FFT spectrum')

#Channel X
channel_fft = []
channel_fft = channel_1

N = len(channel_fft) # length of the signal
T = 1.0 / sample_rate
y = channel_fft
yf = fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

ax = fig2.add_subplot(3,1,1)
ax.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ax.grid()
ax.set_title("Channel X")
ax.set_xlabel('Hz')
ax.set_ylabel('g')

#Channel Y
channel_fft = []
channel_fft = channel_2

N = len(channel_fft) # length of the signal
T = 1.0 / sample_rate
y = channel_fft
yf = fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

ax = fig2.add_subplot(3,1,2)
ax.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ax.grid()
ax.set_title("Channel Y")
ax.set_xlabel('Hz')
ax.set_ylabel('g')

#Channel Z
channel_fft = []
channel_fft = channel_3

N = len(channel_fft) # length of the signal
T = 1.0 / sample_rate
y = channel_fft
yf = fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

ax = fig2.add_subplot(3,1,3)
ax.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ax.grid()
ax.set_title("Channel Z")
ax.set_xlabel('Hz')
ax.set_ylabel('g')

plt.show()
