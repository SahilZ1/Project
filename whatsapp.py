# libraries
import pywhatkit
import pyautogui
import time

# to whom the message is to be sent to
phone_number = "+61470627048"  #phone number
message = "Hey there, this is your Daily Reminder, it is 7pm"  #a message that needs to be sent

#function to send the message
def send_whatsapp_message(phone_number, message):

    """
    Sends a message to the number with a message

    Parameters:
    phone_number (str): Phone number needs to start up with a +
    message (str): The message to be sent to the recipient.

    Example:
    send_whatsapp_message("+61470627048", "Hello! This is a reminder.")
    """

    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message)

        # buffer time to let whatsapp open up
        time.sleep(20)

        #acts as the button "enter"
        pyautogui.press("enter")
        print("Message sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

send_whatsapp_message(phone_number, message)

#extra feature to send email
def send_email_notification(email_address):
    """
    Sends an email notification to the specified email address.

    Parameters:
    email_address (str): The email address to which the notification will be sent.

    Example:
    send_email_notification("example@example.com")
    """
    try:
        pywhatkit.send_mail(email_address)
        print("Email notification sent successfully!")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")

# Uncomment the line below to send an email notification
# send_email_notification("sahil.zagade21@gmail.com")
