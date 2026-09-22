import psutil
import time

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_usage() -> float:
    return psutil.virtual_memory().percent

def get_disk_usage() -> float:
    return psutil.disk_usage("/").percent


def get_system_metrics() -> dict:
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage()
    }

def get_uptime_seconds() -> float:
    pass

print(get_system_metrics())
print(time)