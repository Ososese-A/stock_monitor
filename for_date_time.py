from datetime import datetime

def hr_6 ():
    now = datetime.now()
    hr6_time = str(now.strftime("%I_%M_%S__%p"))
    return hr6_time

def hr_12 ():
    now = datetime.now()
    hr12_time = str(now.strftime("%H_%M_%S__%p"))
    return hr12_time

def date ():
    now = datetime.now()
    date = now.strftime("%y-%m-%d")
    return date