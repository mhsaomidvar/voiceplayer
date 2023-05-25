# Import libraries
import sounddevice as sd
import soundfile as sf
import numpy as np

# Extract data and sampling rate from file
array, smp_rt = sf.read("test1.mp3", dtype='float32')

# start the playback
sd.play(array, smp_rt)

# Wait until file is done playing
status = sd.wait()

# stop the sound
sd.stop()