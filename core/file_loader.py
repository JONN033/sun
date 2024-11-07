import os

def load_file(file_path):
    """Loads a file and returns its content as a list of lines."""
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def load_tokens(file_path='assets/tokens'):
    return load_file(file_path)

def load_webhooks(file_path='assets/webhooks'):
    return load_file(file_path)

def load_emojis(file_path='assets/emojis'):
    return load_file(file_path)

def load_member_ids(file_path='assets/member_ids.'):
    return load_file(file_path)

def load_proxies(file_path='assets/proxies'):
    return load_file(file_path)
