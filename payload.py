import os
import sys

os.system("ls -l /data/")

try:
    os.remove("/data/secret_data.txt")
    print("secret removed")
except:
    print("can't remove secret", file=sys.stderr)

os.system("ls -l /data/")
