#!/usr/bin/python3

import argparse
import subprocess
from typing import Tuple

def parse():
    parser = argparse.ArgumentParser(
        prog="Find MTU",
        description="Find minum MTU on the path between your local host and destination host")
    parser.add_argument(
        "--dest",
        required=True,
        help="destination host")

    return parser.parse_args()


def log(info: str):
    print(f"\n------------[{info}]------------", flush=True)


def try_ping(destination: str, packet_size: int) -> Tuple[bool, str]:
    try:
        subprocess.check_output(["ping", destination, "-c", "1", "-M", "do", "-s", str(packet_size)], stderr=subprocess.STDOUT)
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, e.output.decode()

def find_mtu(destination: str):
    HEADERS_SIZE = 20 + 8 # IP header + ICMP header

    log(f"CHECK IF CONNECTION EXISTS")
    success, err = try_ping(destination, 0)
    if not success:
        log(f"CONNECTION IS UNAVAILABLE BECAUSE ERROR OCCURED:\n {err}")
        return
    log(f"SUCCESS")
    
    l = 0
    r = 1
    log("FINDING MTU UPPER BOUND")
    while True:
        success = try_ping(destination, r)[0]
        r *= 2
        if success:
            log(f"MTU IS AT LEAST: {r + HEADERS_SIZE}")
        else:
            break
    
    log("FINDING MINUM MTU")
    while r - l > 1:
        m = l + (r - l) // 2

        if try_ping(destination, m)[0]:
            l = m
            log(f"MTU AT LEAST {l + HEADERS_SIZE}")
        else:
            r = m
            log(f"MTU LOWER THAN {r + HEADERS_SIZE}")
    
    log(f"MINUMUM MTU BETWEEN YOUR HOST AND {destination} IS {l + HEADERS_SIZE}")

def main():
    args = parse()
    destination = args.dest

    log(f"FIND MINUM MTU BETWEEN YOUR HOST AND {destination}")

    find_mtu(destination)


if __name__ == "__main__":
    main()
