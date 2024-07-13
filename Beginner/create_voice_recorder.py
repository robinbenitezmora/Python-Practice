import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frequency = 44100
duration = 5

recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=2, dtype='int16')
sd.wait()

write('recording0.wav', frequency, recording)
wv.write('recording1.wav', recording, frequency, sampwidth=2)
