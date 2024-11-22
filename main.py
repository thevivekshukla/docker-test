import time
import sys

count = 10

if len(sys.argv) > 1:
    count = int(sys.argv[1])
    if count <= 0:
        raise ValueError("Argument cannot be 0 or negative")

for i in range(1, count + 1):
    print(f"tick tick {i}")
    time.sleep(1)
