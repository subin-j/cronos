import argparse

from cronos import parse_cron_expression

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', type=str, help="Input expression to be parsed to Cronos")
    args = parser.parse_args()

    input_expression = args.expression
    parsed = parse_cron_expression(input_expression)
    
    print("Parsed fields:")
    print(parsed)

main()