import os

os.makedirs("/sql", exist_ok=True)

# Constraints


PK = "PRIMARY KEY"
UNIQUE = "UNIQUE"
NOT_NULL = "NOT NULL"
AUTO = "AUTOINCREMENT"
FK = "FOREIGN KEY"
REF = "REFERENCES"
CHK = "CHECK"
DEF = "DEFAULT"

# Datatype
INT = "INTEGER"
TXT = "TEXT"
REAL = "REAL"
BLOB = "BLOB"
NULL = "NULL"


class Validate:
    __constraints = [PK, UNIQUE, NOT_NULL, AUTO, FK, REF, CHK, DEF]
    __datatypes = [INT, TXT, REAL, BLOB, NULL]
    __valid_columns = []

    @classmethod
    def constraints(cls):
        return cls.__constraints

    @classmethod
    def datatypes(cls):
        return cls.__datatypes

    @classmethod
    def _create(cls, schema: list[tuple[str, str, list[str]]]) -> list[str]:
        cls.__validate_create(schema)

        rows = []
        for idx, (columns) in enumerate(schema):
            col_name, col_type, col_constraint = columns
            cls.__valid_columns.append(col_name)

            col_name = col_name.upper()
            col_type = col_type.upper()
            col_constraint = [_.upper() for _ in col_constraint]

            if col_type not in cls.__datatypes:
                msg = f"Invalid type. Column type in tuple of index {idx} is not a valid Sqlite3 datatype. Found: {col_type}"
                suggestion = cls.__type_suggestion(col_type)
                raise ValueError(f"{msg}\n{suggestion}")

            for const_idx, (col_const) in enumerate(col_constraint):
                if not col_const:
                    continue

                if col_const not in cls.__constraints:
                    msg = f"Invalid constraint. Column constraint in tuple of {idx} (sub-index {const_idx}) is not a valid Sqlite3 constraint. Found: {col_const}"
                    suggestion = cls.__constraint_suggestion(col_const)
                    raise ValueError(f"{msg}\n{suggestion}")

            const = " ".join(col_constraint)
            rows.append(
                f"{col_name} {col_type}"
                if not const
                else f"{col_name} {col_type} {const.strip()}"
            )
        return rows

    @staticmethod
    def __validate_create(schema: list[tuple[str, str, list[str]]]):
        if not isinstance(schema, list):
            msg = "Invalid object type. The schema must be a list of tuples."
            raise ValueError(msg)

        # Iterate over each element in the list with its index
        for idx, (columns) in enumerate(schema):
            # Check if each element is a tuple
            if not isinstance(columns, tuple) or len(columns) != 3:
                msg = f"Invalid object type. Column in tuple of {idx} is not a tuple of (name, type, constrains): {columns}"
                raise ValueError(msg)

            col_name, col_type, col_constraint = columns
            if not isinstance(col_name, str) or not col_name:
                msg = f"Invalid object type. Column name in tuple of {idx} must be a string (non-empty)"
                raise ValueError(msg)
            if not isinstance(col_type, str) or not col_type:
                msg = f"Invalid object type. Column type in tuple of {idx} must be a string (non-empty)."
                raise ValueError(msg)
            if not isinstance(col_constraint, list) or not all(
                isinstance(const, str) for const in col_constraint
            ):
                msg = f"Invalid object type. Column constraint in tuple of {idx} must be List of strings."
                raise ValueError(msg)

    @staticmethod
    def __type_suggestion(col_type: str) -> str:
        suggestions = {"I": INT, "R": REAL, "T": TXT, "N": NULL}
        suggestion = suggestions.get(col_type[0])
        return f"Did you mean '{suggestion}'?" if suggestion is not None else ""

    @staticmethod
    def __constraint_suggestion(col_constraint: str) -> str:
        suggestions = {
            "P": PK,
            "U": UNIQUE,
            "N": NOT_NULL,
            "A": AUTO,
            "F": FK,
            "R": REF,
            "C": CHK,
            "D": DEF,
        }
        if col_constraint:
            suggestion = suggestions.get(col_constraint[0])
            return f"Did you mean '{suggestion}'?" if suggestion is not None else ""
        return ""

    @classmethod
    def _insert(
        cls,
        schema: list[tuple[list[str], list[str]]],
    ) -> tuple[list[str], list[str]]:
        cls.__validate_insert(schema)

        columns, values = [], []
        for idx, items in enumerate(schema):
            column, value = items

            for sub_idx, name in enumerate(column):
                name = name.upper()
                if name not in cls.__valid_columns:
                    msg = f"'{name}' at index {idx}, sub-index {sub_idx} is not a valid column name in the table."
                    raise ValueError(msg)

            columns.extend(column)
            values.extend(value)

        return columns, values

    @staticmethod
    def __validate_insert(schema: list[tuple[list[str], list[str]]]):
        # Check if the object is a list
        if not isinstance(schema, list):
            raise ValueError(
                "Invalid object type. The schema must be a list of tuples."
            )

        # Iterate over each element in the list with its index
        for idx, items in enumerate(schema):
            # Check if each element is a tuple
            if not isinstance(items, tuple) or len(items) != 2:
                msg = f"Invalid object type. tuple at index {idx} must be a tuple of two list ([],[]). Found: {items}"
                raise ValueError(msg)

            # Dynamically validate each tuple's elements using index
            for sub_idx, (sub_element) in enumerate(items):
                Validate.__validate_insert_inner_list(idx, sub_idx, sub_element, items)

                # Check if string is empty in list
                for string in sub_element:
                    if not string.strip():
                        msg = f"Missing value. Element in tuple of {idx} in the tuple (sub-index {sub_idx}) cannot be an empty string."
                        raise ValueError(msg)

    @staticmethod
    def __validate_insert_inner_list(
        idx: int, sub_idx: int, sub_element: list, items: tuple[list[str], list[str]]
    ):
        list1, _ = items

        if not isinstance(sub_element, list) or not all(
            isinstance(subitem, str) for subitem in sub_element
        ):
            msg = f"Invalid object type. Element in tuple of {idx} in the tuple (sub-index {sub_idx}) must be a list of strings. Found: {sub_element}"
            raise ValueError(msg)

        # Check if the list is not empty
        if not sub_element:
            msg = f"Missing value. Element in tuple of {idx} in the tuple (sub-index {sub_idx}) cannot be an empty list."
            raise ValueError(msg)
        if len(list1) != 1:
            msg = f"Too many values. Tuple of list with index {idx} (sub-index {sub_idx}) Must have only one value. Found: '{list1}'"
            raise ValueError(msg)
