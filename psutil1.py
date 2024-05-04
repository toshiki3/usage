import psutil
print(f'CPU :{psutil.cpu_percent(interval=1):5}%')
print(f'Memory:{psutil.virtual_memory().percent:5}%')
