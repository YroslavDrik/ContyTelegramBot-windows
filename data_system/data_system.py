import psutil
import platform
import json

def get_system_data():
    ram_memory = list(psutil.virtual_memory())
    used_ram = round((ram_memory[3] / 1024 ** 3), 1)
    total_ram = round((ram_memory[0] / 1024 ** 3), 1)

    cpu_usage = float(psutil.cpu_percent(interval=1))
    system_name = platform.system()
    disk_usage = []
    disk_list = list(psutil.disk_partitions())
    for disk in disk_list:

        disks = list(psutil.disk_usage(disk.mountpoint))

        name_disk = disk[0]
        used = round((disks[1] / 1024 ** 3),1)
        total = round((disks[0] / 1024 ** 3),1)
        free = round((disks[2] / 1024 ** 3),1)
        disk_usage.append([free, used, total ,name_disk ])
    return system_name, used_ram, total_ram, cpu_usage, disk_usage

def record_data():
    try:
        with open("system_data.json", "r", encoding="utf-8") as file:
            system_data = list(json.load(file))
    except FileNotFoundError:
        with open("system_data.json", "w", encoding="utf-8") as file:
            data = list(get_system_data())
            json.dump(data, file, ensure_ascii=False, indent=4)

    system_data.append(list(get_system_data()))
    with open("system_data.json", "w", encoding="utf-8") as file:
        json.dump(system_data, file, ensure_ascii=False, indent=4)




    return None