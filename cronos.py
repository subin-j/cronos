import argparse

from cronos import Cronos


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "expression", type=str, help="Input expression to be parsed to Cronos"
    )
    args = parser.parse_args()
    # input_example= "*/15 0 1,15 * 1-5 /usr/bin/find"

    if args:
        input_expr = str(args.expression)
        cronos = Cronos(input_expr)
        cronos.run_cronos()


if __name__ == "__main__":
    main()
