def spectogram(audio, window_size=500):
    """
    Builds the spectogram of the audio clip. Split the audio clip into buckets of `window_size` and 
    use the discrete fourier transformation to get the intensity of the frequencies.
    The entry at position (i, j) of the matrix is the intensity of the i-th frequencies in the j-th bucket.
    """
    # your code here
    # Split the audio clip into buckets of `window_size`
    total_buckets = np.int(np.size(audio) / window_size)
    
    #buckets = np.array(np.array_split(audio, window_size))
    
    # 'range' object --> indices_or_sections for split()
    split_window = range(window_size, len(audio), window_size)
    buckets = np.array(np.split(audio, split_window))[:-1]
   
    # debug
    print(total_buckets)
    numrows = len(buckets)    
    numcols = len(buckets[0])
    print("Rows {}, columns {}".format(numrows, numcols))

    dft = dft_matrix(window_size)

    # spectrum is matrix: amount of rows is equal to window_size
    # the amount of columns is equal to bucket size
    spectogram = np.zeros((window_size, total_buckets), dtype=complex)
    
    # The entry at position (i, j) of the matrix is the intensity of the i-th frequencies in the j-th bucket
    for j, bucket in enumerate(buckets):
    bucket1 = bucket.transpose()
    spectrum = np.dot(dft, bucket)
    spectogram[:,j] = np.abs(spectrum)

return (np.abs(spectogram*spectogram))[len(spectogram)//2:]
    
    #return np.zeros((window_size // 2, len(audio) // window_size))


def load_wav(url):
    f = urllib2.urlopen(url)
    buffer = BytesIO(f.read())
    sample_rate, audio = scipy.io.wavfile.read(buffer)
    if len(audio.shape) == 2:
        # only select one channel
        audio = audio[:, 0]
    return sample_rate, audio / audio.max()


dolphines_url = "http://www.pmel.noaa.gov/acoustics/whales/sounds/whalewav/akhumphi1x.wav"
# some dolphin sounds
sample_rate, audio = load_wav(dolphines_url)
dolphines_url = "http://www.pmel.noaa.gov/acoustics/whales/sounds/whalewav/akhumphi1x.wav"
# some dolphin sounds
sample_rate, audio = load_wav(dolphines_url)

# listen to the audio
adt.Audio(data=audio, rate=sample_rate)

# plot the values.
plt.plot(audio)
plt.show()

specgram = spectogram(audio, window_size=500)


im_r = plt.imshow(specgram.real)
plt.colorbar(im_r, fraction=0.02, pad=0.04, cmap='jet')
plt.show()

# verify solution with scipy
from scipy import signal
from scipy.fft import fftshift

f, t, Sxx = signal.spectrogram(audio, 500)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()


# https://musicinformationretrieval.com/magnitude_scaling.html

def replaceZeroes(data):
    min_nonzero = np.min(data[np.nonzero(data)])
    data[data == 0] = min_nonzero
    return data

# plot it logarithmically
# Decibels are a relative unit, they express the power of your signal relative to some reference power.
# If you are working with amplitudes, then the formula is:
# power_db = 20 * log10(amp / amp_ref);
specgram = replaceZeroes(specgram) # avoid exception
log = 20*np.log10(specgram.real/np.max(specgram.real))
im = plt.imshow(log)
#im = plt.imshow(log.imag)

plt.colorbar(im, fraction=0.02, pad=0.04)
plt.show()
print(len(log.real))


