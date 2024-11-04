# test_usql.py
import unittest
from translator import usql_to_sql, sql_to_usql
from ExceptionSQL import safe_parse, USQLSyntaxError
from fluent_api import QueryBuilder

class TestUSQLTranslator(unittest.TestCase):
    def test_traeme_todo(self):
        usql_query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        expected_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_traeme_los_distintos(self):
        usql_query = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        expected_sql = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_mete_en(self):
        usql_query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_actualiza(self):
        usql_query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        expected_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_traeme_mezclando(self):
        usql_query = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        expected_sql = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_traeme_contando(self):
        usql_query = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        expected_sql = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_borra_de_la(self):
        usql_query = "BORRA DE LA tabla clientes DONDE edad ENTRE 18 Y 25;"
        expected_sql = "DELETE FROM tabla clientes WHERE edad BETWEEN 18 AND 25;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_cambia_la_tabla_agrega_columna(self):
        usql_query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        expected_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_cambia_la_tabla_elimina_columna(self):
        usql_query = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        expected_sql = "ALTER TABLE empleados DROP COLUMN direccion;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)
    def test_usql_to_sql(self):
        usql_query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        expected_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)
    def test_usql_to_sql2(self):
        usql_query = "TRAEME nombre, edad DE LA TABLA usuarios DONDE edad > 18;"
        expected_sql = "SELECT nombre, edad FROM usuarios WHERE edad > 18;"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    def test_invalid_usql(self):
        usql_query = "TRAEME DE LA TABLA;"
        with self.assertRaises(USQLSyntaxError):
            safe_parse(usql_query)

    def test_query_with_join(self):
        query = (QueryBuilder()
                .select("pedidos.id", "clientes.nombre")
                .from_table("pedidos")
                .join("clientes", "pedidos.cliente_id = clientes.id")
                .where("clientes.ciudad = 'Barcelona'")
                .build())
        expected_query = ("SELECT pedidos.id, clientes.nombre FROM pedidos "
                        "JOIN clientes ON pedidos.cliente_id = clientes.id "
                        "WHERE clientes.ciudad = 'Barcelona';")
        self.assertEqual(query, expected_query)

    def test_query_with_group_by_and_having(self):
        query = (QueryBuilder()
                .select("COUNT(*)")
                .from_table("ventas")
                .group_by("producto")
                .having("COUNT(*) > 5")
                .build())
        expected_query = ("SELECT COUNT(*) FROM ventas GROUP BY producto "
                        "HAVING COUNT(*) > 5;")
        self.assertEqual(query, expected_query)

    def test_query_with_order_by_and_limit(self):
        query = (QueryBuilder()
                .select("nombre", "edad")
                .from_table("usuarios")
                .order_by("edad DESC")
                .limit(10)
                .build())
        expected_query = ("SELECT nombre, edad FROM usuarios ORDER BY edad DESC LIMIT 10;")
        self.assertEqual(query, expected_query)



    def test_query_with_multiple_filters(self):
        query = (QueryBuilder()
                .select("*")
                .from_table("empleados")
                .where("edad > 30")
                .where("salario > 4000")
                .build())
        expected_query = "SELECT * FROM empleados WHERE edad > 30 WHERE salario > 4000;"
        self.assertEqual(query, expected_query)

    def test_usql_to_sql_with_update(self):
        usql_query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        expected_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        self.assertEqual(usql_to_sql(usql_query), expected_sql)

    """def test_sql_to_usql_with_delete(self):
        sql_query = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        expected_usql = "BORRA DE LA clientes DONDE edad ENTRE 18 AND 25;"
        self.assertEqual(sql_to_usql(sql_query), expected_usql)"""
    
    def test_sql_to_usql_with_alter_table(self):
        sql_query = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        expected_usql = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        self.assertEqual(sql_to_usql(sql_query), expected_usql)

    def test_parser_with_invalid_syntax(self):
        usql_query = "TRAEME SIN_TEXTO;"
        with self.assertRaises(USQLSyntaxError):
            safe_parse(usql_query)



class TestFluentAPI(unittest.TestCase):
    def test_query_building(self):
        query = (QueryBuilder()
                 .select("nombre", "edad")
                 .from_table("usuarios")
                 .where("edad > 18")
                 .build())
        expected_query = "SELECT nombre, edad FROM usuarios WHERE edad > 18;"
        self.assertEqual(query, expected_query)




if __name__ == '__main__':
    unittest.main()
