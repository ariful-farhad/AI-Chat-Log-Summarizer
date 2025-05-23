from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pathlib import Path
from pydantic import BaseModel
from typing import List
import os


load_dotenv()

class ChatSummaryOutput(BaseModel):
    summary: str
    keywords: List[str]

class GeminiSummarizer:
    def __init__(self, model_name="gemini-2.5-flash-preview-04-17", temperature=0.9):
        self.model = ChatGoogleGenerativeAI(model=model_name, temperature=temperature)
        self.parser = JsonOutputParser(pydantic_object=ChatSummaryOutput)

        self.prompt = PromptTemplate(
          template=(
              "Summarize this chat in 1 or maximum 2 sentences under the 'summary' field.\n"
              "Then pick 5 most relevent ones, keep the relative order\n\n"
              "Return your response as a JSON object with keys 'summary' and 'keywords'.\n"
              "Chat:\n{chat_text}\n{keywords}\n{format_instruction}"
          ),
          input_variables=["chat_text", "keywords"],
          partial_variables={"format_instruction": self.parser.get_format_instructions()},
        )


        self.chain = self.prompt | self.model | self.parser

    def summarize_file(self, file_path: str, keyWords: list[str]) -> str:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Chat log file not found: {file_path}")
        
        chat_text = path.read_text(encoding="utf-8")
        result = self.chain.invoke({"chat_text": chat_text, "keywords": keyWords})
        return result
      
    def summarize_all_chats_in_folder(self, folder_path: str) -> dict:
        folder = Path(folder_path)
        if not folder.exists() or not folder.is_dir():
            raise NotADirectoryError(f"Folder not found: {folder_path}")

        combined_text = []
        all_keywords = []

        from chat_log_parsing import ChatAnalyzer  
        for file in folder.glob("*.txt"):
            analyzer = ChatAnalyzer(str(file))
            lines = analyzer.read_chat_log()
            analyzer.parse_chat(lines)
            combined_text.extend(lines)
            _, keywords = analyzer.analyze()
            all_keywords.extend([word for word, _ in keywords])

        
        joined_text = '\n'.join(combined_text)

        from collections import Counter
        top_keywords = [word for word, _ in Counter(all_keywords).most_common(10)]

        result = self.chain.invoke({
            "chat_text": joined_text,
            "keywords": top_keywords
        })

        return result
