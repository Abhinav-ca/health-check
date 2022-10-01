#!/usr/bin/env python3
import os
import shutil
import sys
import socket
def check_reboot():
    # return true if computer has a pending reboot
    return os.path.exists("/run/reboot_required")
def check_disk_full(disk, min_gb,min_percent):
    du=shutil.disk_usage(disk)
    percent_free=100*du.free/du.total
    gigabyte_free=du.free/2**30

     #calculating th percent free and gigabyte free wih du func
    if gigabyte_free < min_gb or percent_free < min_percent:

        return True
    return False
def check_root_full():
    return check_disk_full(disk='/',min_gb=2,min_percent=10)

def check_cpu_constraint():
    #return true if CPU is having too mush usage, false otherwise
    return psutil.cpu_percent(1)>75

def check_no_network():
    try:
        socket.gethostbyname('www.google.com')
        return False
    except:
        return True
def main():
    func={check_reboot:"reboot-required",check_root_full:'disk full',check_cpu_constraint:'CPU load is too high!',check_no_network:'no working network'}
    ok=True
    for f in func: 
        if f():
            print(func[f])
            ok=False
    if not ok:
        sys.exit(1)
    print("everything ok!")
if __name__=="__main__":
    main()
    
