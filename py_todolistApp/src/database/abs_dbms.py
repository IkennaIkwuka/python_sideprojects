from abc import ABC, abstractmethod


class AbsDatabaseManagementSystem(ABC):
    # @abstractmethod
    # def connecting(self, db_name): ...
    
    @abstractmethod
    def create(self, table: str, schema: list[tuple[str, str, list[str]]]): ...

    @abstractmethod
    def insert(self, table: str, schema: list[tuple[list[str], list[str]]]): ...

    @abstractmethod
    def update(self): ...

    @abstractmethod
    def fetch(self): ...

    @abstractmethod
    def drop(self): ...

    @abstractmethod
    def close(self): ...
