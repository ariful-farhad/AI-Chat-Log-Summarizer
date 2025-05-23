# AI Chat Log Summarizer

## Overview

This project is a Python-based tool designed to analyze and summarize AI chat conversations. It processes plain-text `.txt` chat logs and performs the following tasks:

- Separates user and AI messages
- Counts messages from both sides
- Extracts top keywords using TF-IDF
- Generates concise summaries using Google's Gemini model
- Saves structured outputs in JSON and text formats

## Features

- Individual and combined summary generation
- Keyword extraction and frequency analysis
- Organized output directory for reports

## Folder Structure

```
.
├── chats/                # Input chat files (chat1.txt, chat2.txt, ...)
├── outputs/              # Output folder for summaries and JSON files
├── chat_log_parsing.py   # Module for parsing and analyzing chat logs
├── chat_summary.py       # Module for generating summaries using Gemini
├── main.py               # Entry point script
├── .env                  # Stores API key
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Input Format

Chat logs must follow this format:

```
User: Hello, what is Python?
AI: Python is a programming language.
User: What can I build with it?
AI: You can build websites, data apps, AI systems, and more.
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chat-log-summarizer.git
cd chat-log-summarizer
```

### 2. Set Up the Environment

Ensure Python 3.10 or higher is installed.

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file and add your Gemini API key:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Add Chat Files

Place your `.txt` chat logs inside the `chats/` folder.

### 5. Run the Tool

```bash
python main.py
```

Choose from:

- **Individual Report**: Select a file to generate and view detailed summary
- **Combined Report**: Generate a single summary for all chats

## Output

- `outputs/<chat_name>.json`: Ordered user/AI messages
- `outputs/<chat_name>_summary.txt`: Summary report for the chat
- `outputs/final_summary.txt`: Combined summary of all chats

## Example Output

```
Summary:
- The conversation had 15 exchanges.
- The user asked mainly about Python and its uses.
- Most common keywords: Python, use, data, AI, language.
```
