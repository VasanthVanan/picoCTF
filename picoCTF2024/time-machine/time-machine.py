# Time Machine
# https://play.picoctf.org/events/73/challenges/challenge/425?category=5&page=1

import subprocess

def run_command(command):
    if isinstance(command, str):
        command = command.split()

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0: return result.stdout
    else: return None

run_command('../GitTools/Extractor/extractor.sh drop-in dumped-folder')

print(run_command('find ./dumped-folder -type f -exec cat {} +').splitlines()[-2])

