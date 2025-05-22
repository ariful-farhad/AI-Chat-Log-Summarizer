from chat_log_parsing import ChatAnalyzer
from chat_summary import GeminiSummarizer

def main():
    file_path = "chat.txt"
    

    analyzer = ChatAnalyzer(file_path)
    (total, user_count, ai_count), keywords = analyzer.analyze()

    print("\n--- Basic Summary ---")
    print(f"- Total number of exchanges: {total}")
    print(f"- User messages: {user_count}, AI messages: {ai_count}")
    print("- Most common keywords:", ', '.join(word for word, _ in keywords))

    summarizer = GeminiSummarizer()
    summary = summarizer.summarize_file(file_path)

    print("\n--- Gemini AI Summary ---")
    print(summary)

if __name__ == "__main__":
    main()
