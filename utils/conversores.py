from datetime import datetime, timedelta

def str_para_datetime(date_str):
    return datetime.strptime(date_str, "%d/%m/%Y")


def seconds_para_tempo(seconds):
    td = timedelta(seconds=seconds * 2)
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if td.days > 0:
        parts.append(f"{td.days} dia{'s' if td.days > 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hora{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minuto{'s' if minutes > 1 else ''}")

    return " e ".join(parts)
