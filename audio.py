#llm_py3/bin/activate
import pyaudio
import wave



def record_audio(file_path, sample_rate):

    # Parameters
    FORMAT = pyaudio.paInt16 # Audio format
    CHANNELS = 1 # Mono audio
    RATE = 44100 # Sample rate
    CHUNK = 1024 # Data chunk size
    RECORD_SECONDS = 8 # Duration of recording
    WAVE_OUTPUT_FILENAME = file_path

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)


    print("Recording...")

    frames = []

    # Record for the set duration
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wave_file:
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))

    print("Audio saved as", WAVE_OUTPUT_FILENAME)
    print("Done")

