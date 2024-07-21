
import pyaudio

# Settings

FORMAT = pyaudio.paInt16 #this is 16 bit signed integer audio smaples
CHANNELS = 1    #set channels mono here
RATE = 44100        #no of samples per second
CHUNK = 1024        #no of audio frames per seconds  or frames per buffer
RECORD_SECONDS = 5    #time for recording
OUTPUT_FILENAME = "output.wav"   #saved file



# Initialize PyAudio
audio = pyaudio.PyAudio()  #object interact with the input device

    # Open microphone stream
stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    #this thing captures the input audio stream
print("Recording started...")

   # Start recording
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    d = stream.read(CHUNK)
    frames.append(d)



    # Stop recording

stream.stop_stream()
stream.close()
audio.terminate()




 #Play the recorded audio
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True)
stream.write(b''.join(frames))

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

