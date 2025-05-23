# AI Chat Log Summarizer

This project summarizes chat logs using the Gemini language model. It can generate individual summaries for specific chat files or a combined summary of all chat files in the "chats" directory.

## Requirements

- Python 3.6+
- The following Python packages:

  ```
  nltk==3.8.1
  langchain
  langchain-core
  langchain-google-genai
  google-generativeai
  python-dotenv
  numpy
  scikit-learn
  langchain_experimental
  langchain-community
  langgraph
  pydantic
  ```

  You can install these packages using pip:

  ```bash
  pip install -r requirements.txt
  ```

  Additionally, the project requires downloading `punkt` and `stopwords` from `nltk`. This is done by running the `setup.py` file:

  ```bash
  python setup.py
  ```

## Usage

1.  Clone the repository.
2.  Install the required packages using `pip install -r requirements.txt`.
3.  Run `python setup.py` to download the necessary `nltk` data.
4.  Create a `.env` file with your Gemini API key:

    ```
    GEMINI_API_KEY=YOUR_API_KEY
    ```

5.  Place your chat log files (in `.txt` format) in the `chats` directory.
6.  Run `main.py`.
7.  Select an option:
    - 1: Generate individual chat summary
    - 2: Generate combined summary of all chats
8.  The output summaries will be saved in the `outputs` directory.

## Example

Here's an example of how to run the project and generate a combined summary of all chat files:

1.  Open a terminal and navigate to the project directory.
2.  Run `python setup.py`.
3.  Run `python main.py`.
4.  Enter `2` to select the "Generate combined summary of all chats" option.
5.  The final summary will be saved in the `outputs/final_summary.txt` file.

## Sample Output

```
Combined Summary:
- The conversation discusses various topics, including project updates, technical issues, and potential solutions. The team members collaborate to troubleshoot problems and make progress on the project.
- Most common keywords: project, update, issue, solution, team.
```
