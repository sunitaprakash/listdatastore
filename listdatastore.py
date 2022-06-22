import os
import time
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data_dir', type=str)
args = parser.parse_args()
dir_list = os.listdir(args.data_dir)
time.sleep(60)
print(dir_list)

print("all the contents of datastore")
contents = list(Path(args.data_dir).iterdir())
print(contents)

print("all the contents of datastore usingos.walk")
for path,dirs,files in os.walk(args.data_dir):
    for filename in files:
        print( os.path.join(path,filename))
