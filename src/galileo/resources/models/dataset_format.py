from enum import Enum


class DatasetFormat(str, Enum):
    CSV = "csv"
    FEATHER = "feather"
    JSON = "json"
    JSONL = "jsonl"

    def __str__(self) -> str:
        return str(self.value)
