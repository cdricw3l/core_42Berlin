def secure_archive(
        file_name: str,
        action: int = -1,
        content: str = "") -> tuple[bool, str]:
    try:
        match action:
            case 0:
                with open(file_name, 'r') as f:
                    lines: str = f.read()
                response: tuple[bool, str] = (True, lines)
            case 1:
                with open(file_name, 'w') as f:
                    f.write(content)
                response = (True, 'Content successfully written to file')
            case _:
                response = (False, 'Bad action: param 2 must be 0 or 1')
    except Exception as e:
        response = (False, f"{e}")
    return response


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    read_mode: int = 0
    write_mode: int = 1
    print("Using 'secure_archive'to read from a nonexistent file:")
    reponse: tuple[bool, str] = secure_archive('/not/existing/file', read_mode)
    print(reponse)
    print("\nUsing 'secure_archive'to read from an inaccessible file:")
    reponse = secure_archive('/var/log/auth.log', read_mode)
    print(reponse)
    print("\nUsing 'secure_archive'to read from a regular file")
    reponse = secure_archive('ancient_fragment.txt', read_mode)
    print(reponse)
    print("\nUsing 'secure_archive'to write previous content to a new file:")
    reponse = secure_archive("output.txt", write_mode, reponse[1])
    print(reponse)
