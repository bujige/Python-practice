import psutil
print(psutil.cpu_count()) # CPU逻辑数量

print(psutil.cpu_count(logical=False)) # CPU物理核心

print(psutil.cpu_times())