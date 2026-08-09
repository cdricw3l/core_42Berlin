from abc import ABC, abstractmethod
from typing import Protocol, Any


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataProcessor(ABC):

    _data: dict[int, str]
    _processed_numeric: int
    _processed_text: int
    _processed_log: int
    _remaining_numeric: int
    _remaining_text: int
    _remaining_log: int

    def __init__(self) -> None:
        self._data = {}
        self._processed_numeric = 0
        self._remaining_numeric = 0
        self._processed_text = 0
        self._remaining_text = 0
        self._processed_log = 0
        self._remaining_log = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def set_processed(self, code: str, value: int) -> None:
        match code:
            case 'NUMERIC':
                self._processed_numeric += value
            case 'TEXT':
                self._processed_text += value
            case 'LOG':
                self._processed_log += value

    def set_remaining(self, code: str, value: int) -> None:
        match code:
            case 'NUMERIC':
                self._remaining_numeric += value
            case 'TEXT':
                self._remaining_text += value
            case 'LOG':
                self._remaining_log += value

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception(f"Output error: data processor "
                            f"{self.__class__.__name__} is empty")
        key: int = list(self._data.keys())[0]
        value: str | None = self._data.get(key)
        self._data.pop(key)
        if value is None:
            raise Exception("output error value is None")
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
                self._data.update({self._processed_numeric: str(data)})
                self.set_processed('NUMERIC', 1)
                self.set_remaining('NUMERIC', 1)
            case 'float':
                self._data.update({self._processed_numeric: str(data)})
                self.set_processed('NUMERIC', 1)
                self.set_remaining('NUMERIC', 1)

            case 'list':
                # mypy [union-attr]: see documentation
                # -> mypy.readthedocs.io/en/stable/error_code_list.html
                assert isinstance(data, list)
                values: list[int | float] = data
                for value in values:
                    if self.validate(value) is False:
                        raise Exception("Improper numeric data")
                    k: int = self._processed_numeric
                    v: str = str(value)
                    self._data.update({k: v})
                    self.set_processed('NUMERIC', 1)
                    self.set_remaining('NUMERIC', 1)
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
                self._data.update({self._processed_text: str(data)})
                self.set_processed('TEXT', 1)
                self.set_remaining('TEXT', 1)
            case 'list':
                for value in data:
                    if self.validate(value) is False:
                        raise Exception("Improper text data")
                    key: int = self._processed_text
                    self._data.update({key: value})
                    self.set_processed('TEXT', 1)
                    self.set_remaining('TEXT', 1)
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
                self.set_processed('LOG', 1)
                self.set_remaining('LOG', 1)
            case 'list':
                if self.validate(data) is False:
                    raise Exception("Improper log data")
                assert isinstance(data, list)
                for value in data:
                    log_level = value.get('log_level')
                    log_message = value.get('log_message')
                    self._data.update(
                        {self._processed_log: f"{log_level}: {log_message}"})
                    self.set_processed('LOG', 1)
                    self.set_remaining('LOG', 1)
            case _:
                raise Exception("Improper log data")


class DataStream:

    __proc: list[DataProcessor]

    def __init__(self) -> None:
        self.__proc = []

    def get_proc(self) -> list[DataProcessor]:
        return self.__proc

    def register_processor(self, proc: DataProcessor) -> None:
        self.__proc.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            proc: DataProcessor | None = None
            for processor in self.__proc:
                if processor.validate(item) is True:
                    proc = processor
            if proc is None:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")
            else:
                proc.ingest(item)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self.__proc) == 0:
            print("No processor found, no data")
        for proc in self.__proc:
            if isinstance(proc, NumericProcessor):
                proc_type: str = 'Numeric'
                total: int = proc._processed_numeric
                remaining: int = proc._remaining_numeric
            if isinstance(proc, TextProcessor):
                proc_type = 'Text'
                total = proc._processed_text
                remaining = proc._remaining_text
            if isinstance(proc, LogProcessor):
                proc_type = 'Log'
                total = proc._processed_log
                remaining = proc._remaining_log
            print(f"{proc_type} Processor: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def consume_data(self, stream: DataProcessor) -> tuple[int, str]:
        try:
            data: tuple[int, str] = stream.output()
            if isinstance(stream, NumericProcessor):
                stream.set_remaining('NUMERIC', -1)
            if isinstance(stream, TextProcessor):
                actual_remaining = stream._remaining_text
                if actual_remaining > 0:
                    stream.set_remaining('TEXT', -1)
            if isinstance(stream, LogProcessor):
                actual_remaining = stream._remaining_log
                if actual_remaining > 0:
                    stream.set_remaining('LOG', -1)
        except Exception as e:
            raise e
        return data

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for item in self.__proc:
            data: list[tuple[int, str]] = []
            for i in range(nb):
                try:
                    data.append(self.consume_data(item))
                except Exception:
                    pass
            plugin.process_output(data)


class Csv_plugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        for i in range(len(data)):
            print(f"{data[i][1]}", end=",") if i < len(data) - 1\
                else print(f"{data[i][1]}", end="")
        print()


class Json_plugin:

    def process_output(self, data: list[tuple[int, str]]) -> None:
        json: dict[str, str] = {}
        print("JSON Output:")
        for i in range(len(data)):
            json.update({f"Item_{data[i][0]}": data[i][1]})
        print(json)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...\n")
    stream: DataStream = DataStream()

    stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    numeric_processor: NumericProcessor = NumericProcessor()
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()

    stream.register_processor(numeric_processor)
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)
    data_batch: list[Any] = ['Hello world',
                             [3.14, -1, 2.71],
                             [{'log_level': 'WARNING',
                               'log_message':
                               'Telnet access! Use ssh instead'},
                              {'log_level': 'INFO',
                               'log_message': 'User wil is connected'}],
                             42, ['Hi', 'five']]
    print(f"Send first batch of data "
          f"on stream: {data_batch}")
    stream.process_stream(data_batch)
    print()
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_pipe: Csv_plugin = Csv_plugin()
    stream.output_pipeline(3, csv_pipe)
    print()
    stream.print_processors_stats()

    data_batch = [21,
                  ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                  [{'log_level': 'ERROR', 'log_message': '500 server crash'},
                   {'log_level': 'NOTICE',
                    'log_message': 'Certificate expires in 10 days'}],
                  [32, 42, 64, 84, 128, 168],
                  'World hello']
    print(f"\nSend another batch of data: {data_batch}\n")
    stream.process_stream(data_batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_pipe: Json_plugin = Json_plugin()
    stream.output_pipeline(5, json_pipe)
    print()
    stream.print_processors_stats()
