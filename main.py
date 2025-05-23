from chat_log_parsing import ChatAnalyzer
from chat_summary import GeminiSummarizer
from pathlib import Path


def list_chat_files(chat_dir):
    return sorted([f for f in chat_dir.glob("*.txt")])

def generate_individual_summary(chat_dir, output_dir, summarizer):
    chat_files = list_chat_files(chat_dir)

    print("\nAvailable chat files:")
    for idx, file in enumerate(chat_files):
        print(f"{idx + 1}. {file.name}")

    try:
        choice = int(input("\nEnter the number of the chat file to summarize: ")) - 1
        if not (0 <= choice < len(chat_files)):
            raise ValueError("Invalid selection.")
        file_path = chat_files[choice]
    except ValueError as e:
        print(f"Error: {e}")
        return

    analyzer = ChatAnalyzer(str(file_path))
    (total, user_count, ai_count), keywords = analyzer.analyze()
    analyzer.save_ordered_chat_as_json(output_dir)

    summary = summarizer.summarize_file(str(file_path), keywords)

    # Print to console
    print("\n--- Individual Chat Summary ---")
    print(f"- Total number of exchanges: {total}")
    print(f"- User messages: {user_count}, AI messages: {ai_count}")
    print(f"- Summary: {summary['summary'].strip()}")
    print(f"- Most common keywords: {', '.join(summary['keywords'])}")

    # Save individual summary
    summary_filename = output_dir / f"{file_path.stem}_summary.txt"
    with open(summary_filename, "w", encoding="utf-8") as f:
        f.write("Summary:\n")
        f.write(f"- The conversation had {total} exchanges.\n")
        f.write(f"- {summary['summary'].strip()}\n")
        f.write(f"- Most common keywords: {', '.join(summary['keywords'])}.\n")

def generate_combined_summary(chat_dir, output_dir, summarizer):
    final_result = summarizer.summarize_all_chats_in_folder(str(chat_dir))
    final_summary_path = output_dir / "final_summary.txt"
    with open(final_summary_path, "w", encoding="utf-8") as f:
        f.write("Combined Summary:\n")
        f.write(f"- {final_result['summary'].strip()}\n")
        f.write(f"- Most common keywords: {', '.join(final_result['keywords'])}.\n")
    print("\nFinal summary saved to outputs/final_summary.txt")

def main():
    chat_dir = Path("chats")
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    summarizer = GeminiSummarizer()

    print("Select an option:")
    print("1. Generate individual chat summary")
    print("2. Generate combined summary of all chats")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        generate_individual_summary(chat_dir, output_dir, summarizer)
    elif choice == '2':
        generate_combined_summary(chat_dir, output_dir, summarizer)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
