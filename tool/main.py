import sys

import shell


def main():
    args = sys.argv
    if len(args) > 1:
        config_path = args[1]
        shell.start(config_path)


if __name__ == '__main__':
    main()
