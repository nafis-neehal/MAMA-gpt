import audio, S2TT, T2ST, gpt_4, urllib.request, webbrowser

class assistant:
    def __init__(self) -> None:
        self.query = ''
        self.response = ''

    def record(self, file_path="sample.wav", sample_rate=44100):
        audio.record_audio(file_path, sample_rate)

    def translate_speech_to_text(self, file_path):
        print("Translating the recorded audio to text...")
        print("Transmitting to SeamlessM4T API")
        result = S2TT.run_inference(file_path)
        self.query = result 

    def get_gpt_4_response(self):
        print("Sending the query to GPT-4")
        response = gpt_4.get_response(self.query)
        self.response = response

    def translate_text_to_speech(self):
        result = T2ST.run_inference(self.response)

        print(result[0])

        url = 'file://' + result[0]
        webbrowser.open(url)

    def add_log_transcript(self, dialogue, speaker, file_path="log.txt"):
        """
        Appends a given dialogue to the log file specified by file_path.
        If the file does not exist, it will be created.

        Parameters:
        - dialogue (str): The dialogue to append to the log file.
        - file_path (str): The path to the log file.
        """
        with open(file_path, "a") as file:
            file.write( speaker + ": " + dialogue + "\n")



     