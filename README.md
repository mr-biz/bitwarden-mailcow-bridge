# Bitwarden-Mailcow-Bridge

This project creates a bridge between Bitwarden and Mailcow, allowing you to automatically add new aliases from Bitwarden to your Mailcow server.

## Prerequisites

- A Bitwarden account
- A Mailcow server
- Python 3.x installed

## Installation and Usage

# 1. Install rbw (Unofficial Bitwarden CLI)
```
wget https://github.com/doy/rbw/releases/download/1.12.1/rbw_1.12.1_linux_amd64.tar.gz
tar -xzvf rbw_1.12.1_linux_amd64.tar.gz
sudo mv rbw /usr/local/bin/
sudo mv rbw-agent /usr/local/bin/
sudo chmod +x /usr/local/bin/rbw
rbw --version
rbw config set email your-bitwarden-email@example.com
rbw login
rbw sync
```

# 2. Set Environment Variables
# Create a .env file in the project root directory with the following content:
```
LOG_FILE=path/to/your/log/file.log
CATCHALL_PATTERN=your_catchall_pattern
LAST_CHECK_FILE=path/to/last_check_file
PRIMARY_INBOX=your_primary_inbox@example.com
MAILCOW_API_URL=https://your-mailcow-server.com/api/v1
MAILCOW_API_KEY=your_mailcow_api_key
```

# 3. Set Up Python Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 4. Run the Script
```
python3 addaliases.py
```
