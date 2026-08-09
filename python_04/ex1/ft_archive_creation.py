import sys
import typing


if __name__ == "__main__":

    args: list[str] = sys.argv
    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>\n")
    else:
        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{args[1]}'")
            fd: typing.IO[str] = open(args[1])
            print("---\n")
            lines: str = fd.read()
            print(lines)
            fd.close()
            print(f"\n---\nFile '{args[1]}' closed.\n")
            split: list[str] = lines.split('\n')
            transformed_data: str = ""
            for s in split:
                transformed_data = transformed_data + s + '#\n'
            print("Transform_data:\n---\n")
            print(f"{transformed_data}\n---\n")
            new_name: str = input('Enter new file name (or empty):')
            if len(new_name) == 0:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_name}'")
                new_file: typing.IO[str] = open(new_name, 'w')
                new_file.write(transformed_data)
                print(f"Data saved in file '{new_name}'\n")
                new_file.close()
        except (KeyboardInterrupt, EOFError):
            print("\nNot saving data.")
        except (Exception) as e:
            print(f"Error opening file '{args[1]}': {e}\n")
