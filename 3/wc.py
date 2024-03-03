import click
from sys import stdin

@click.command
@click.argument("filenames", nargs=-1)
def wc(filenames):
    if len(filenames) == 0:
        num_words, num_chars = 0, 0
        content = stdin.readlines()
        for line in content:
            num_words += len(line.split())
            num_chars += len(line)
        print(f"\t{len(content)}\t{num_words}\t{num_chars}")
    else:
        total_lines, total_words, total_chars = 0, 0, 0
        for filename in filenames:
            num_lines, num_words, num_chars = 0, 0, 0
            with open(filename, 'r') as file:
                for line in file:
                    num_lines += 1
                    num_words += len(line.split())
                    num_chars += len(line)
            total_lines += num_lines
            total_words += num_words
            total_chars += num_chars
            print(f"\t{num_lines}\t{num_words}\t{num_chars}\t{filename}")
        if len(filenames) > 1:
            print(f"\t{total_lines}\t{total_words}\t{total_chars}\ttotal")

if __name__ == "__main__":
    wc()