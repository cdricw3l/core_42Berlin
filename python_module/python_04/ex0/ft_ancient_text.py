import sys
import typing

if __name__ == "__main__":

    args: list[str] = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{args[1]}'")
            fd: typing.IO[str] = open(args[1])
            print("---")
            line = fd.read()
            print("")
            print(line)
            print(f"\n---\nFile '{args[1]}' closed.")
            fd.close()
        except Exception as e:
            print(f"Error opening file '{args[1]}': {e}\n")
