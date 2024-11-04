from usql_parser import parser

class USQLSyntaxError(Exception):
    pass

def safe_parse(query: str):
    try:
        result = parser.parse(query)
        return result
    except SyntaxError as e:
        raise USQLSyntaxError(f"Query invalida: {e}")
