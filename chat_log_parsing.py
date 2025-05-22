import re
from sklearn.feature_extraction.text import TfidfVectorizer
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

    def extract_keywords(self, top_n=10):
        documents = [' '.join(self.user_msgs + self.ai_msgs)]

        stop_words = list(stopwords.words('english'))  

        vectorizer = TfidfVectorizer(
            stop_words=stop_words,
            lowercase=True,
            token_pattern=r'\b[a-zA-Z]{2,}\b'
        )

        tfidf_matrix = vectorizer.fit_transform(documents)
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]

        tfidf_scores = list(zip(feature_names, scores))
        sorted_keywords = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

        return sorted_keywords[:top_n]

    def analyze(self):
        lines = self.read_chat_log()
        self.parse_chat(lines)
        return self.count_messages(), self.extract_keywords()

    def get_full_text(self):
        return '\n'.join(self.read_chat_log())
