#!/usr/bin/env python3

from typing import Any, Protocol
from data_processor import DataProcessor, NumericProcessor
from data_processor import TextProcessor, LogProcessor


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:

    def __init__(self):
        self.procoses: list[DataProcessor] = []
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

            print(
                f"{name}: {total} items processed, "
                f"{remaining} remaining"
            )

    def output_pipeline(
        self, nb: int, plugin: ExportPlugin
    ) -> None:
        output: list[tuple[int, str]] = []

        for proc in self.procoses:
            count = 0

            while count < nb and proc.data:
                output.append(proc.output())
                count += 1

        plugin.process_output(output)


class CSVExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        print("CSV Output:")

        for item in data:
            print(f"{item[0]},{item[1]}")


class JSONExportPlugin:

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        print("JSON Output:")
        print("{")

        for i, item in enumerate(data):
            comma = "," if i < len(data) - 1 else ""
            print(f'  "item_{item[0]}": "{item[1]}"{comma}')

        print("}")


if __name__ == "__main__":
    stream = DataStream()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    data: list[Any] = [
        42,
        "HELLO",
        {"level": "ERROR"},
        3.14,
        "WORLD"
    ]

    stream.process_stream(data)
    stream.print_processors_stats()

    csv_plug = CSVExportPlugin()
    json_plug = JSONExportPlugin()

    stream.output_pipeline(3, csv_plug)
    stream.print_processors_stats()

    new_data: list[Any] = [
        100,
        "PYTHON",
        {"level": "INFO"},
        200.5,
        "PIPELINE"
    ]

    stream.process_stream(new_data)
    stream.print_processors_stats()

    stream.output_pipeline(5, json_plug)
    stream.print_processors_stats()