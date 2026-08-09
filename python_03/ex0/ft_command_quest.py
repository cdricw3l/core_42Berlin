import sys
# https://docs.python.org/3/library/sys.html

# way 1
if __name__ == "__main__":
    print("=== Command Quest ===")
    args: list[str] = sys.argv
    print(f"Program name: {args[0]}")
    nb_of_arg: int = len(args)
    if nb_of_arg == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {nb_of_arg - 1}")
        i: int = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {nb_of_arg}\n")

# way 2
# if __name__ == "__main__":
#     print("=== Command Quest ===")
#     args: list[str] = sys.argv
#     print(f"Program name: {args[0]}")
#     nb_of_arg: int = len(args)
#     if nb_of_arg == 1:
#         print("No arguments provided!")
#     else:
#         print(f"Arguments received: {nb_of_arg - 1}")
#         i: int = 1
#         while i < nb_of_arg - 1:
#             print(f"Argument {i}: {args[i]}")
#     print(f"Total arguments: {nb_of_arg}\n")
