We start by making directory structure.
cronos/
├── cli.py
├── cronos.py
├── test_cronos.py
├── utils.py
├── README.md
├── requirements.txt
└── venv/

First I want to set up basic foundation for testing CLI inputs.

I will use argparse(https://docs.python.org/3/library/argparse.html) to parse input expression.

Now I want to start writing unit test.
Test will validate input string 

I first start by reading the example input and output, and decide the rules of the validation.

input: "The cron string will be passed to your application as a single argument."

~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"

output: "The output should be formatted as a table with the field name taking the first 14 columns and
the times as a space-separated list following it."

minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find

I induce the rules of parsing by refering to example given.

six fields: five time fields (minute, hour, day of
month, month, and day of week) plus a command.

Design decision:
How to parse each field?
each field -> each parse_field -> each values list
or
each field ->universal parse_field -> merged values list

Decided to go with the second approach, reason being the regex rule is unlikely to change.

parsed_fields = {
    "minute": parsed[0],
    "hour": parsed[1],
    "day of month": parsed[2],
    "month": parsed[3],
    "day of week": parsed[4],
    "command": parsed[5],
}

I always need this kind of map in my cronos.py because I want to be feeding in this key value pairs, and get key value pairs out.
The keys will stay same, but values will be updated from expression string to list of int values.

