"""Utility functions."""

__author__ = "123456789"


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Function reads CSV File."""
    from csv import DictReader
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """The column value is returned."""
    value: list[str] = []
    for row in table:
        value.append(row[column])
    return value


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function coverts table rows into columns."""
    result: dict[str, list[str]] = {}
    keys = table[0].keys()
    for key in keys:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Function gets the first n rows."""
    result: dict[str, list[str]] = {}
    for key in table:
        result[key] = table[key][:rows]
        """n rows results in command."""
    return result


def select(table: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Function selects subset columns"""
    result: dict[str, list[str]] = {}
    for col in cols:
        result[col] = table[col]
    return result


def count(table: list[str]) -> dict[str, int]:
    """Function takes lists and return dict."""
    result: dict[str, int] = {}
    for i in range(len(table)):
        if table[i] in result:
            result[table[i]] += 1
        else:
            result[table[i]] = 1
    return result


def to_list(table: dict[str, list[str]]) -> int:
    """Takes dictionary of type str, list[str] and returns list[str]."""
    result: list = []
    for item in table:
        i = 0
        while i < 502:
            result.append(table[item][i])
            i += 1
    return result


def concat(x: dict[str, list], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat function."""
    new_dict: dict[str, list[str]] = {}
    for item in x:
        new_dict[item] = x[item]
    for item in y:
        if item in new_dict:
            count: int = 0
            while count < len(y[item]):
                new_dict[item].append(y[item][count])
                count += 1
        else:
            new_dict[item] = y[item]
    return new_dict