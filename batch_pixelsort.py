import os

for i in range(1, 32):
    count = str(i).zfill(3)
    os.system(f'python pixelsort.py input/output-{count}.png -o output/output-{count}.png -i 50 -r')
    print(f'finished image-{count}')