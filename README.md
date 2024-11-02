**Dependencies:**
pywhatkit: A library to send WhatsApp messages and emails.
pyautogui: Used to automate pressing keys like "Enter".
time: Provides delay functions to control the script's execution timing.


**Usage:**
Set phone_number to the desired recipient’s WhatsApp number in international format (e.g., +61470627048).
Customize the message variable with the message you want to send.

**Functions:**
send_whatsapp_message(): Sends a WhatsApp message instantly using pywhatkit and automates pressing "Enter" using pyautogui.
send_email_notification(): Sends an email notification using pywhatkit.send_mail. This line is optional and commented out by default.

**Error Handling:**
The script includes basic error handling to print any issues encountered during the message or email sending process.
