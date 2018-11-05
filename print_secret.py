import os
import sys

print(os.environ['JENKY_SECRET'])

if __name__ == '__main__':
    for a in sys.argv:
        print(a, len(a))
