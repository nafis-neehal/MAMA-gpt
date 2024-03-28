import assistant
import time

import warnings


def run(file_path, log_file_path):

    #init
    mojnu = assistant.assistant()

    #record
    mojnu.record(file_path, 44100)

    #Sleep
    time.sleep(5)

    #translate S2TT
    mojnu.translate_speech_to_text(file_path)

    #Print query
    print(mojnu.query)

    #add to log
    mojnu.add_log_transcript(mojnu.query, "User", log_file_path)

    #Send to OpenAI
    mojnu.get_gpt_4_response()

    #Receive and print Answer
    print(mojnu.response)

    #add to log
    mojnu.add_log_transcript(mojnu.response, "Mojnu", log_file_path)

    #Translate T2ST
    mojnu.translate_text_to_speech()

def main():
    # Your code here
    warnings.filterwarnings("ignore")
    
    print("Mojnu welcome's you!")
    print("Please wait for 3 seconds after each response to each query is heard.")
    print("Press Ctrl+C to exit.")
    
    log_file_path = "./log.txt"
    with open(log_file_path, "w") as file:
        pass 

    counter = 1

    try:
        while True:
            file_path = f"./queries/q{counter}.wav"
            run(file_path, log_file_path)
            counter += 1
            time.sleep(15)
    except KeyboardInterrupt:
        print("Program stopped by user.")
        print("Goodbye!")
    

if __name__ == "__main__":
    main()