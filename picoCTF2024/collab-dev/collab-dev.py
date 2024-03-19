# Collaborative Development
# https://play.picoctf.org/events/73/challenges/challenge/410?category=5&page=1

import subprocess, re

def run_command(command):
    if isinstance(command, str):
        command = command.split()

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0: return result.stdout
    else: return None

run_command('../GitTools/Extractor/extractor.sh drop-in dumped-folder')
    
output = run_command('find ./dumped-folder -type f -exec cat {} +').splitlines()

clean = lambda x : x.replace('print(','').replace('"','').replace(')','').split(',')

filtered = [clean(x) for x in output if 'print' in x]

print(filtered[1][0]+filtered[-3][0]+filtered[-1][0])