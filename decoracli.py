#!/usr/bin/env python3

import argparse
import decora

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', required=True)
    parser.add_argument('--key', required=True)

    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--on', action='store_true')
    action.add_argument('--off', action='store_true')
    action.add_argument('--dim', type=int)

    args = parser.parse_args()

    switch = decora.decora(args.address, bytes.fromhex(args.key))
    switch.connect()

    if args.on:
        switch.on()
    elif args.off:
        switch.off()
    else:
        switch.set_brightness(args.dim)

if __name__ == '__main__':
    main()
