import imaplib

# 1. Configuration
IMAP_SERVER = "imap.gmail.com"  # Use "://office365.com" for Outlook
EMAIL_USER = "your_email@gmail.com"
EMAIL_PASS = "your_app_password"  # Use an App Password, NOT your main password

def check_mail():
    try:
        # 2. Connect and Login
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        
        # 3. Select the inbox
        mail.select("inbox")
        
        # 4. Search for all unread (unseen) emails
        status, response = mail.search(None, 'UNSEEN')
        
        # 5. Process results
        unread_msg_nums = response[0].split()
        count = len(unread_msg_nums)
        
        if count > 0:
            print(f"You have {count} new email(s)!")
        else:
            print("No new emails.")
            
        mail.logout()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_mail()
