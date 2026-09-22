import psutil
import time

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=1)

def get_memory_usage() -> float:
    return psutil.virtual_memory().percent

def get_disk_usage() -> float:
    return psutil.disk_usage("/").percent

def get_uptime_seconds() -> float:
    uptime = time.time() - psutil.boot_time()
    return uptime

def get_load_average() -> tuple[float, float, float]:
    return psutil.getloadavg()

def get_system_metrics() -> dict:
    return {
        "cpu": get_cpu_usage(),
        "memory": get_memory_usage(),
        "disk": get_disk_usage(),
        "uptime": get_uptime_seconds(),
        "load_average": get_load_average()
    }

def get_processes() -> list[dict]:
    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "memory_percent", "cmdline"]
    ):
        processes.append(process.info)
    
    return processes

def get_top_memory_processes(processes: list[dict], limit: int = 5) -> list[dict]:
    sorted_processes = sorted(
        processes,
        key=lambda process: process["memory_percent"],
        reverse=True
    )

    return sorted_processes[:limit]
         
processes = get_processes()
print(get_top_memory_processes(processes))
