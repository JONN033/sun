import os
def load_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("tokens.txt not found. Please make sure it exists.")
        return []

def format_tokens(tokens, format_choice):
    formatted_tokens = []
    for token_line in tokens:
        parts = token_line.split(':')
        if len(parts) < 3:
            print(f"Skipping invalid token line: {token_line}")
            continue

        if format_choice == 1:
            formatted_token = f"{parts[0]}:{parts[1]}:{parts[2]}"  # Email:Pass:Token
        elif format_choice == 2:
            formatted_token = f"{parts[2]}:{parts[0]}:{parts[1]}"  # Token:Email:Pass
        elif format_choice == 3:
            formatted_token = f"{parts[1]}:{parts[0]}:{parts[2]}"  # Pass:Email:Token
        elif format_choice == 4:
            formatted_token = f"{parts[0]}:{parts[2]}:{parts[1]}"  # Email:Token:Pass
        else:
            print("Invalid format choice.")
            return []

        # masking
        masked_token = f"{parts[2][:5]}******"  # masking for display
        formatted_tokens.append(f"{masked_token}:{parts[0]}:{parts[1]}")

    return formatted_tokens

def save_tokens(file_path, formatted_tokens):
    with open(file_path, 'w') as file:
        file.write("\n".join(formatted_tokens))
    print("tokens.txt has been overwritten.")

def main():
    file_path = 'assets/tokens.txt'
    tokens = load_tokens(file_path)

    if not tokens:
        return

    print("Select a token format:")
    print("1. Email:Pass:Token (default)")
    print("2. Token:Email:Pass")
    print("3. Pass:Email:Token")
    print("4. Email:Token:Pass")

    try:
        format_choice = int(input("Enter your choice (1-4): ").strip())
    except ValueError:
        print("Invalid input. Defaulting to format 1.")
        format_choice = 1

    formatted_tokens = format_tokens(tokens, format_choice)

    if formatted_tokens:
        print("\nFormatted Tokens:")
        for token in formatted_tokens:
            print(token)

        overwrite = input("\nWould you like to overwrite tokens.txt? (y/n): ").strip().lower()
        if overwrite == 'y':
            save_tokens(file_path, formatted_tokens)
        else:
            print("tokens.txt has not been modified.")
    else:
        print("No valid tokens were formatted.")

if __name__ == "__main__":
    main()
