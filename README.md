# Bitwarden-Mailcow-Bridge

This project creates a bridge between Bitwarden and Mailcow, allowing you to automatically add new aliases from Bitwarden to your Mailcow server.

## Bitwarden Mailcow Bridge: Enhanced Email Alias Management

The Bitwarden Mailcow Bridge is a powerful tool designed to streamline email alias management for users running their own Mailcow mail servers. This script addresses the growing trend of using catch-all email addresses while providing a more controlled and secure approach to email alias management.

**Key Features and Benefits:**

- **Selective Alias Management:** Instead of relying on catch-all addresses, this bridge allows you to use only the aliases you've created in Bitwarden, giving you precise control over your email communications.

- **Cost-Effective Solution:** By leveraging your existing Mailcow setup, you can avoid paying subscriptions for anonymous email services, making it an economical choice for privacy-conscious users.

- **Security-Focused Design:** The script is intentionally not designed for headless environments, prioritizing security in its operation.

- **Enhanced Reply Functionality:** After running the script, you'll be able to reply to senders using your aliases directly from Mailcow's SOGo interface.

**IMAP Integration:**

To utilize this functionality with IMAP, you'll need to set up IMAP identities in SOGo:

1. Navigate to Settings -> Mail -> IMAP Accounts
2. Select the pencil icon to edit your existing IMAP account
3. Choose "New Identity" to create the necessary IMAP identities

This bridge offers a tailored solution for users who want granular control over their email aliases while maintaining the benefits of self-hosted email infrastructure.
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

# 2. Clone the Bitwarden-Mailcow Bridge repository to your local machine
```
git clone https://github.com/mr-biz/bitwarden-mailcow-bridge.git
cd bitwarden-mailcow-bridge
```

# 3. Set Environment Variables
# Create a .env file in the project root directory with the following content:
```
LOG_FILE=path/to/your/log/file.log
CATCHALL_PATTERN=@example.com
LAST_CHECK_FILE=path/to/last_check_file
PRIMARY_INBOX=your_primary_inbox@example.com
MAILCOW_API_URL=https://your-mailcow-server.com/api/v1/add/alias
MAILCOW_API_KEY=your_mailcow_api_key
```

# 4. Set Up Python Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# 5. Run the Script
```
python3 addaliases.py
```
