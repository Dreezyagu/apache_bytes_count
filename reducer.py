import sys
byte_size = 0
current_count = 0
count_map = {}
gb_in_bytes = 1024*1024*1024

for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # parse the input we got from mapper.py
    size, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        size = int(size)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    current_count+=1
    size_in_gb = size/gb_in_bytes
    byte_size += size_in_gb


count_cost = current_count*0.001
byte_cost = byte_size*0.08

result_map = {"Total cost": count_cost + byte_cost}

print(result_map)