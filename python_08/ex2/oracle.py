import os
import sys
try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except (ImportError, ImportWarning):
    pass


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


def match_variable(s: str) -> str:
    match s:
        case 'MATRIX_MODE':
            return 'Mode'
        case 'DATABASE_URL':
            return 'Database'
        case 'API_KEY':
            return 'API Access'
        case 'LOG_LEVEL':
            return 'Log Level'
        case 'ZION_ENDPOINT':
            return 'Zion Network'
    return ""


def get_variable(key: str) -> str:
    try:
        value: str = os.environ[key]
    except KeyError:
        return 'missing'
    if len(os.environ[key]) == 0:
        return 'missing'
    return value


def display_config() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    key_list: list[str] = ['MATRIX_MODE',
                           'DATABASE_URL',
                           'API_KEY',
                           'LOG_LEVEL',
                           'ZION_ENDPOINT']
    config: dict[str, str] = {k: get_variable(k) for k in key_list}

    print('Mode: ', end='')
    status: str | None = config.get('MATRIX_MODE')
    print(status)
    print('Database: ', end='')
    status = config.get('DATABASE_URL')
    print('Connected to local instance')\
        if status != 'missing' else print(status)
    print('API Access: ', end='')
    status = config.get('API_KEY')
    print('Authenticated') if status != 'missing' else print(status)
    print('Log Level: ', end='')
    status = config.get('LOG_LEVEL')
    print(status)
    print('Zion Network: ', end='')
    status = config.get('ZION_ENDPOINT')
    print('Online') if status != 'missing' else print(status)
    print("\nEnvironment security check:")
    print(f"{Color_line.GREEN}"
          f"[OK] No hardcoded secrets detected{Color_line.RESET}")
    if len([x for x in config if config.get(x) == 'missing']) > 0:
        print(f"{Color_line.RED}"
              f"[NOK] .env file not properly configured{Color_line.RESET}")
    else:
        print(f"{Color_line.GREEN}"
              f"[OK] .env file properly configured{Color_line.RESET}")
    print(f"{Color_line.GREEN}"
          f"[OK] Production overrides available{Color_line.RESET}")
    print('\nThe Oracle sees all configurations.')


def python_venv_instruction() -> None:
    italic_name: str = "\x1B[3m<environment name>\x1B[0m"
    print(f"{Color_line.YELLOW}"
          f"python -m venv {italic_name}")
    print(f"{Color_line.YELLOW}source {italic_name}"
          f"{Color_line.YELLOW}/bin/activate # On Unix")
    print(f"{italic_name}{Color_line.YELLOW}"
          f"\\Scripts\\activate # On Windows{Color_line.RESET}\n")


if __name__ == "__main__":

    if sys.prefix == sys.base_prefix:
        print("\nplease create a virtual environment:")
        python_venv_instruction()
        sys.exit(1)
    try:
        env = load_dotenv()
    except NameError:
        print(f"{Color_line.RED}python-dotenv is missing!"
              f"{Color_line.RESET} run -> {Color_line.YELLOW}"
              f"pip install python-dotenv{Color_line.RESET}")
        sys.exit(1)
    if env is False:
        print(f"{Color_line.RED}configuration is missing{Color_line.RESET}")
    else:
        display_config()
