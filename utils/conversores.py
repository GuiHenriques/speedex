from datetime import datetime

def str_para_datetime(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y")
