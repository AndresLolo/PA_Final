# fluent_api.py
from typing import List, Union

class QueryBuilder:
    def __init__(self):
        self.query_parts: List[str] = []

    def select(self, *columns: str) -> 'QueryBuilder':
        cols = ', '.join(columns) if columns else '*'
        self.query_parts.append(f"SELECT {cols}")
        return self

    def from_table(self, table_name: str) -> 'QueryBuilder':
        self.query_parts.append(f"FROM {table_name}")
        return self

    def where(self, condition: str) -> 'QueryBuilder':
        self.query_parts.append(f"WHERE {condition}")
        return self

    def join(self, table_name: str, on_condition: str) -> 'QueryBuilder':
        self.query_parts.append(f"JOIN {table_name} ON {on_condition}")
        return self

    def group_by(self, *columns: str) -> 'QueryBuilder':
        cols = ', '.join(columns)
        self.query_parts.append(f"GROUP BY {cols}")
        return self

    def having(self, condition: str) -> 'QueryBuilder':
        self.query_parts.append(f"HAVING {condition}")
        return self

    def order_by(self, *columns: str) -> 'QueryBuilder':
        cols = ', '.join(columns)
        self.query_parts.append(f"ORDER BY {cols}")
        return self

    def limit(self, count: int) -> 'QueryBuilder':
        self.query_parts.append(f"LIMIT {count}")
        return self

    def build(self) -> str:
        return ' '.join(self.query_parts) + ';'

    def __str__(self) -> str:
        return self.build()
