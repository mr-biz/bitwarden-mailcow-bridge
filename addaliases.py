import os
import subprocess
import difflib
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables
LOG_FILE = os.getenv("LOG_FILE")
CATCHALL_PATTERN = os.getenv("CATCHALL_PATTERN")
LAST_CHECK_FILE = os.getenv("LAST_CHECK_FILE")
PRIMARY_INBOX = os.getenv("PRIMARY_INBOX")
MAILCOW_API_URL = os.getenv("MAILCOW_API_URL")
MAILCOW_API_KEY = os.getenv("MAILCOW_API_KEY")

def get_bitwarden_items():
    subprocess.run(["rbw", "unlock"], check=True)
    subprocess.run(["rbw", "sync"], check=True)
    return subprocess.check_output(["rbw", "list", "--fields", "user"]).decode().splitlines()

def get_new_items(current_items):
    if os.path.exists(LAST_CHECK_FILE):
        with open(LAST_CHECK_FILE, "r") as f:
            last_check_items = f.read().splitlines()
    else:
        last_check_items = []

    diff = list(difflib.unified_diff(last_check_items, current_items, n=0))
    return [line[1:] for line in diff if line.startswith('+') and not line.startswith('+++')]

def filter_matching_items(new_items):
    return [item for item in new_items if CATCHALL_PATTERN in item and item != PRIMARY_INBOX]

def add_alias_to_mailcow(alias, goto):
    headers = {
        'X-API-Key': MAILCOW_API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        "address": alias,
        "goto": goto,
        "active": "1",
        "sogo_visible": "1"  # Make alias visible in SOGo
    }
    response = requests.post(f"{MAILCOW_API_URL}/api/v1/add/alias", headers=headers, json=data)
    if response.status_code == 200:
        print(f"Successfully created alias: {alias} -> {goto}")
    else:
        print(f"Failed to create alias {alias}: {response.text}")

def main():
    current_items = get_bitwarden_items()
    new_items = get_new_items(current_items)
    matching_items = filter_matching_items(new_items)

    if matching_items:
        with open(LOG_FILE, "w") as f:
            f.write("\n".join(matching_items))

        for alias in matching_items:
            add_alias_to_mailcow(alias, PRIMARY_INBOX)

    with open(LAST_CHECK_FILE, "w") as f:
        f.write("\n".join(current_items))

if __name__ == "__main__":
    main()
