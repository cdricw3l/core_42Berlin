from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    _data: dict[int, str]

    def __init__(self) -> None:
        self._data = {}

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception(f"Output error: data processor "
                            f"{self.__class__.__name__} is empty")
        key: int = list(self._data.keys())[0]
        value: str | None = self._data.get(key)
        if value is None:
            raise Exception("output error value is None")
        self._data.pop(key)
        return (key, value)


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'int':
                return True
            case 'float':
                return True
            case 'list':
                for d in data:
                    if type(d) is not int and type(d) is not float:
                        return False
                return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:

        match type(data).__name__:
            case 'int':
                self._data.update({len(self._data): str(data)})
            case 'float':
                self._data.update({len(self._data): str(data)})
            case 'list':
                # mypy [union-attr]: see documentation
                # -> mypy.readthedocs.io/en/stable/error_code_list.html
                assert isinstance(data, list)
                values: list[int | float] = data
                for value in values:
                    if self.validate(value) is False:
                        raise Exception("Improper numeric data")
                    k: int = len(self._data)
                    v: str = str(value)
                    self._data.update({k: v})
            case _:
                raise Exception("Improper numeric data")


class TextProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'str':
                return True
            case 'list':
                for value in data:
                    if type(value) is not str:
                        return False
                return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        match type(data).__name__:
            case 'str':
                self._data.update({len(self._data): str(data)})
            case 'list':
                for value in data:
                    if self.validate(value) is False:
                        raise Exception("Improper text data")
                    key: int = len(self._data)
                    self._data.update({key: value})
            case _:
                raise Exception("Improper text data")


class LogProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        match type(data).__name__:
            case 'dict':
                if 'log_level' not in data or 'log_message' not in data:
                    return False
                if len(data) != 2:
                    return False
                for x in data:
                    if type(x) is not str or type(data.get(x)) is not str:
                        return False
                return True
            case 'list':
                for value in data:
                    if type(value) is not dict:
                        return False
                    if 'log_level' not in value or 'log_message' not in value:
                        return False
                    if len(value) != 2:
                        return False
                    for x in value:
                        if type(x) is not str or type(value.get(x)) is not str:
                            return False
                return True
            case _:
                return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        match  type(data).__name__:
            case 'dict':
                if self.validate(data) is False:
                    raise Exception("Improper log data")
                assert isinstance(data, dict)
                value: dict[str, str] = data

                log_level: str | None = value.get('log_level')
                log_message: str | None = value.get('log_message')
                self._data.update(
                    {len(self._data): f"{log_level}: {log_message}"})
            case 'list':
                if self.validate(data) is False:
                    raise Exception("Improper log data")
                assert isinstance(data, list)
                for value in data:
                    log_level = value.get('log_level')
                    log_message = value.get('log_message')
                    self._data.update(
                        {len(self._data): f"{log_level}: {log_message}"})
            case _:
                raise Exception("Improper log data")


if __name__ == "__main__":

    num: NumericProcessor = NumericProcessor()
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")

    print(f"Trying to validate input '42': {num.validate(42)}")
    print(f"Trying to validate input 'hello': {num.validate('hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        # the comment below disable arg type check for this line
        num.ingest('foo')  # type: ignore[arg-type]
    except Exception as e:
        print(f"Got exception: {e}")

    arr_num: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {arr_num}")
    try:
        num.validate(arr_num)
        num.ingest(arr_num)
        print("Extracting 3 values...")
        for i in range(3):
            data: tuple[int, str] = num.output()
            print(f"Numeric value {data[0]}: {data[1]}")
    except Exception as e:
        print(e)

    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_processor.validate(42)}")

    arr_text: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {arr_text}")
    try:
        text_processor.validate(arr_text)
        text_processor.ingest(arr_text)
        print("Extracting 1 values...")
        for i in range(1):
            data = text_processor.output()
            print(f"Text value {data[0]}: {data[1]}")
    except Exception as e:
        print(e)
    print("\nTesting Log Processor...")

    print(f"Trying to validate input 'Hello': "
          f"{log_processor.validate('Hello')}")
    arr_log: list[dict[str, str]] = [{'log_level': 'NOTICE',
                                      'log_message': 'Connection to server'
                                      },
                                     {'log_level': 'ERROR',
                                      'log_message': 'Unauthorized access!!'
                                      }]
    print(f"Processing data: {arr_log}")
    try:
        log_processor.ingest(arr_log)
        print("Extracting 2 values...")
        for i in range(2):
            data = log_processor.output()
            print(f"Log entry {data[0]}: {data[1]}")
    except Exception as e:
        print(e)
