import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



class ChatAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.user_msgs = []
        self.ai_msgs = []

    def read_chat_log(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def parse_chat(self, lines):
        for line in lines:
            line = line.strip()
            if line.startswith("User:"):
                self.user_msgs.append(line[5:].strip())
            elif line.startswith("AI:"):
                self.ai_msgs.append(line[3:].strip())

    def count_messages(self):
        total = len(self.user_msgs) + len(self.ai_msgs)
        return total, len(self.user_msgs), len(self.ai_msgs)

    def extract_keywords(self, top_n=5):
        all_text = ' '.join(self.user_msgs + self.ai_msgs).lower()
        tokens = word_tokenize(all_text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [w for w in tokens if w.isalnum() and w not in stop_words]
        freq_dist = Counter(filtered_tokens)
        return freq_dist.most_common(top_n)

    def analyze(self):
        lines = self.read_chat_log()
        self.parse_chat(lines)
        return self.count_messages(), self.extract_keywords()

    def get_full_text(self):
        return '\n'.join(self.read_chat_log())
