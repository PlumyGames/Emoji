import sys

import shell


def main():
    args = sys.argv
    arglen = len(args)
    if arglen == 1:
        print(shell.default_config())
    elif arglen > 1:
        config_path = args[1]
        shell.start(config_path)


if __name__ == '__main__':
    main()
