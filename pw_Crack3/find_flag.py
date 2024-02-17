import os

pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

for i in pos_pw_list:
    try:
        os.system('echo "{}" | python3 level3.py | grep "pico"'.format(i))
    except:
        pass
