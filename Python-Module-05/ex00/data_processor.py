# #!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    def __init__(self):
        self.data: list[str] = []
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        element = self.data.pop(0)
        result = (self.counter, element)
        self.counter += 1
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data,(int,float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int,float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Invalid Data")
        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data,str):
            return True
        if isinstance(data,list):
            return all(isinstance(x,str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Invalid data")

        if isinstance(data, list):
            for item in data:
                self.data.append(item)
        else:
            self.data.append(data)

class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and
                all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )

        return False

    def ingest(self, data: dict | list) -> None:
        if not self.validate(data):
            raise Exception("Invalid data")

        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))


if __name__ == "__main__":
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print(numeric.validate(42))
    print(numeric.validate("42"))
    print(numeric.validate([1, 2, 3]))
    print(numeric.validate([1, "hello"]))

    print(text.validate("hello"))
    print(text.validate(["hello", "world"]))
    print(text.validate(["hello", 42]))

    print(log.validate({"level": "ERROR", "message": "Failed"}))
    print(log.validate({"level": "ERROR", "code": 500}))

    try:
        numeric.ingest("invalid")
    except Exception as e:
        print(e)

    numeric.ingest(42)
    numeric.ingest(3.14)
    numeric.ingest([10, 20.5])

    print(numeric.output())
    print(numeric.output())
    print(numeric.output())
    print(numeric.output())