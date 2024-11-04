# translator.py
from usql_parser import lexer, parser, USQL_TO_SQL, SQL_TO_USQL
import re

def usql_to_sql(usql_query: str) -> str:
    # Replace 'Y' with 'AND' considering it as a standalone word
    usql_query = re.sub(r'(?<!\w)Y(?!\w)', 'AND', usql_query, flags=re.IGNORECASE)

    sql_query = usql_query
    # Sort keywords by length in descending order to ensure longer keywords are replaced first
    for usql_kw in sorted(USQL_TO_SQL.keys(), key=lambda x: -len(x)):
        # Use word boundaries to match the exact keyword
        pattern = r'\b' + re.escape(usql_kw) + r'\b'
        sql_query = re.sub(pattern, USQL_TO_SQL[usql_kw], sql_query)
    return sql_query

def sql_to_usql(sql_query: str) -> str:
    usql_query = sql_query
    # Sort keywords by length in descending order to ensure longer keywords are replaced first
    for sql_kw in sorted(SQL_TO_USQL.keys(), key=lambda x: -len(x)):
        # Use word boundaries to match the exact keyword
        pattern = r'\b' + re.escape(sql_kw) + r'\b'
        usql_query = re.sub(pattern, SQL_TO_USQL[sql_kw], usql_query)
    return usql_query
