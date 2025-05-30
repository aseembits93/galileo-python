from enum import Enum


class LogRecordsNumberFilterOperator(str, Enum):
    BETWEEN = "between"
    EQ = "eq"
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    NE = "ne"

    def __str__(self) -> str:
        return str(self.value)
