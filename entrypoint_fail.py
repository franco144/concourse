#!/usr/bin/env python3

import subprocess
import sys

# Define command as string
cmd = 'tree'

# Use shell to execute the command and store it in sp variable
sp = subprocess.Popen(cmd,shell=True)

# Store the return code in rc variable
rc=sp.wait()

# Print the content of sp variable
print(sp)

sys.exit(11)
