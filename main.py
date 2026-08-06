#!/usr/bin/env python3
"""ffodial-python-n4xm."""
import sys,argparse
from utils import timestamp
def main():
    p=argparse.ArgumentParser(description="ffodial-python-n4xm")
    p.add_argument("--version",action="version",version="1.0.0")
    p.add_argument("-v","--verbose",action="store_true")
    a=p.parse_args()
    if a.verbose:print(f"[{timestamp()}] ffodial-python-n4xm v1.0.0")
    print(f"Hello from ffodial-python-n4xm!")
    return 0
if __name__=="__main__":sys.exit(main())
