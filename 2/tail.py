import click
from sys import stdin

@click.command()
@click.argument("filenames", nargs=-1)
def tail(filenames):
    if len(filenames) == 0:
        content = stdin.readlines()
        print("==> stdin <==")
        if len(content) < 18:
            print("".join([f"{line}" for line in content]))
        else:
            content = content[-17:]
            print("".join([f"{line}" for line in content]))
    else:
        for i, filename in enumerate(filenames):
            print(f"==> {filename} <==")
            with open(filename, 'r') as file:
                content = file.readlines()
                if len(content) < 11:
                    print(''.join([f"{line}" for line in content]))
                else:
                    content = content[-10:]
                    print(''.join([f"{line}" for line in content]))
                if i != len(filenames) - 1:
                    print(" ")

if __name__ == "__main__":
    tail()