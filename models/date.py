from datetime import datetime

def nowtostr() -> str:
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")