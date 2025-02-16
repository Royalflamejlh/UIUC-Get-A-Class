import win32com.client
#other libraries to be used in this script
import os
import re
from datetime import datetime, timedelta
def getEmails():
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")
        
    inbox = mapi.GetDefaultFolder(6)

    messages = inbox.Items

    received_dt = datetime.now() - timedelta(days=14)
    received_dt = received_dt.strftime('%m/%d/%Y %H:%M %p')
    messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
    messages = messages.Restrict("[SenderEmailAddress] = 'techservices-no-reply@illinois.edu'")
    messages = messages.Restrict("[Subject] = 'Section Enrollment Status Update from Course Explorer'")

    for message in list(messages):
        if message.UnRead == True:
            match = re.search('CRN: (\d+)', message.Body)
            if match:
                message.Unread = False
                return(int(match.group(1)))
    return(0)
    