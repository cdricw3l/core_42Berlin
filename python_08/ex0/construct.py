import sys
import site


class Color_line():
    BLACK: str = "\033[90m"
    RED: str = "\033[91m"
    GREEN: str = "\033[92m"
    YELLOW: str = "\033[93m"
    BLUE: str = "\033[94m"
    PURPLE: str = "\033[95m"
    CYAN: str = "\033[96m"
    WHITE: str = "\033[97m"
    RESET: str = "\033[0m"


def interpreter() -> str | None:
    path: str = sys.executable
    python: str = path.split('/')[len(path.split('/')) - 1]
    if python == 'python':
        return f"{sys.executable}{sys.version_info[0]}.{sys.version_info[1]}"
    elif python == "python3":
        return f"{sys.executable}.{sys.version_info[1]}"
    return None


def get_vitual_env() -> str:
    path: str = sys.prefix
    venv: str = path.split("/")[len(path.split("/")) - 1]
    return venv


def python_venv_instruction() -> None:
    italic_name: str = "\x1B[3m<environment name>\x1B[0m"
    print(f"{Color_line.YELLOW}"
          f"python -m venv {italic_name}")
    print(f"{Color_line.YELLOW}source {italic_name}"
          f"{Color_line.YELLOW}/bin/activate # On Unix")
    print(f"{italic_name}{Color_line.YELLOW}"
          f"\\Scripts\\activate # On Windows{Color_line.RESET}\n")


if __name__ == "__main__":
    if sys.base_prefix == sys.prefix:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {interpreter()}")
        print("Virtual Environment: None detected\n")
        print(f"{Color_line.YELLOW}"
              f"WARNING: You're in the global environment")
        print(f"The machines can see "
              f"everything you install.{Color_line.RESET}\n")
        python_venv_instruction()
        print("Then run this program again")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {interpreter()}")
        print(f"Virtual Environment: {get_vitual_env()}")
        print(f"Environment Path: {sys.prefix}\n")
        print(f"{Color_line.GREEN}SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print(f"the global system.{Color_line.RESET}\n")
        print("Package installation path:")
        print(f"{site.getsitepackages()[0]}")
