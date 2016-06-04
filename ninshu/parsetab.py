
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '8A196833E6BD620B5EC669B0815A1E75'
    
_lr_action_items = {'=':([10,],[24,]),'YIN':([0,2,4,6,7,11,16,21,23,25,26,35,36,42,44,45,46,],[1,1,-1,1,-5,-8,-2,-6,-7,1,1,1,1,-4,1,1,-9,]),'}':([7,11,21,23,35,36,45,46,],[-5,-8,-6,-7,40,41,46,-9,]),'SEAL':([40,],[42,]),'MULT':([3,5,10,14,15,22,30,31,32,33,34,37,38,39,],[-20,17,-21,-21,17,-19,-17,17,-18,17,17,17,17,17,]),'>':([3,14,15,22,30,31,32,33,],[-20,-21,28,-19,-17,-16,-18,-15,]),'MINUS':([0,1,2,3,4,5,6,7,8,10,11,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,44,45,46,],[8,8,8,-20,-1,18,8,-5,8,-21,-8,-21,18,-2,8,8,8,8,-6,-19,-7,8,8,8,8,8,8,-17,-16,-18,-15,18,8,8,18,18,18,-4,8,8,-9,]),'NUMBER':([0,1,2,4,6,7,8,11,16,17,18,19,20,21,23,24,25,26,27,28,29,35,36,42,44,45,46,],[3,3,3,-1,3,-5,3,-8,-2,3,3,3,3,-6,-7,3,3,3,3,3,3,3,3,-4,3,3,-9,]),'EQ':([3,14,15,22,30,31,32,33,],[-20,-21,29,-19,-17,-16,-18,-15,]),'ID':([0,1,2,4,6,7,8,11,16,17,18,19,20,21,23,24,25,26,27,28,29,35,36,42,44,45,46,],[10,14,10,-1,10,-5,14,-8,-2,14,14,14,14,-6,-7,14,10,10,14,14,14,10,10,-4,10,10,-9,]),'PLUS':([3,5,10,14,15,22,30,31,32,33,34,37,38,39,],[-20,20,-21,-21,20,-19,-17,-16,-18,-15,20,20,20,20,]),';':([3,5,9,10,14,22,30,31,32,33,34,],[-20,-14,23,-21,-21,-19,-17,-16,-18,-15,-13,]),'$end':([2,4,6,7,11,16,21,23,42,46,],[0,-1,-3,-5,-8,-2,-6,-7,-4,-9,]),'<':([3,14,15,22,30,31,32,33,],[-20,-21,27,-19,-17,-16,-18,-15,]),'YANG':([41,],[43,]),'{':([3,12,13,14,22,30,31,32,33,37,38,39,43,],[-20,25,26,-21,-19,-17,-16,-18,-15,-11,-10,-12,44,]),'JUTSU':([0,2,4,6,7,11,16,21,23,42,46,],[12,12,-1,-3,-5,-8,-2,-6,-7,-4,-9,]),'DIV':([3,5,10,14,15,22,30,31,32,33,34,37,38,39,],[-20,19,-21,-21,19,-19,-17,19,-18,19,19,19,19,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chakra':([0,2,],[4,16,]),'yinyang':([0,2,6,25,26,35,36,44,45,],[11,11,11,11,11,11,11,11,11,]),'predicate':([1,],[13,]),'combo_move':([0,2,25,26,44,],[6,6,35,36,45,]),'hand_sign':([0,2,6,25,26,35,36,44,45,],[9,9,9,9,9,9,9,9,9,]),'move':([0,2,6,25,26,35,36,44,45,],[7,7,21,7,7,21,21,7,21,]),'showdown':([0,],[2,]),'expression':([0,1,2,6,8,17,18,19,20,24,25,26,27,28,29,35,36,44,45,],[5,15,5,5,22,30,31,32,33,34,5,5,37,38,39,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> showdown","S'",1,None,None,None),
  ('showdown -> chakra','showdown',1,'p_ninja_showdown','parser.py',24),
  ('showdown -> showdown chakra','showdown',2,'p_ninja_showdown','parser.py',25),
  ('chakra -> combo_move','chakra',1,'p_chakra','parser.py',34),
  ('chakra -> JUTSU { combo_move } SEAL','chakra',5,'p_chakra','parser.py',35),
  ('combo_move -> move','combo_move',1,'p_combo_move','parser.py',45),
  ('combo_move -> combo_move move','combo_move',2,'p_combo_move','parser.py',46),
  ('move -> hand_sign ;','move',2,'p_move','parser.py',55),
  ('move -> yinyang','move',1,'p_move','parser.py',56),
  ('yinyang -> YIN predicate { combo_move } YANG { combo_move }','yinyang',9,'p_yinyang','parser.py',62),
  ('predicate -> expression > expression','predicate',3,'p_predicate','parser.py',69),
  ('predicate -> expression < expression','predicate',3,'p_predicate','parser.py',70),
  ('predicate -> expression EQ expression','predicate',3,'p_predicate','parser.py',71),
  ('hand_sign -> ID = expression','hand_sign',3,'p_hand_sign','parser.py',82),
  ('hand_sign -> expression','hand_sign',1,'p_hand_sign','parser.py',83),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',94),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',95),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','parser.py',96),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parser.py',97),
  ('expression -> MINUS expression','expression',2,'p_expression_UMINUS','parser.py',110),
  ('expression -> NUMBER','expression',1,'p_expression_variable','parser.py',115),
  ('expression -> ID','expression',1,'p_expression_ID','parser.py',121),
]
