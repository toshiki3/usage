import psutil
print(f'CPU :{psutil.cpu_percent(interval=1):5}%')
