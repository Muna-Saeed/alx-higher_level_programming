#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{} argument{}:".format(
            num_arguments,
            's' if num_arguments != 1 else ''
        ))

    for i in range(num_arguments):
        print("{}: {}".format(i + 1, arguments[i]))
