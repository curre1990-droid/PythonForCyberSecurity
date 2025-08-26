#!/usr/bin/python3
# First example of pining from Python
# by Buggsy Mogues
# 08/25/2025

# import necessary Python modules
import platform
import os

# Assign IP to ping to a variable
ip = "127.0.0.1"
# Build our ping command
ping_cmd = f"ping -c 1 -i 2 {ip} > /dev/null 2>&1"
# Execute command and capture exit code
exit_code = os.system(ping_cmd)
#Print results to console
print(exit_code)
