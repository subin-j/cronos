import argparse
from cronos import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "expression", type=str, help="Input expression to be parsed to Cronos"
    )
    args = parser.parse_args()
    run_cronos(args.expression)


if __name__ == "__main__":
    main()
