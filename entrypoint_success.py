#!/usr/bin/env python3

import subprocess
import sys

# Define command as string
cmd = 'ls -ltr'

# Use shell to execute the command and store it in sp variable
sp = subprocess.Popen(cmd,shell=True)

print('subprocess started. now waiting for it to finish...')
# Store the return code in rc variable
#rc=sp.wait()

# Print the content of sp variable
print(f"sp content --> {sp}")

sys.exit(sp.check_returncode())
