import click
from sys import stdin

@click.command()
@click.option('--filename', default="stdin", help='Name of target file/standard input')
def file_output(filename):
    if filename == "stdin":
        print("".join([f"{idx + 1} {line}" for idx, line in enumerate(stdin)]))
    else:
        with open(filename, 'r') as file:
            content = file.readlines()
            print(''.join([f"{idx + 1} {line}" for idx, line in enumerate(content)]))

if __name__ == "__main__":
    file_output()