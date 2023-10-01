import random
import time

# List of words for the typing test
word_list = [
    "python",
    "programming",
    "challenge",
    "typing",
    "practice",
    "openai",
    "developer",
    "keyboard",
    "accuracy",
    "speed",
]

# Function to display a random word from the list
def get_random_word():
    return random.choice(word_list)

# Function to calculate typing speed and accuracy
def calculate_results(start_time, end_time, correct_chars, total_chars):
    time_elapsed = end_time - start_time
    typing_speed = (correct_chars / 5) / (time_elapsed / 60)  # Words per minute
    accuracy = (correct_chars / total_chars) * 100
    return typing_speed, accuracy

# Main function to run the typing test
def main():
    print("Welcome to the Typing Test!")

    input("Press Enter to start...")

    num_words = 5  # You can change the number of words to type

    correct_chars = 0
    total_chars = 0

    for _ in range(num_words):
        target_word = get_random_word()
        print(f"Type the word: {target_word}")
        start_time = time.time()
        user_input = input()
        end_time = time.time()

        correct_chars += sum(c1 == c2 for c1, c2 in zip(target_word, user_input))
        total_chars += len(target_word)

    typing_speed, accuracy = calculate_results(start_time, end_time, correct_chars, total_chars)

    print(f"\nTyping Speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
