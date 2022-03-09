from datetime import datetime

def nowtostr() -> str:
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")

def strtodate(date, format="%d-%m-%Y %H:%M:%S") -> datetime:
    return datetime.strptime(date, format)