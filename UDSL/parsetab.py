

_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTUALIZA AGREGA_LA_COLUMNA AGRUPANDO_POR AND BORRA_DE_LA CAMBIA_LA_TABLA CLAVE_PRIMA CLAVE_REFERENTE COMMA COMO_MUCHO CONTANDO CREA_LA_TABLA DE_LA_TABLA DIVIDE DONDE ELIMINA_LA_COLUMNA EN ENTRE EN_ESTO EQUALS ES_NULO EXISTE GREATER GREATEREQUAL IDENTIFIER LESS LESSEQUAL LOS_DISTINTOS LOS_VALORES LPAREN METE_EN MEZCLANDO MINUS NOTEQUAL NO_NULO NUMBER OR ORDENA_POR PARECIDO_A PLUS POR_DEFECTO RPAREN SEMICOLON SETEA STRING TIMES TIRA_LA_TABLA TODO TRAEME TRANSFORMA_A UNICO WHERE_DEL_GROUP_BYstatement_list : statement_list statement\n                      | statementstatement : select_statement SEMICOLON\n                 | insert_statement SEMICOLON\n                 | update_statement SEMICOLON\n                 | delete_statement SEMICOLON\n                 | alter_table_statement SEMICOLONselect_statement : TRAEME select_items DE_LA_TABLA table_name optional_whereselect_items : TODO\n                    | LOS_DISTINTOS IDENTIFIER\n                    | IDENTIFIERtable_name : IDENTIFIERoptional_where : DONDE conditions\n                      | emptyconditions : condition\n                  | conditions logical_operator conditioncondition : IDENTIFIER comparison_operator valuecomparison_operator : EQUALS\n                           | GREATER\n                           | LESS\n                           | GREATEREQUAL\n                           | LESSEQUAL\n                           | NOTEQUALvalue : STRING\n             | NUMBER\n             | IDENTIFIERlogical_operator : AND\n                        | ORinsert_statement : METE_EN table_name LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPARENupdate_statement : ACTUALIZA table_name SETEA assignment_list optional_wheredelete_statement : BORRA_DE_LA table_name optional_wherealter_table_statement : CAMBIA_LA_TABLA table_name alter_actioncolumn_list : column_list COMMA IDENTIFIER\n                   | IDENTIFIERvalue_list : value_list COMMA value\n                  | valueassignment_list : assignment_list COMMA assignment\n                       | assignmentassignment : IDENTIFIER EQUALS valuealter_action : AGREGA_LA_COLUMNA IDENTIFIER data_type constraints\n                    | ELIMINA_LA_COLUMNA IDENTIFIERdata_type : IDENTIFIER LPAREN NUMBER RPAREN\n                 | IDENTIFIERconstraints : constraints constraint\n                   | constraint\n                   | emptyconstraint : NO_NULO\n                  | POR_DEFECTO value\n                  | UNICO\n                  | CLAVE_PRIMA\n                  | CLAVE_REFERENTEempty :'
    
_lr_action_items = {'TRAEME':([0,1,2,13,14,15,16,17,18,],[8,8,-2,-1,-3,-4,-5,-6,-7,]),'METE_EN':([0,1,2,13,14,15,16,17,18,],[9,9,-2,-1,-3,-4,-5,-6,-7,]),'ACTUALIZA':([0,1,2,13,14,15,16,17,18,],[10,10,-2,-1,-3,-4,-5,-6,-7,]),'BORRA_DE_LA':([0,1,2,13,14,15,16,17,18,],[11,11,-2,-1,-3,-4,-5,-6,-7,]),'CAMBIA_LA_TABLA':([0,1,2,13,14,15,16,17,18,],[12,12,-2,-1,-3,-4,-5,-6,-7,]),'$end':([1,2,13,14,15,16,17,18,],[0,-2,-1,-3,-4,-5,-6,-7,]),'SEMICOLON':([3,4,5,6,7,24,26,32,34,35,38,41,42,44,45,48,49,52,65,66,69,70,71,72,73,74,75,77,78,79,80,82,83,84,87,88,91,92,],[14,15,16,17,18,-12,-52,-31,-14,-32,-52,-52,-38,-13,-15,-41,-8,-30,-43,-52,-37,-26,-39,-24,-25,-16,-17,-40,-45,-46,-47,-49,-50,-51,-44,-48,-42,-29,]),'TODO':([8,],[20,]),'LOS_DISTINTOS':([8,],[21,]),'IDENTIFIER':([8,9,10,11,12,21,28,30,31,33,36,37,47,51,53,54,55,56,57,58,59,60,61,62,63,64,81,85,93,],[22,24,24,24,24,29,24,40,43,46,47,48,65,68,43,70,46,-27,-28,70,-18,-19,-20,-21,-22,-23,70,70,70,]),'DE_LA_TABLA':([19,20,22,29,],[28,-9,-11,-10,]),'LPAREN':([23,24,65,67,],[30,-12,76,85,]),'SETEA':([24,25,],[-12,31,]),'DONDE':([24,26,38,41,42,69,70,71,72,73,],[-12,33,33,33,-38,-37,-26,-39,-24,-25,]),'AGREGA_LA_COLUMNA':([24,27,],[-12,36,]),'ELIMINA_LA_COLUMNA':([24,27,],[-12,37,]),'RPAREN':([39,40,68,70,72,73,86,89,90,94,],[50,-34,-33,-26,-24,-25,91,92,-36,-35,]),'COMMA':([39,40,41,42,68,69,70,71,72,73,89,90,94,],[51,-34,53,-38,-33,-37,-26,-39,-24,-25,93,-36,-35,]),'EQUALS':([43,46,],[54,59,]),'AND':([44,45,70,72,73,74,75,],[56,-15,-26,-24,-25,-16,-17,]),'OR':([44,45,70,72,73,74,75,],[57,-15,-26,-24,-25,-16,-17,]),'GREATER':([46,],[60,]),'LESS':([46,],[61,]),'GREATEREQUAL':([46,],[62,]),'LESSEQUAL':([46,],[63,]),'NOTEQUAL':([46,],[64,]),'LOS_VALORES':([50,],[67,]),'STRING':([54,58,59,60,61,62,63,64,81,85,93,],[72,72,-18,-19,-20,-21,-22,-23,72,72,72,]),'NUMBER':([54,58,59,60,61,62,63,64,76,81,85,93,],[73,73,-18,-19,-20,-21,-22,-23,86,73,73,73,]),'NO_NULO':([65,66,70,72,73,77,78,79,80,82,83,84,87,88,91,],[-43,80,-26,-24,-25,80,-45,-46,-47,-49,-50,-51,-44,-48,-42,]),'POR_DEFECTO':([65,66,70,72,73,77,78,79,80,82,83,84,87,88,91,],[-43,81,-26,-24,-25,81,-45,-46,-47,-49,-50,-51,-44,-48,-42,]),'UNICO':([65,66,70,72,73,77,78,79,80,82,83,84,87,88,91,],[-43,82,-26,-24,-25,82,-45,-46,-47,-49,-50,-51,-44,-48,-42,]),'CLAVE_PRIMA':([65,66,70,72,73,77,78,79,80,82,83,84,87,88,91,],[-43,83,-26,-24,-25,83,-45,-46,-47,-49,-50,-51,-44,-48,-42,]),'CLAVE_REFERENTE':([65,66,70,72,73,77,78,79,80,82,83,84,87,88,91,],[-43,84,-26,-24,-25,84,-45,-46,-47,-49,-50,-51,-44,-48,-42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement_list':([0,],[1,]),'statement':([0,1,],[2,13,]),'select_statement':([0,1,],[3,3,]),'insert_statement':([0,1,],[4,4,]),'update_statement':([0,1,],[5,5,]),'delete_statement':([0,1,],[6,6,]),'alter_table_statement':([0,1,],[7,7,]),'select_items':([8,],[19,]),'table_name':([9,10,11,12,28,],[23,25,26,27,38,]),'optional_where':([26,38,41,],[32,49,52,]),'empty':([26,38,41,66,],[34,34,34,79,]),'alter_action':([27,],[35,]),'column_list':([30,],[39,]),'assignment_list':([31,],[41,]),'assignment':([31,53,],[42,69,]),'conditions':([33,],[44,]),'condition':([33,55,],[45,74,]),'logical_operator':([44,],[55,]),'comparison_operator':([46,],[58,]),'data_type':([47,],[66,]),'value':([54,58,81,85,93,],[71,75,88,90,94,]),'constraints':([66,],[77,]),'constraint':([66,77,],[78,87,]),'value_list':([85,],[89,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement_list","S'",1,None,None,None),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','usql_parser.py',146),
  ('statement_list -> statement','statement_list',1,'p_statement_list','usql_parser.py',147),
  ('statement -> select_statement SEMICOLON','statement',2,'p_statement','usql_parser.py',151),
  ('statement -> insert_statement SEMICOLON','statement',2,'p_statement','usql_parser.py',152),
  ('statement -> update_statement SEMICOLON','statement',2,'p_statement','usql_parser.py',153),
  ('statement -> delete_statement SEMICOLON','statement',2,'p_statement','usql_parser.py',154),
  ('statement -> alter_table_statement SEMICOLON','statement',2,'p_statement','usql_parser.py',155),
  ('select_statement -> TRAEME select_items DE_LA_TABLA table_name optional_where','select_statement',5,'p_select_statement','usql_parser.py',159),
  ('select_items -> TODO','select_items',1,'p_select_items','usql_parser.py',163),
  ('select_items -> LOS_DISTINTOS IDENTIFIER','select_items',2,'p_select_items','usql_parser.py',164),
  ('select_items -> IDENTIFIER','select_items',1,'p_select_items','usql_parser.py',165),
  ('table_name -> IDENTIFIER','table_name',1,'p_table_name','usql_parser.py',169),
  ('optional_where -> DONDE conditions','optional_where',2,'p_optional_where','usql_parser.py',173),
  ('optional_where -> empty','optional_where',1,'p_optional_where','usql_parser.py',174),
  ('conditions -> condition','conditions',1,'p_conditions','usql_parser.py',178),
  ('conditions -> conditions logical_operator condition','conditions',3,'p_conditions','usql_parser.py',179),
  ('condition -> IDENTIFIER comparison_operator value','condition',3,'p_condition','usql_parser.py',183),
  ('comparison_operator -> EQUALS','comparison_operator',1,'p_comparison_operator','usql_parser.py',187),
  ('comparison_operator -> GREATER','comparison_operator',1,'p_comparison_operator','usql_parser.py',188),
  ('comparison_operator -> LESS','comparison_operator',1,'p_comparison_operator','usql_parser.py',189),
  ('comparison_operator -> GREATEREQUAL','comparison_operator',1,'p_comparison_operator','usql_parser.py',190),
  ('comparison_operator -> LESSEQUAL','comparison_operator',1,'p_comparison_operator','usql_parser.py',191),
  ('comparison_operator -> NOTEQUAL','comparison_operator',1,'p_comparison_operator','usql_parser.py',192),
  ('value -> STRING','value',1,'p_value','usql_parser.py',196),
  ('value -> NUMBER','value',1,'p_value','usql_parser.py',197),
  ('value -> IDENTIFIER','value',1,'p_value','usql_parser.py',198),
  ('logical_operator -> AND','logical_operator',1,'p_logical_operator','usql_parser.py',202),
  ('logical_operator -> OR','logical_operator',1,'p_logical_operator','usql_parser.py',203),
  ('insert_statement -> METE_EN table_name LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN','insert_statement',9,'p_insert_statement','usql_parser.py',207),
  ('update_statement -> ACTUALIZA table_name SETEA assignment_list optional_where','update_statement',5,'p_update_statement','usql_parser.py',211),
  ('delete_statement -> BORRA_DE_LA table_name optional_where','delete_statement',3,'p_delete_statement','usql_parser.py',215),
  ('alter_table_statement -> CAMBIA_LA_TABLA table_name alter_action','alter_table_statement',3,'p_alter_table_statement','usql_parser.py',219),
  ('column_list -> column_list COMMA IDENTIFIER','column_list',3,'p_column_list','usql_parser.py',223),
  ('column_list -> IDENTIFIER','column_list',1,'p_column_list','usql_parser.py',224),
  ('value_list -> value_list COMMA value','value_list',3,'p_value_list','usql_parser.py',228),
  ('value_list -> value','value_list',1,'p_value_list','usql_parser.py',229),
  ('assignment_list -> assignment_list COMMA assignment','assignment_list',3,'p_assignment_list','usql_parser.py',233),
  ('assignment_list -> assignment','assignment_list',1,'p_assignment_list','usql_parser.py',234),
  ('assignment -> IDENTIFIER EQUALS value','assignment',3,'p_assignment','usql_parser.py',238),
  ('alter_action -> AGREGA_LA_COLUMNA IDENTIFIER data_type constraints','alter_action',4,'p_alter_action','usql_parser.py',242),
  ('alter_action -> ELIMINA_LA_COLUMNA IDENTIFIER','alter_action',2,'p_alter_action','usql_parser.py',243),
  ('data_type -> IDENTIFIER LPAREN NUMBER RPAREN','data_type',4,'p_data_type','usql_parser.py',247),
  ('data_type -> IDENTIFIER','data_type',1,'p_data_type','usql_parser.py',248),
  ('constraints -> constraints constraint','constraints',2,'p_constraints','usql_parser.py',252),
  ('constraints -> constraint','constraints',1,'p_constraints','usql_parser.py',253),
  ('constraints -> empty','constraints',1,'p_constraints','usql_parser.py',254),
  ('constraint -> NO_NULO','constraint',1,'p_constraint','usql_parser.py',258),
  ('constraint -> POR_DEFECTO value','constraint',2,'p_constraint','usql_parser.py',259),
  ('constraint -> UNICO','constraint',1,'p_constraint','usql_parser.py',260),
  ('constraint -> CLAVE_PRIMA','constraint',1,'p_constraint','usql_parser.py',261),
  ('constraint -> CLAVE_REFERENTE','constraint',1,'p_constraint','usql_parser.py',262),
  ('empty -> <empty>','empty',0,'p_empty','usql_parser.py',266),
]
