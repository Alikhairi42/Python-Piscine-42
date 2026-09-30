#!/usr/bin/env python3

from typing import Any
from data_processor import DataProcessor, NumericProcessor ,TextProcessor ,LogProcessor

class DataStream:
    def __init__(self):
        self.procoses: list[Any] = []
        self.stats = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.procoses.append(proc)
        self.stats[proc] = 0
    
    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed = False

            for pr in self.procoses:
                if pr.validate(item):
                    pr.ingest(item)
                    self.stats[pr] += 1
                    processed = True
                    break

            if not processed:
                print(
                    f"DataStream error - Can't process element in stream: {item}"
                )
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.procoses:
            print("No processor found, no data")
            return

        for proc in self.procoses:
            name = type(proc).__name__
            total = self.stats[proc]
            remaining = len(proc.data)

            print(f"{name}: {total} items processed, {remaining} remaining")

if __name__ == "__main__":
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream = DataStream()

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)
    data: list[Any] = [42,"HELLO",{"level": "ERROR"}, 3.13,"WORLD"]
    print(stream.process_stream(data))

    stream.print_processors_stats()