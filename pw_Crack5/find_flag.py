import os

with open('dictionary.txt', 'r') as f:
     lines = f.readlines()


pwds = list(map(lambda x: x.replace('\n',''), lines))[::-1]

print(pwds)
# for i in pwds:
#    try:
#      os.system('echo "{}" | python3 level5.py | grep "pico"'.format(i))
#    except:
#      pass

