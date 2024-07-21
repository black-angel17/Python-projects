import socket
import pyaudio
import wave
import time
# Settings

FORMAT = pyaudio.paInt16 #this is 16 bit signed integer audio smaples
CHANNELS = 1    #set channels mono here
RATE = 44100        #no of samples per second
CHUNK = 1024        #no of audio frames per seconds  or frames per buffer
RECORD_SECONDS = 5    #time for recording
OUTPUT_FILENAME = "output.wav"   #saved file

def get_input():

    # Initialize PyAudio
    audio = pyaudio.PyAudio()  #object  creation to interact with input device

    # Open microphone stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    #this thing captures the input audio stream
    print("Recording started...")
    data =b''

    # Start recording
    #frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        d = stream.read(CHUNK)
        data = data + d

    return data
        #frames.append(data)



    # Stop recording

    #stream.stop_stream()
    #stream.close()
    #audio.terminate()


def play(x):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True)
    stream.write(x)
    print("NOW PLAYING SOUND ON ")
    stream.stop_stream()
    stream.close()
    audio.terminate()



def calling():

    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.77.108', 5000)
    cli_socket.connect(server_address)
    print('Connected to {}:{}'.format(*server_address))
    while True:
        try:
            dat='break'
            data = get_input()
            print(type(data))
            print(data)

            print("sending wait 5 sec")
            cli_socket.sendall(data)
            time.sleep(2)
            print("Two second happen")
            cli_socket.sendall(dat.encode('utf-8'))
            print("print empty data")
            time.sleep(5)
            print("data sended")

        except KeyboardInterrupt:
                print("keyboard interrupt detected")
                break




def receive():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_ip = '192.168.77.106'
    local_port = 5000
    sock.bind((local_ip, local_port))
    sock.listen(1)
    print('Waiting for incoming connection...')
    # Accept an incoming connection
    conn, addr = sock.accept()
    print('Connected to:', addr)
    while True:
        try:
            data = b''
            # Send and receive audio data
            while True:
                # Read audio data from the microphone
                # data = stream.read(CHUNK)
                # Send audio data to the connected peer
                # conn.sendall(data)
                # Receive audio data from the connected peer

                datas = conn.recv(CHUNK)
                data = data + datas
                if not datas:
                    play(data)
                    break

        except KeyboardInterrupt:
            print("keyboard interrupt detected")
            break


while True:
    inp = input("Enter to Call or Receive::::")


    if inp ==  'call':
        calling()
    elif inp == 'rec':
        receive()


