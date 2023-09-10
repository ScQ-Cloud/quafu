
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "mainleft+-left*/left^rightUMINUSASSIGN BARRIER CHANNEL CREG FLOAT GATE ID IF INCLUDE INT MATCHES MEASURE NONE OPAQUE OPENQASM PI QREG RESET STRING UNIT\n        main : program\n        \n        program : statement\n        \n        program : program statement\n        \n        statement : OPENQASM FLOAT ';'\n                    | OPENQASM FLOAT error\n                    | OPENQASM error\n        \n        statement : qop ';'\n                | qop error\n                | qif ';'\n                | qif error\n        \n        qif : IF '(' primary MATCHES INT ')' qop \n            | IF '(' primary MATCHES INT error\n            | IF '(' primary MATCHES error\n            | IF '(' primary error\n            | IF '(' error\n            | IF error\n        \n        qop : id primary_list\n            | id '(' ')' primary_list \n            | id '(' expression_list ')' primary_list\n        \n        qop : id '(' ')' error \n            | id '(' error\n            | id '(' expression_list ')' error\n            | id '(' expression_list error\n        \n        qop : MEASURE primary ASSIGN primary\n        \n        qop : MEASURE primary ASSIGN error\n            | MEASURE primary error\n            | MEASURE error\n        \n        qop : BARRIER primary_list\n        \n        qop : BARRIER error\n        \n        qop : RESET primary\n        \n        qop : RESET error\n        \n        qarg_list : id\n        \n        qarg_list : qarg_list ',' id\n        \n        carg_list : id\n        \n        carg_list : carg_list ',' id\n        \n        statement : GATE id gate_scope qarg_list gate_body \n        \n        statement : GATE id gate_scope '(' ')' qarg_list gate_body \n        \n        statement : GATE id gate_scope '(' carg_list ')' qarg_list gate_body \n        \n        gate_scope : \n        \n        gate_body : '{' gate_scope '}'\n                    | '{' gate_scope error\n        \n        gate_body : '{' gop_list gate_scope '}'\n                    | '{' gop_list gate_scope error\n        \n        gop_list : gop\n        \n        gop_list : gop_list gop\n        \n        gop : id id_list ';'\n            | id id_list error\n            | id '(' ')' id_list ';'\n            | id '(' ')' id_list error\n            | id '(' ')' error\n            | id '(' error\n        \n        gop : id '(' expression_list ')' id_list ';'\n            | id '(' expression_list ')' id_list error\n            | id '(' expression_list ')' error\n            | id '(' expression_list error\n        \n        gop : BARRIER id_list ';'\n            | BARRIER id_list error\n            | BARRIER error\n        \n        statement : qdecl ';'\n                    | cdecl ';'\n                    | qdecl error\n                    | cdecl error\n        \n        qdecl : QREG indexed_id\n                | QREG error\n        \n        cdecl : CREG indexed_id\n                | CREG error\n        \n        id : ID\n            | error\n        \n        indexed_id : id '[' INT ']'\n                    | id '[' INT error\n                    | id '[' error\n        \n        primary : id\n                | indexed_id\n        \n        primary_list : primary\n                     | primary_list ',' primary\n        \n        id_list : id\n        \n        id_list : id_list ',' id\n        \n        unary : INT\n        \n        unary : FLOAT\n        \n        unary : PI\n        \n        unary : id\n        \n        expression : expression '*' expression\n                    | expression '/' expression\n                    | expression '+' expression\n                    | expression '-' expression\n                    | expression '^' expression\n        \n        expression : - expression %prec UMINUS\n        \n        expression : unary\n        \n        expression : '(' expression ')'\n        \n        expression : id '(' expression ')'\n        \n        expression_list : expression\n        \n        expression_list : expression_list ',' expression\n        \n        ignore : STRING\n        "
    
_lr_action_items = {'OPENQASM':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[4,4,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'GATE':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[8,8,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'MEASURE':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,122,124,125,133,137,138,147,],[12,12,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,12,-40,-41,-37,-42,-43,-38,]),'BARRIER':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,94,114,115,122,124,125,127,132,133,137,138,139,140,143,145,146,147,150,152,153,154,156,157,158,],[13,13,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,117,117,-44,13,-40,-41,-45,-58,-37,-42,-43,-46,-47,-51,-56,-57,-38,-50,-55,-48,-49,-54,-52,-53,]),'RESET':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,122,124,125,133,137,138,147,],[14,14,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,14,-40,-41,-37,-42,-43,-38,]),'IF':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[15,15,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'QREG':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[16,16,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'CREG':([0,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[17,17,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'ID':([0,2,3,5,8,9,12,13,14,16,17,18,19,21,22,23,24,25,26,29,32,33,34,35,42,49,50,51,53,55,56,60,65,71,75,79,81,82,83,84,85,86,92,93,94,96,114,115,116,117,119,120,122,124,125,127,130,132,133,137,138,139,140,141,142,143,145,146,147,150,151,152,153,154,156,157,158,],[18,18,-2,-68,18,18,18,18,18,18,18,-67,-3,-6,-7,-8,-9,-10,-39,18,-59,-61,-60,-62,18,-4,-5,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-36,18,18,18,18,-44,18,18,18,18,18,-40,-41,-45,18,-58,-37,-42,-43,-46,-47,18,18,-51,-56,-57,-38,-50,18,-55,-48,-49,-54,-52,-53,]),'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,72,73,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,98,99,101,102,103,104,105,106,107,108,109,110,111,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,],[5,5,-2,21,-68,23,25,5,5,33,35,37,39,41,43,45,48,-67,-3,50,-6,-7,-8,-9,-10,-39,-72,-17,58,-74,-73,-59,-61,-60,-62,66,-27,-28,-29,-30,-31,68,-16,-63,-64,-65,-66,-4,-5,5,73,5,-81,5,78,80,-21,-91,5,-88,-78,-79,-80,89,-26,91,-15,5,99,-71,-75,5,-18,-20,103,-23,5,5,5,5,5,5,-87,-24,-25,111,-14,-36,5,5,5,-69,-70,-89,-19,-22,-92,-82,-83,-84,-85,-86,123,-13,125,5,-44,5,132,5,5,-90,5,-12,-40,-41,138,-45,-76,140,143,146,-58,-37,-11,-42,-43,-46,-47,5,150,-51,152,-56,-57,-38,-77,154,-50,156,-55,-48,-49,158,-54,-52,-53,]),'$end':([1,2,3,19,21,22,23,24,25,32,33,34,35,49,50,92,124,125,133,137,138,147,],[0,-1,-2,-3,-6,-7,-8,-9,-10,-59,-61,-60,-62,-4,-5,-36,-40,-41,-37,-42,-43,-38,]),'FLOAT':([4,29,55,60,75,81,82,83,84,85,86,130,],[20,63,63,63,63,63,63,63,63,63,63,63,]),'(':([5,9,15,18,26,29,51,54,55,58,60,75,81,82,83,84,85,86,116,130,143,],[-68,29,42,-67,-39,55,71,75,55,-68,55,55,55,55,55,55,55,55,130,55,-68,]),'[':([5,18,27,37,39,41,45,46,48,68,78,89,103,],[-68,-67,52,-68,-68,-68,-68,52,-68,-68,-68,-68,-68,]),',':([5,18,27,28,30,31,38,39,54,57,58,59,61,62,63,64,69,70,73,74,77,78,87,95,97,98,99,101,102,103,104,105,106,107,108,109,112,118,121,128,129,131,132,134,135,143,144,148,149,150,155,156,],[-68,-67,-72,53,-74,-73,53,-68,-81,81,-68,-91,-88,-78,-79,-80,-32,93,-71,-75,53,-68,-87,-34,120,-69,-70,-89,53,-68,-92,-82,-83,-84,-85,-86,-33,93,-90,-76,141,141,-68,93,-35,-68,81,-77,141,-68,141,-68,]),';':([5,6,7,10,11,18,20,27,28,30,31,37,38,39,40,41,43,44,45,47,48,58,66,68,73,74,77,78,80,88,89,91,98,99,102,103,111,123,128,129,131,132,136,148,149,150,155,156,],[-68,22,24,32,34,-67,49,-72,-17,-74,-73,-27,-28,-29,-30,-31,-16,-63,-64,-65,-66,-21,-26,-15,-71,-75,-18,-20,-23,-24,-25,-14,-69,-70,-19,-22,-13,-12,-76,139,145,-68,-11,-77,153,-68,157,-68,]),'{':([5,18,69,70,112,118,134,],[-68,-67,-32,94,-33,94,94,]),')':([5,18,29,54,57,58,59,61,62,63,64,71,76,87,95,97,100,101,104,105,106,107,108,109,110,121,130,135,143,144,],[-68,-67,56,-81,79,-68,-91,-88,-78,-79,-80,96,101,-87,-34,119,121,-89,-92,-82,-83,-84,-85,-86,122,-90,142,-35,-68,151,]),'*':([5,18,54,58,59,61,62,63,64,76,87,100,101,104,105,106,107,108,109,121,143,],[-68,-67,-81,-68,82,-88,-78,-79,-80,82,-87,82,-89,82,-82,-83,82,82,-86,-90,-68,]),'/':([5,18,54,58,59,61,62,63,64,76,87,100,101,104,105,106,107,108,109,121,143,],[-68,-67,-81,-68,83,-88,-78,-79,-80,83,-87,83,-89,83,-82,-83,83,83,-86,-90,-68,]),'+':([5,18,54,58,59,61,62,63,64,76,87,100,101,104,105,106,107,108,109,121,143,],[-68,-67,-81,-68,84,-88,-78,-79,-80,84,-87,84,-89,84,-82,-83,-84,-85,-86,-90,-68,]),'-':([5,18,29,54,55,58,59,60,61,62,63,64,75,76,81,82,83,84,85,86,87,100,101,104,105,106,107,108,109,121,130,143,],[-68,-67,60,-81,60,-68,85,60,-88,-78,-79,-80,60,85,60,60,60,60,60,60,-87,85,-89,85,-82,-83,-84,-85,-86,-90,60,-68,]),'^':([5,18,54,58,59,61,62,63,64,76,87,100,101,104,105,106,107,108,109,121,143,],[-68,-67,-81,-68,86,-88,-78,-79,-80,86,-87,86,-89,86,86,86,86,86,-86,-90,-68,]),'ASSIGN':([18,27,31,36,37,73,98,99,],[-67,-72,-73,65,-68,-71,-69,-70,]),'MATCHES':([18,27,31,67,68,73,98,99,],[-67,-72,-73,90,-68,-71,-69,-70,]),'INT':([29,52,55,60,75,81,82,83,84,85,86,90,130,],[62,72,62,62,62,62,62,62,62,62,62,110,62,]),'PI':([29,55,60,75,81,82,83,84,85,86,130,],[64,64,64,64,64,64,64,64,64,64,64,]),']':([72,],[98,]),'}':([94,113,114,115,126,127,132,139,140,143,145,146,150,152,153,154,156,157,158,],[-39,124,-39,-44,137,-45,-58,-46,-47,-51,-56,-57,-50,-55,-48,-49,-54,-52,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main':([0,],[1,]),'program':([0,],[2,]),'statement':([0,2,],[3,19,]),'qop':([0,2,122,],[6,6,136,]),'qif':([0,2,],[7,7,]),'id':([0,2,8,9,12,13,14,16,17,29,42,51,53,55,56,60,65,71,75,79,81,82,83,84,85,86,93,94,96,114,116,117,119,120,122,130,141,142,151,],[9,9,26,27,27,27,27,46,46,54,27,69,27,54,27,54,27,95,54,27,54,54,54,54,54,54,112,116,69,116,128,128,69,135,9,54,148,128,128,]),'qdecl':([0,2,],[10,10,]),'cdecl':([0,2,],[11,11,]),'primary_list':([9,13,56,79,],[28,38,77,102,]),'primary':([9,12,13,14,42,53,56,65,79,],[30,36,30,40,67,74,30,88,30,]),'indexed_id':([9,12,13,14,16,17,42,53,56,65,79,],[31,31,31,31,44,47,31,31,31,31,31,]),'gate_scope':([26,94,114,],[51,113,126,]),'expression_list':([29,130,],[57,144,]),'expression':([29,55,60,75,81,82,83,84,85,86,130,],[59,76,87,100,104,105,106,107,108,109,59,]),'unary':([29,55,60,75,81,82,83,84,85,86,130,],[61,61,61,61,61,61,61,61,61,61,61,]),'qarg_list':([51,96,119,],[70,118,134,]),'gate_body':([70,118,134,],[92,133,147,]),'carg_list':([71,],[97,]),'gop_list':([94,],[114,]),'gop':([94,114,],[115,127,]),'id_list':([116,117,142,151,],[129,131,149,155,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> program','main',1,'p_main','qfasm_parser.py',356),
  ('program -> statement','program',1,'p_program','qfasm_parser.py',366),
  ('program -> program statement','program',2,'p_program_list','qfasm_parser.py',373),
  ('statement -> OPENQASM FLOAT ;','statement',3,'p_statement_openqasm','qfasm_parser.py',386),
  ('statement -> OPENQASM FLOAT error','statement',3,'p_statement_openqasm','qfasm_parser.py',387),
  ('statement -> OPENQASM error','statement',2,'p_statement_openqasm','qfasm_parser.py',388),
  ('statement -> qop ;','statement',2,'p_statement_qop','qfasm_parser.py',401),
  ('statement -> qop error','statement',2,'p_statement_qop','qfasm_parser.py',402),
  ('statement -> qif ;','statement',2,'p_statement_qop','qfasm_parser.py',403),
  ('statement -> qif error','statement',2,'p_statement_qop','qfasm_parser.py',404),
  ('qif -> IF ( primary MATCHES INT ) qop','qif',7,'p_statement_qif','qfasm_parser.py',412),
  ('qif -> IF ( primary MATCHES INT error','qif',6,'p_statement_qif','qfasm_parser.py',413),
  ('qif -> IF ( primary MATCHES error','qif',5,'p_statement_qif','qfasm_parser.py',414),
  ('qif -> IF ( primary error','qif',4,'p_statement_qif','qfasm_parser.py',415),
  ('qif -> IF ( error','qif',3,'p_statement_qif','qfasm_parser.py',416),
  ('qif -> IF error','qif',2,'p_statement_qif','qfasm_parser.py',417),
  ('qop -> id primary_list','qop',2,'p_unitaryop','qfasm_parser.py',457),
  ('qop -> id ( ) primary_list','qop',4,'p_unitaryop','qfasm_parser.py',458),
  ('qop -> id ( expression_list ) primary_list','qop',5,'p_unitaryop','qfasm_parser.py',459),
  ('qop -> id ( ) error','qop',4,'p_unitaryop_error','qfasm_parser.py',476),
  ('qop -> id ( error','qop',3,'p_unitaryop_error','qfasm_parser.py',477),
  ('qop -> id ( expression_list ) error','qop',5,'p_unitaryop_error','qfasm_parser.py',478),
  ('qop -> id ( expression_list error','qop',4,'p_unitaryop_error','qfasm_parser.py',479),
  ('qop -> MEASURE primary ASSIGN primary','qop',4,'p_measure','qfasm_parser.py',488),
  ('qop -> MEASURE primary ASSIGN error','qop',4,'p_measure_error','qfasm_parser.py',497),
  ('qop -> MEASURE primary error','qop',3,'p_measure_error','qfasm_parser.py',498),
  ('qop -> MEASURE error','qop',2,'p_measure_error','qfasm_parser.py',499),
  ('qop -> BARRIER primary_list','qop',2,'p_barrier','qfasm_parser.py',511),
  ('qop -> BARRIER error','qop',2,'p_barrier_error','qfasm_parser.py',519),
  ('qop -> RESET primary','qop',2,'p_reset','qfasm_parser.py',526),
  ('qop -> RESET error','qop',2,'p_reset_error','qfasm_parser.py',534),
  ('qarg_list -> id','qarg_list',1,'p_gate_qarg_list_begin','qfasm_parser.py',541),
  ('qarg_list -> qarg_list , id','qarg_list',3,'p_gate_qarg_list_next','qfasm_parser.py',549),
  ('carg_list -> id','carg_list',1,'p_gate_carg_list_begin','qfasm_parser.py',559),
  ('carg_list -> carg_list , id','carg_list',3,'p_gate_carg_list_next','qfasm_parser.py',567),
  ('statement -> GATE id gate_scope qarg_list gate_body','statement',5,'p_statement_gatedecl_nolr','qfasm_parser.py',577),
  ('statement -> GATE id gate_scope ( ) qarg_list gate_body','statement',7,'p_statement_gatedecl_noargs','qfasm_parser.py',584),
  ('statement -> GATE id gate_scope ( carg_list ) qarg_list gate_body','statement',8,'p_statement_gatedecl_args','qfasm_parser.py',591),
  ('gate_scope -> <empty>','gate_scope',0,'p_gate_scope','qfasm_parser.py',598),
  ('gate_body -> { gate_scope }','gate_body',3,'p_gate_body_emptybody','qfasm_parser.py',606),
  ('gate_body -> { gate_scope error','gate_body',3,'p_gate_body_emptybody','qfasm_parser.py',607),
  ('gate_body -> { gop_list gate_scope }','gate_body',4,'p_gate_body','qfasm_parser.py',615),
  ('gate_body -> { gop_list gate_scope error','gate_body',4,'p_gate_body','qfasm_parser.py',616),
  ('gop_list -> gop','gop_list',1,'p_gop_list_begin','qfasm_parser.py',624),
  ('gop_list -> gop_list gop','gop_list',2,'p_gop_list_next','qfasm_parser.py',630),
  ('gop -> id id_list ;','gop',3,'p_gop_nocargs','qfasm_parser.py',639),
  ('gop -> id id_list error','gop',3,'p_gop_nocargs','qfasm_parser.py',640),
  ('gop -> id ( ) id_list ;','gop',5,'p_gop_nocargs','qfasm_parser.py',641),
  ('gop -> id ( ) id_list error','gop',5,'p_gop_nocargs','qfasm_parser.py',642),
  ('gop -> id ( ) error','gop',4,'p_gop_nocargs','qfasm_parser.py',643),
  ('gop -> id ( error','gop',3,'p_gop_nocargs','qfasm_parser.py',644),
  ('gop -> id ( expression_list ) id_list ;','gop',6,'p_gop_cargs','qfasm_parser.py',661),
  ('gop -> id ( expression_list ) id_list error','gop',6,'p_gop_cargs','qfasm_parser.py',662),
  ('gop -> id ( expression_list ) error','gop',5,'p_gop_cargs','qfasm_parser.py',663),
  ('gop -> id ( expression_list error','gop',4,'p_gop_cargs','qfasm_parser.py',664),
  ('gop -> BARRIER id_list ;','gop',3,'p_gop_barrier','qfasm_parser.py',680),
  ('gop -> BARRIER id_list error','gop',3,'p_gop_barrier','qfasm_parser.py',681),
  ('gop -> BARRIER error','gop',2,'p_gop_barrier','qfasm_parser.py',682),
  ('statement -> qdecl ;','statement',2,'p_statement_bitdecl','qfasm_parser.py',694),
  ('statement -> cdecl ;','statement',2,'p_statement_bitdecl','qfasm_parser.py',695),
  ('statement -> qdecl error','statement',2,'p_statement_bitdecl','qfasm_parser.py',696),
  ('statement -> cdecl error','statement',2,'p_statement_bitdecl','qfasm_parser.py',697),
  ('qdecl -> QREG indexed_id','qdecl',2,'p_qdecl','qfasm_parser.py',706),
  ('qdecl -> QREG error','qdecl',2,'p_qdecl','qfasm_parser.py',707),
  ('cdecl -> CREG indexed_id','cdecl',2,'p_cdecl','qfasm_parser.py',719),
  ('cdecl -> CREG error','cdecl',2,'p_cdecl','qfasm_parser.py',720),
  ('id -> ID','id',1,'p_id','qfasm_parser.py',733),
  ('id -> error','id',1,'p_id','qfasm_parser.py',734),
  ('indexed_id -> id [ INT ]','indexed_id',4,'p_indexed_id','qfasm_parser.py',745),
  ('indexed_id -> id [ INT error','indexed_id',4,'p_indexed_id','qfasm_parser.py',746),
  ('indexed_id -> id [ error','indexed_id',3,'p_indexed_id','qfasm_parser.py',747),
  ('primary -> id','primary',1,'p_primary','qfasm_parser.py',758),
  ('primary -> indexed_id','primary',1,'p_primary','qfasm_parser.py',759),
  ('primary_list -> primary','primary_list',1,'p_primary_list','qfasm_parser.py',767),
  ('primary_list -> primary_list , primary','primary_list',3,'p_primary_list','qfasm_parser.py',768),
  ('id_list -> id','id_list',1,'p_id_list_begin','qfasm_parser.py',780),
  ('id_list -> id_list , id','id_list',3,'p_id_list_next','qfasm_parser.py',786),
  ('unary -> INT','unary',1,'p_unary_int','qfasm_parser.py',795),
  ('unary -> FLOAT','unary',1,'p_unary_float','qfasm_parser.py',801),
  ('unary -> PI','unary',1,'p_unary_pi','qfasm_parser.py',807),
  ('unary -> id','unary',1,'p_unary_id','qfasm_parser.py',814),
  ('expression -> expression * expression','expression',3,'p_expr_binary','qfasm_parser.py',822),
  ('expression -> expression / expression','expression',3,'p_expr_binary','qfasm_parser.py',823),
  ('expression -> expression + expression','expression',3,'p_expr_binary','qfasm_parser.py',824),
  ('expression -> expression - expression','expression',3,'p_expr_binary','qfasm_parser.py',825),
  ('expression -> expression ^ expression','expression',3,'p_expr_binary','qfasm_parser.py',826),
  ('expression -> - expression','expression',2,'p_expr_uminus','qfasm_parser.py',847),
  ('expression -> unary','expression',1,'p_expr_unary','qfasm_parser.py',857),
  ('expression -> ( expression )','expression',3,'p_expr_pare','qfasm_parser.py',863),
  ('expression -> id ( expression )','expression',4,'p_expr_mathfunc','qfasm_parser.py',869),
  ('expression_list -> expression','expression_list',1,'p_exprlist_begin','qfasm_parser.py',881),
  ('expression_list -> expression_list , expression','expression_list',3,'p_exprlist_next','qfasm_parser.py',887),
  ('ignore -> STRING','ignore',1,'p_ignore','qfasm_parser.py',897),
]
