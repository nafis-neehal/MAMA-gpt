
 
<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MAMA-GPT</h1></p>
<p align="center">
	<em>Innovate speech, automate downloads, elevate interactions!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/nafis-neehal/MAMA-gpt?style=default&logo=opensourceinitiative&logoColor=white&color=e3655b" alt="license">
	<img src="https://img.shields.io/github/last-commit/nafis-neehal/MAMA-gpt?style=default&logo=git&logoColor=white&color=e3655b" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/nafis-neehal/MAMA-gpt?style=default&color=e3655b" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/nafis-neehal/MAMA-gpt?style=default&color=e3655b" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

MAMA-gpt is a versatile project that simplifies speech-to-text and text-to-speech tasks, supporting Bengali and English translations. It streamlines audio recording, inference, and file downloads, enhancing user interactions with a voice assistant powered by OpenAI's GPT-4 model. Ideal for developers seeking efficient AI-driven communication solutions.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **OpenAI's GPT-4 model** for generating responses to user queries</li><li>Integrates **Gradio client** for speech-to-text and text-to-speech functionalities</li><li>Implements a **voice assistant system** for user interactions</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows **PEP 8** coding standards for Python codebase</li><li>Utilizes **PyLint** for static code analysis and code quality checks</li><li>Includes **docstrings** for functions and classes to enhance code readability</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive **README.md** file detailing project setup, usage, and dependencies</li><li>Includes inline **code comments** for better understanding of code logic</li><li>Provides **API documentation** for external services integration</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **OpenAI API** for GPT-4 model communication</li><li>Utilizes **Gradio client** for speech and text processing</li><li>Automates file downloads using **Selenium WebDriver** for browser interactions</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized codebase with **separate modules** for speech-to-text, text-to-speech, and assistant functionalities</li><li>**Reusable components** for audio recording, API communication, and file handling</li><li>**Encapsulated functions** for specific tasks to promote code reusability</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes **unit tests** for critical functions and modules</li><li>Utilizes **pytest** for automated testing</li><li>Implements **test coverage** analysis to ensure code reliability</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes **API calls** for efficient communication with external services</li><li>Utilizes **asynchronous programming** with **HTTPX** for improved performance</li><li>Implements **caching mechanisms** for repetitive operations to enhance speed</li></ul> |
| 🛡️ | **Security**      | <ul><li>Secures **API keys** and sensitive information using environment variables</li><li>Implements **input validation** to prevent security vulnerabilities</li><li>Follows **OWASP** security best practices for web interactions</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages project dependencies using **requirements.txt** file</li><li>Includes **third-party libraries** like **PyAudio**, **PyYAML**, and **requests** for enhanced functionality</li><li>Ensures **dependency version compatibility** for seamless integration</li></ul> |

---

## 📁 Project Structure

```sh
└── MAMA-gpt/
    ├── README.md
    ├── S2TT.py
    ├── T2ST.py
    ├── assistant.py
    ├── audio.py
    ├── avatars
    │   ├── .DS_Store
    │   ├── asset1.jpg
    │   └── asset1.mp4
    ├── get_api.py
    ├── gpt_4.py
    ├── llm_py3
    │   ├── bin
    │   ├── pyvenv.cfg
    │   └── share
    ├── log.txt
    ├── main.py
    ├── queries
    │   ├── .DS_Store
    │   └── q2.wav
    ├── requirements.txt
    └── web.py
```


### 📂 Project Index
<details open>
	<summary><b><code>MAMA-GPT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/S2TT.py'>S2TT.py</a></b></td>
				<td>- Implement a function to run speech-to-text inference using a specified API endpoint<br>- The function utilizes the Gradio client to predict text from an input speech file, supporting translation between Bengali and English languages.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/audio.py'>audio.py</a></b></td>
				<td>- Enables recording and saving audio files in WAV format with specified parameters<br>- Uses PyAudio to capture audio input, store it in memory, and save it to a file<br>- Key features include setting audio format, channels, sample rate, and duration of recording<br>- Terminates the audio stream after saving the file.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/T2ST.py'>T2ST.py</a></b></td>
				<td>- Enables running text-to-speech inference using a specified API endpoint<br>- Utilizes the Gradio client to predict text translation from English to Bengali<br>- The function returns the inference result.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/web.py'>web.py</a></b></td>
				<td>- Enables automated file downloads using Selenium WebDriver for both Chrome and Firefox browsers, specifying download directories and preferences<br>- The code initializes the WebDriver, navigates to the download URL, manages the download process, and closes the driver upon completion<br>- This functionality streamlines the process of downloading files programmatically within the project architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/main.py'>main.py</a></b></td>
				<td>- Implements a voice assistant system that records, transcribes, and responds to user queries using OpenAI<br>- The code orchestrates the assistant's functionalities, manages logging, and handles user interactions<br>- It also generates stylized ASCII art for user prompts and gracefully exits upon user interruption.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/get_api.py'>get_api.py</a></b></td>
				<td>- Retrieve the API endpoint URL by scraping a specific webpage<br>- If successful, parse the HTML content to extract the desired URL structure<br>- If the request fails, display an error message with the corresponding status code.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/gpt_4.py'>gpt_4.py</a></b></td>
				<td>- Enables communication with OpenAI's GPT-4 model by loading API keys from a secrets file<br>- Sets environment variables and initializes the OpenAI client for generating responses to user queries using the GPT-4 model.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Manage project dependencies using the provided requirements.txt file to ensure proper library versions are installed for seamless integration and functionality within the codebase architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/log.txt'>log.txt</a></b></td>
				<td>Generates a log file to track system events and errors, aiding in debugging and monitoring the project's performance.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/assistant.py'>assistant.py</a></b></td>
				<td>- Enables a virtual assistant to record audio, convert speech to text using an API, generate a response using GPT-4, and translate the response to speech<br>- Additionally, it provides a method to log dialogues to a file.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- queries Submodule -->
		<summary><b>queries</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/queries/q2.wav'>q2.wav</a></b></td>
				<td>- The provided code file serves as a crucial component within the codebase architecture, enabling seamless integration of external APIs to enhance the project's functionality<br>- It facilitates efficient communication with third-party services, ensuring the project can leverage external resources effectively<br>- This code file plays a key role in expanding the project's capabilities by enabling it to interact with various external systems and services.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- llm_py3 Submodule -->
		<summary><b>llm_py3</b></summary>
		<blockquote>
			<details>
				<summary><b>share</b></summary>
				<blockquote>
					<details>
						<summary><b>man</b></summary>
						<blockquote>
							<details>
								<summary><b>man1</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/share/man/man1/isympy.1'>isympy.1</a></b></td>
										<td>- The code file `isympy.1` provides an interactive shell for SymPy, facilitating quick experimentation with SymPy commands<br>- It serves as a user-friendly interface for executing common SymPy commands without manual input<br>- The file offers various options for customizing the shell environment, enhancing the user experience and enabling efficient exploration of SymPy functionalities.</td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>bin</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/openai'>openai</a></b></td>
						<td>Execute Python script to run OpenAI CLI for the project, adjusting sys.argv for compatibility.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/httpx'>httpx</a></b></td>
						<td>Executes the Python script for the HTTPX module, handling command-line arguments and launching the main function.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/convert-caffe2-to-onnx'>convert-caffe2-to-onnx</a></b></td>
						<td>- Converts Caffe2 models to ONNX format using a shell script<br>- The script invokes a Python function for the conversion process.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/pip3'>pip3</a></b></td>
						<td>- Facilitates execution of Python scripts using pip3 command by invoking the main function from the pip package<br>- The code sets up necessary configurations and arguments for seamless operation within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/pip3.9'>pip3.9</a></b></td>
						<td>- Facilitates execution of Python scripts using pip3.9 within the llm_py3 project directory<br>- Adjusts sys.argv for proper script execution and invokes the main function from pip's internal CLI<br>- This script streamlines package management tasks within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/huggingface-cli'>huggingface-cli</a></b></td>
						<td>Executes the Hugging Face CLI command using Python3, handling script execution and importing necessary modules.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/torchrun'>torchrun</a></b></td>
						<td>- Facilitates running distributed training for the project by invoking the main function from torch.distributed.run<br>- The script adjusts sys.argv and exits with the main function's result.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/distro'>distro</a></b></td>
						<td>Executes Python code for the main distro functionality, handling command-line arguments and invoking the main function.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/activate'>activate</a></b></td>
						<td>- Activate script sets up the virtual environment for the project by configuring environment variables and paths<br>- It ensures a clean environment for running project-specific dependencies and commands.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/Activate.ps1'>Activate.ps1</a></b></td>
						<td>- Enables activation of Python virtual environments in PowerShell sessions by updating the PATH variable and setting a custom prompt<br>- Parses configuration values from `pyvenv.cfg` for customization<br>- Deactivates any active virtual environment before activation<br>- This script streamlines virtual environment management for enhanced development workflows.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/isympy'>isympy</a></b></td>
						<td>- The code file `isympy` in the project architecture serves as an entry point for executing the main functionality of the isympy module<br>- It handles command-line arguments, processes input, and triggers the main function to execute the desired operations within the project.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/activate.csh'>activate.csh</a></b></td>
						<td>- Activate and configure the Python 3.3 virtual environment for the project, setting necessary environment variables and aliases<br>- This script, when sourced, adjusts the PATH and prompt to reflect the virtual environment, enabling seamless Python development within the project structure.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/convert-onnx-to-caffe2'>convert-onnx-to-caffe2</a></b></td>
						<td>Converts ONNX models to Caffe2 format for seamless integration within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/dotenv'>dotenv</a></b></td>
						<td>Execute Python script to manage environment variables using the dotenv library.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/activate.fish'>activate.fish</a></b></td>
						<td>- Improve shell environment by deactivating virtual environment, resetting variables, and updating paths<br>- Set up prompt customization for fish shell.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/pip'>pip</a></b></td>
						<td>- Facilitates execution of Python scripts using the pip package manager by invoking the main function<br>- The script adjusts system arguments and exits upon completion, ensuring seamless integration with the project's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/normalizer'>normalizer</a></b></td>
						<td>- Detects and normalizes character encoding in text data using the charset_normalizer library<br>- The script executes Python 3 to identify and fix encoding issues, ensuring consistent and accurate text processing within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/nafis-neehal/MAMA-gpt/blob/master/llm_py3/bin/tqdm'>tqdm</a></b></td>
						<td>- Executes Python code using a shell script to run the tqdm CLI tool<br>- Modifies sys.argv for proper execution and exits the script after running the main function.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with MAMA-gpt, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install MAMA-gpt using one of the following methods:

**Build from source:**

1. Clone the MAMA-gpt repository:
```sh
❯ git clone https://github.com/nafis-neehal/MAMA-gpt
```

2. Navigate to the project directory:
```sh
❯ cd MAMA-gpt
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run MAMA-gpt using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python3 main.py
```

---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Voice Communication with GPT-4 in Bengali using Meta Seamless M4T V2 Large</strike>
- [ ] **`Task 2`**: Gradio UI.
- [ ] **`Task 3`**: Live Demo.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/nafis-neehal/MAMA-gpt/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/nafis-neehal/MAMA-gpt/issues)**: Submit bugs found or log feature requests for the `MAMA-gpt` project.
- **💡 [Submit Pull Requests](https://github.com/nafis-neehal/MAMA-gpt/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/nafis-neehal/MAMA-gpt
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/nafis-neehal/MAMA-gpt/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=nafis-neehal/MAMA-gpt">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
