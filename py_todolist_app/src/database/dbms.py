import sqlite3
# from sql import db_ops, AbsDatabaseManagementSystem,Validate
# from sql import

# from sql.constants import *
import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.database.validate_sql import Validate

# from src.sql.validate_sql import Validate
# import os

# os.makedirs("/src/sql/validate_sql", exist_ok=True)


class DBMS:
    def __init__(self, db_name: str) -> None:
        """Connects to Database of name provided. if it does not exists create one.

        Args:
            db_name (str): Database name.
        """
        # self.v_sql = Validate()
        self.db_name = db_name

        self.valid_columns = []
        try:
            self.connection = sqlite3.connect(f"{db_name}.db")
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
            print(f"Connection to {db_name}.db successful")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def __execute_query(self, query: str, params=None):
        try:
            print(f"Executing query: {query}")
            self.cursor.execute(query, params if params else ())
            self._commit()
            # return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            self._rollback()
            raise

    # Transactional operations
    def _commit(self):
        self.connection.commit()
        print("Transaction committed")

    def _rollback(self):
        self.connection.rollback()
        print("Transaction rollback")

    def close(self):
        self.cursor.close()
        self.connection.close()
        print(f"Connection to {self.db_name}.db closed")

    # @db_ops
    def create(self, table: str, schema: list[tuple[str, str, list[str]]]):
        """Create database table

        Args:
            table (str): Table name
            schema (list[tuple[str, str, list[str]]]): List of tuple of str and list[str] to hold the column's name, types and constraints.
        """
        table_row = Validate._create(schema)

        sql = ",\n\t".join(table_row)
        query = f"CREATE TABLE IF NOT EXISTS {table} (\n\t{sql}\n)"

        print(f"\nExecuting query: \n{query}")
        self.__execute_query(query)
        # self.cursor.execute(query)
        print(f"Table '{table}' has been created")

    # @db_ops
    def insert(self, table: str, schema: list[tuple[list[str], list[str]]]):
        """_summary_

        Args:
            table (str): _description_
            columns (list[str]): _description_
            values (list[str]): _description_
        """
        print("Validating schema...")
        columns, values = Validate()._insert(schema)
        stripped_columns = [_.strip() for _ in columns]
        stripped_values = [_.strip() for _ in values]

        col = ", ".join(stripped_columns)
        val = ", ".join("?" * len(stripped_values))
        query = f"INSERT INTO {table} ({col}) VALUES ({val})"

        print(f"\nExecuting query: \n{query}")
        self.__execute_query(query, values)
        # self.cursor.execute(query, values)
        print(f"Values: '{', '.join(values)}' inserted into table '{table}'")

    # Todo
    # stopped here
    def fetch(
        self,
        table: str,
        columns: list[str] | None = None,
        filter: list[tuple[list[str], list[str]]] | None = None,
    ):
        """_summary_

        Args:
            table (str): _description_
            columns (list[str] | None, optional): _description_. Defaults to None.
            condition (str | None, optional): _description_. Defaults to None.
            values (list[Any] | None, optional): _description_. Defaults to None.

        Returns:
            list[Any]: _description_
        """
        query = f"SELECT * FROM {table}"

        if columns:
            self.__validate_fetch_column(columns, self.valid_columns)
            column = ", ".join(columns)
            query = f"SELECT {column} FROM {table}"

        vals = []
        if filter:
            conditions, values = self.__validate_fetch(filter)
            # _ = ", ".join(conditions)
            # query += " " + f"{_}"
            _ = " AND ".join(conditions)
            query += " " + f"WHERE {_}"
            vals.extend(values)
        try:
            print(f"\nExecuting query: \n{query}")
            self.cursor.execute(query, vals if vals else ())
            print(f"Values '{','.join(vals)}'")
            self._rollback()
        except Exception as e:
            print(f"Unexpected Error: {e}")
            self._rollback()

        return self.cursor.fetchall()

    def __validate_fetch(self, filter: list[tuple[list[str], list[str]]]):
        col = [""]
        val = [""]

        if len(filter) != 1:
            msg = f"Multiple values in '{filter}', please provide one condition clause and its corresponding values Both in the forms of list."
            raise ValueError(msg)

        for conditions, values in filter:
            placeholder = self.__validate_fetch_filter(values, conditions)

            if len(values) != placeholder:
                _col = ", ".join(conditions)
                _val = ", ".join(values)
                msg = f"The number of placeholder '?' does'nt correspond with the number of values provided. Clause '{_col}', Value '{_val}'."
                raise ValueError(msg)

            col.extend(conditions)
            val.extend(values)

        conditions = [_ for _ in col if _.strip()]
        values = [_ for _ in val if _.strip()]

        return conditions, values

    @staticmethod
    def __validate_fetch_filter(values: list[str], conditions: list[str]):
        placeholder = 0
        for value in values:
            if not isinstance(value, str):
                _ = ", ".join(values)
                msg = f"Condition values '{_}' must be in string form"
                raise ValueError(msg)

            if (not value) or (not value.strip()):
                _ = values.index(value)
                msg = f"condition at index '{_}' cannot be empty"
                raise ValueError(msg)

        for condition in conditions:
            if not isinstance(condition, str):
                msg = f"Condition clause '{condition}' must be in string form"
                raise ValueError(msg)

            if (not condition) or (not condition.strip()):
                _ = conditions.index(condition)
                msg = f"condition at index '{_}' cannot be empty"
                raise ValueError(msg)

            if "?" not in condition:
                msg = f"Placeholder '?' is missing in your condition clause: '{condition}'"
                raise ValueError(msg)

            placeholder += condition.count("?")
        return placeholder

    @staticmethod
    def __validate_fetch_column(columns: list[str], column_names: list[str]):
        for col in columns:
            if not isinstance(col, str):
                msg = f"'{col}' must be a string."
                raise ValueError(msg)
            if (not col) or (not col.strip()):
                msg = "Cannot be empty"
                raise ValueError(msg)
            if not col.isupper():
                msg = f"'{col}' must be in all caps"
                raise ValueError(msg)
            if col not in column_names:
                msg = f"'{col}' is not a valid column"
                raise ValueError(msg)

    def update(
        self,
        table_name: str,
        column_to_change: str | list[str],
        condition: str,
        values: list[str],
    ):
        """_summary_

        Args:
            table_name (str): _description_
            column_to_change (str | list[str]): _description_
            condition (str): _description_
            values (tuple[str] | tuple[str, ...]): _description_
        """
        query = f"UPDATE {table_name} SET {column_to_change} WHERE {condition}"
        # self.executing(query, values)

    def drop(self, table: str):
        query = f"DROP TABLE IF EXISTS {table}"
        try:
            self.cursor.execute(query)
            print(f"Table '{table}' dropped successfully")
        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    # schema: list[dict[str, str | list[str]]] = [
    #     {"name": "hi", "type": "integer", "constraint": ["lion"]},
    #     {"name": "hello", "type": "interger", "constraint": ["book"]},
    # ]
    # print(schema)
    # for idx, items in enumerate(schema):
    #     print(f"constraint at index :{idx}::{items.get('constraint')}")
    #     for sub_items in items:
    #         print(f"sub-items:{sub_items}")

    db_name = "Main"
    table = "MASTER"
    db = DBMS(db_name.title())
    # while (user_input := input("Close connection?")) not in ["y", "n"]:
    #     if user_input == "n":
    #         break

    # print("not a valid input")

    # schema = [
    #     ("ID", "INteger", ["primary key", "autoincrement"]),
    #     ("TASKS", "text", ["unique", "NoT null"]),
    #     ("USERS", "text", ["unique"]),
    # ]
    # db.create(table, schema)
    schema = f"PRAGMA table info({table})"
    db._DBMS__execute_query(schema)
    dbs= db.cursor.fetchone()
    print(dbs)
    # for i in dbs:
    #     print(i)
    # # Validate()._Validate__parse_create_param(schema)
    # # valid_sql._create(schema)
    # schema = [(["TASKS"], ["hi ugonna"]), (["users"], ["ggff"])]
    # # valid_sql._parse_insert_param(schema)
    # db.insert(table, schema)
    # column = ["TASKS", "USERS"]
    # schema = [(["ID = ?"], [2])]
    # rows = db.fetch(table, column, schema)
    # for _ in rows:
    #     print(_)

    # db.drop("example")
    db.close()
