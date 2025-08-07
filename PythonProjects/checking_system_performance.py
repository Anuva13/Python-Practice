import shutil as s  # used to check disk space etc
import psutil as p  # used to check CPU health etc

def main():
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR !")
    else:
        print("Everything is OK!")

def check_disk_usage(disk):
    du = s.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = p.cpu_percent(1)
    return usage < 75

def show_disk_usage(disk="/"):
    du = s.disk_usage(disk)
    total = du.total / (1024 ** 3)  # Convert to GB
    used = du.used / (1024 ** 3)
    free = du.free / (1024 ** 3)
    percent_free = du.free / du.total * 100

    print(f"Disk usage for {disk}:")
    print(f"  Total: {total:.2f} GB")
    print(f"  Used : {used:.2f} GB")
    print(f"  Free : {free:.2f} GB")
    print(f"  Free (%): {percent_free:.2f}%\n")
    
def show_cpu_usage():
    usage = p.cpu_percent(interval=1)
    print("CPU Usage:")
    print(f"  Usage: {usage:.2f}%")

if __name__ == "__main__":
    show_disk_usage("/")
    show_cpu_usage()
    main()
