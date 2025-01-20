from datetime import datetime


a=1737395666
last_time = (datetime.fromtimestamp(a).strftime('%Y-%m-%d %H:%M:%S'))
print(last_time)