import re
import sys
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def read_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()
      
def parse_chat(lines):
    user_msgs, ai_msgs = [], []
    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_msgs.append(line[5:].strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line[3:].strip())
    return user_msgs, ai_msgs

def count_messages(user_msgs, ai_msgs):
    return len(user_msgs) + len(ai_msgs), len(user_msgs), len(ai_msgs)

def extract_keywords(messages, top_n=5):
    all_text = ' '.join(messages).lower()
    tokens = word_tokenize(all_text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w.isalnum() and w not in stop_words]
    freq_dist = Counter(filtered_tokens)
    return freq_dist.most_common(top_n)

def generate_summary(total, user_count, ai_count, keywords):
    print("\nSummary:")
    print(f"- Total number of exchanges: {total}")
    print(f"- User messages: {user_count}, AI messages: {ai_count}")
    print("- Most common keywords:", ', '.join(word for word, _ in keywords))
   

def main():
    file_path = "chat.txt"
    lines = read_chat_log(file_path)
    user_msgs, ai_msgs = parse_chat(lines)
    total, user_count, ai_count = count_messages(user_msgs, ai_msgs)
    keywords = extract_keywords(user_msgs + ai_msgs)
    generate_summary(total, user_count, ai_count, keywords)

if __name__ == "__main__":
    main()