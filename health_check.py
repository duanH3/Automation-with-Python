#!/usr/bin/env python3
import os
import shutil
import sys
import socket
import psutil
import emails

def check_available_memory():
    """Returns True if memory is not less than 500MB"""
    available = psutil.virtual_memory().available
    memory_use  = available / 1024 ** 2 #convert to MB
    return memory_use > 500

def check_disk_usage():
    """Returns True if disk has at least 20% space"""
    du = shutil.disk_usage("/")
    free = du.free / du.total * 100
    return free < 20

def check_cpu_constrained():
    """Returns True if the cpu is having too much usage, False otherwise."""
    return psutil.cpu_percent(1) > 80

def check_localhost():
    """Returns True if localhost = 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def sent_email(error):
  sender = "automation@example.com"
  receiver = "student-04-9abe0a3a7348@example.com"
  subject = error
  body = "Please check your system and resolve the issue as soon as possible."
  message = emails.generate_email(sender, receiver, subject, body)
  emails.send(message)

def main():
    checks = [
        (check_available_memory, "Error - Available memory is less than 500MB"),
        (check_disk_usage, "Error - Available disk space is less than 20%"),
        (check_cpu_constrained, "Error - CPU usage is over 80%"),
        (check_localhost, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]
    everything_ok = True
    for check, error_msg in checks:
        if check():
            sent_email(error_msg)
            print(error_msg)
            everything_ok = False
            
    if not everything_ok:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)
main()
