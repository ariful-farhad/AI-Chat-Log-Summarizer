from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import os
from pathlib import Path

load_dotenv()

class GeminiSummarizer:
    def __init__(self, model_name="gemini-2.5-flash-preview-04-17", temperature=0.9):
        self.model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        self.parser = JsonOutputParser()

        self.prompt = PromptTemplate(
            template=(
                "Summarize this chat in 1–2 sentences.\n"
                "Example: The user asked mainly about Python and its uses.\n\n"
                "Chat:\n{chat_text}\n\n{format_instruction}"
            ),
            input_variables=["chat_text"],
            partial_variables={"format_instruction": self.parser.get_format_instructions()},
        )

        self.chain = self.prompt | self.model | self.parser

    def summarize_file(self, file_path: str) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Chat log file not found: {file_path}")
        
        chat_text = path.read_text(encoding="utf-8")
        result = self.chain.invoke({"chat_text": chat_text})
        return result
