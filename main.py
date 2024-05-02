import sys
import os
import argparse


def invalid_keyword_file():
    print('Invalid keyword file. Read help menu for more')
    sys.exit(1)


def load_keyword_file(key_path: str):
    if len(key_path) > 0 and os.path.isfile(key_path) is False:
        invalid_keyword_file()
    keywords = []
    with open(key_path, 'r+') as keyword_file:
        lines = [line.strip().split(',') for line in keyword_file.readlines()]
        keywords = [keyword.strip() for row in lines for keyword in row if len(keyword) > 1]
    if len(keywords) < 1:
        invalid_keyword_file()
    return keywords


if __name__ == '__main__':
    prog = 'Google Suggestions'
    description = 'This program produces Google auto-complete suggestions of provided keywords'
    parser = argparse.ArgumentParser(prog=prog, description=description)
    parser.add_argument('-k', '--keywords', required=False, nargs='*')
    parser.add_argument('-f', '--filename', required=False, nargs=1)
    parser.add_argument('-o', '--output', required=False, nargs=1)
    args = parser.parse_args()
    keyword_args = args.keywords
    keyword_file_arg = args.filename[0] if args.filename and len(args.filename) > 0 else None
    output_file_arg = args.output[0] if args.output and len(args.output) > 0 else None
    if keyword_args is None and keyword_file_arg is None:
        parser.print_help()
        sys.exit(1)
    print(f'ARGS:\nkeywords: {keyword_args}\nkeyword file: {keyword_file_arg}\noutput file: {output_file_arg}')
