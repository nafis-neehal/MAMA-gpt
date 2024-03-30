import assistant
import time
import sys
import warnings
warnings.filterwarnings("ignore")


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

def create_boxed_text(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border_line = '+' + '-' * (max_length + 4) + '+'

    boxed_text = [border_line]
    for line in lines:
        # Center align text within the box, considering the padding
        line_text = "| " + line.center(max_length) + "   |"
        boxed_text.append(line_text)
    boxed_text.append(border_line)

    return '\n'.join(boxed_text)

def main():
    # Your code here
    
    
   # To create a more stylized ASCII art with a box around the text, we can manually add borders and padding around the text lines.

    text = """Mojnu welcomes you!
    Please wait for 3 seconds after each response to each query is heard.
    Press Ctrl+C to exit."""

    # Generate the boxed ASCII art
    boxed_text = create_boxed_text(text)
    print(boxed_text)

    log_file_path = "./log.txt"
    with open(log_file_path, "w") as file:
        pass 

    counter = int(sys.argv[1]) if sys.argv[1] else 3

    try:
        while counter:
            file_path = f"./queries/q{counter}.wav"
            run(file_path, log_file_path)
            counter -=1
            time.sleep(15)
    except KeyboardInterrupt:
        print("Program stopped by user.")
        print("Goodbye!")

    text = """
    Thank you for using Mojnu! Goodbye!
    """
    # Generate the boxed ASCII art
    boxed_text = create_boxed_text(text)
    print(boxed_text)
    

if __name__ == "__main__":
    main()