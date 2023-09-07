# Qfasm is modified OPENQASM 2.0. Currently it is mainly used to 
# transfer circuit data to backends. Further it will 
# support more instructions (classical or quantum) to enable 
# interaction with quantum hardware

import os
import ply.lex as lex
import numpy as np
from qfasm_parser import Id
from exceptions import LexerError

class QfasmLexer(object):

    def __init__(self, filename:str = None):
        self.build(filename)
        # read qelib1.inc
        qelib1 = os.path.join(os.path.dirname(__file__), 'qelib1.inc')
        self.file_lexer_stack = []
        self.push_lexer(qelib1)

    def build(self, filename:str = None):
        self.lexer = lex.lex(module=self)
        self.lexer.filename = filename
        self.lexer.lineno = 1
        if filename:
            with open(filename,"r") as ifile:
                self.data = ifile.read()
            self.lexer.input(self.data)
    
    def push_lexer(self, filename):
        self.file_lexer_stack.append(self.lexer)
        self.build(filename=filename)
    
    def pop_lexer(self):
        self.lexer = self.file_lexer_stack.pop()

    def input(self, data):
        self.data = data
        self.lexer.input(data)

    def token(self):
        ret = self.lexer.token()
        return ret

    literals = r'=()[]{};<>,.+-/*^"'

    reserved = {
        "creg": "CREG",
        "qreg": "QREG",
        "pi": "PI",
        "measure": "MEASURE",
        "include": "INCLUDE",
        "barrier": "BARRIER",
        "gate": "GATE",
        "opaque":"OPAQUE",
        "reset":"RESET",
        "if":"IF"
    }

    tokens = [
                 "FLOAT",
                 "INT",
                 "STRING",
                 "ASSIGN",
                 "MATCHES",
                 "ID",
                 "UNIT",
                 "CHANNEL",
                 "OPENQASM",
                 "NONE"
             ] + list(reserved.values())
    
    # dispose include file
    def t_INCLUDE(self, _):
        "include"
        filename_token = self.lexer.token()
        if isinstance(filename_token.value, str):
            filename = filename_token.value.strip('"')
        else:
            raise LexerError("Invalid include: need a quoted string as filename.")
        
        # just ignore, because we include it at first
        if filename == 'qelib1.inc' :
            semicolon_token = self.lexer.token()
            if semicolon_token is None or semicolon_token.value != ";":
                raise LexerError(f'Expecting ";" for INCLUDE at line {semicolon_token.lineno}, in file {self.lexer.filename}')
            return self.lexer.token()
            
        if not os.path.exists(filename):
            raise LexerError(f"Include file {filename} cannot be found, at line {filename_token.lineno}, in file {self.lexer.filename}")

        semicolon_token = self.lexer.token()
        if semicolon_token is None or semicolon_token.value != ";":
            raise LexerError(f'Expecting ";" for INCLUDE at line {semicolon_token.lineno}, in file {self.lexer.filename}')
        
        self.push_lexer(filename)
        return self.lexer.token()


    def t_FLOAT(self, t):
        r"(([1-9]\d*\.\d*)|(0\.\d*[1-9]\d*))"
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r"\d+"
        t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r"\"([^\\\"]|\\.)*\""
        return t

    def t_ASSIGN(self, t):
        r"->"
        return t

    def t_MATCHES(self, t):
        r"=="
        return t

    def t_UNIT(self, t):
        r"ns|us"
        return t

    def t_CHANNEL(self, t):
        r"XY|Z"
        return t

    def t_OPENQASM(self, t):
        r"OPENQASM"
        return t

    def t_NONE(self, t):
        r"None"
        return t
    
    def t_CX_U(self, t):
        "CX|U"
        t.type = "ID"
        t.value = Id(t.value, self.lexer.lineno, self.lexer.filename)
        return t
    
    def t_ID(self, t):
        r"[a-z][a-zA-Z0-9_]*"
        t.type = self.reserved.get(t.value, "ID")
        # all the reset | barrier | gate | include  | measure | opaque  
        t.value = Id(t.value, self.lexer.lineno, self.lexer.filename)
        return t
    
    def t_COMMENT(self, _):
        r"//.*"
        pass

    t_ignore = " \t\r"

    def t_error(self, t):
        raise LexerError(f"Illegal character {t.value[0]}")

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    def t_eof(self, _):
        if self.file_lexer_stack:
            self.pop_lexer()
            return self.lexer.token()
        return None

    def test_data(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

    def test_file(self):
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok) 

if __name__ == "__main__":
    m = QfasmLexer('qasm.qasm')
    # m.build()
    # m.test_data("rx(21ns, pi) q[0], q[1]")
    m.test_file()