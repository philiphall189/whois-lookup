"""WHOIS Lookup — Query WHOIS for a domain and print registrar and expiry if present."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='whois_lookup',
        description='Query WHOIS for a domain and print registrar and expiry if present.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('WHOIS Lookup')
    print('A short WHOIS, not a full dump page.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
