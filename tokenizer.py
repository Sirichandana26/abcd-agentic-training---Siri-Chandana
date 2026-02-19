"""
Basic Tokenizer Program
Splits text into tokens (words) and optionally keeps or removes punctuation.
"""

import re


def tokenize(text, keep_punctuation=False):
    """
    Split text into tokens.
    - keep_punctuation=False: returns only words (letters/numbers)
    - keep_punctuation=True: splits on whitespace but keeps punctuation attached
    """
    if keep_punctuation:
        # Split on whitespace only
        return text.split()
    # Split on non-word characters (spaces, punctuation)
    return re.findall(r'\b\w+\b', text.lower())


def main():
    print("=== Basic Tokenizer ===\n")

    # Example text
    sample = "Hello, world! This is a basic tokenizer program. It splits text into tokens."
    print("Sample text:")
    print(f"  {sample}\n")

    # Tokenize (words only)
    tokens = tokenize(sample)
    print("Tokens (words only):")
    print(f"  {tokens}\n")

    # Tokenize (with punctuation as separate)
    tokens_with_punct = tokenize(sample, keep_punctuation=True)
    print("Tokens (with punctuation):")
    print(f"  {tokens_with_punct}\n")

    # Interactive mode: type your own text
    print("--- Type your own text (press Enter to tokenize, empty line to quit) ---")
    while True:
        line = input("> ").strip()
        if not line:
            break
        result = tokenize(line)
        print(f"  Tokens: {result}\n")


if __name__ == "__main__":
    main()
