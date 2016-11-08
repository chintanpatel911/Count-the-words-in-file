#Name : Chintan Patel
#CSU ID: 2473177
#Description: In this project we are asked to write and interpreter
#			  which used the top-down recursive-descent method and 
#			  inherited/synthesized attributed.

import sys
import operator
import re
import collections

just_len = 60

NUM = r'(?P<NUM>\d+\.+\d+)'
INTS = r'(?P<INTS>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
POWERS = r'(?P<POWERS>\^)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'

m_pattern = re.compile('|'.join((NUM, INTS, PLUS, MINUS, TIMES, DIVIDE, POWERS, LPAREN, RPAREN, WS)))
Token = collections.namedtuple('Token', ['type', 'value'])
 
# generate new tokens for each line 

def gen_tokens(pattern, text):
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        token = Token(m.lgroup, m.group())

        if token.type != 'WS':
            yield token

 
class Expression: 

    def parse(self, text):
        self.tokens = gen_tokens(m_pattern, text)
        self.current_token = None
        self.next_token = None
        self._advance()

        return self.expr()

    def _advance(self):
        self.current_token, self.next_token = self.next_token, next(self.tokens, None)

    def _accept(self, token_type):

        if self.next_token and self.next_token.type == token_type:
            self._advance()
            return True
        else:
            return False

    def _expect(self, token_type):
        if not self._accept(token_type):
            raise SyntaxError('Expected ' + token_type)

    def expr(self):

        expr_value = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):

            op = self.current_token.type
            right = self.term()
            if op == 'PLUS':
                expr_value += right
            elif op == 'MINUS':
                expr_value -= right
            else:
                raise SyntaxError('check again ' + op)

        return expr_value

    def term(self):

        term_value = self.factor()

        while self._accept('TIMES') or self._accept('DIVIDE') or self._accept('POWERS'):
            op = self.current_token.type

            if op == 'POWERS':
                x = self.factor()
                term_value = term_value ** x
            elif op == 'TIMES':
                term_value *= self.factor()
            elif op == 'DIVIDE':
                term_value /= self.factor()
            else:
                raise SyntaxError('check again ' + op)

        return term_value

    def factor(self):

        if self._accept('NUM'):
            return float(self.current_token.value)
        elif self._accept('INTS'):
            return int(self.current_token.value)
        elif self._accept('LPAREN'):
            expr_value = self.expr()

            self._expect('RPAREN')

            return expr_value
        else:
            raise SyntaxError(' NUMBER or LPAREN')

e = Expression()

def prog():
    decl_list()
    stmt_list()
    return;

def decl_list():
    decl()
    return;

def stmt_list():
    stmt()
    return;

def decl():
    type()
    id_list()
    return;

def type():
    if (dtr == 'int'):
        for localtype in line.split():
            if localtype !='int' and localtype !=',' and localtype !=';':
                key[localtype] = 0
                #  print word_int
    elif (dtr == 'real'):
        for localtype in line.split():
            if localtype !='real' and localtype !=',' and localtype !=';':
                w_real[localtype] = 0
                # print word_real
    return;
def id_list():
    return;

def stmt():
    ptr = ""
    if dtr != "print":
        for item in key:
            # print string 
            if item == dtr:
                ptr2 = line.partition(' ')[0]
                if ptr2 != "print":
                    for localstmt in line.split():
                        if localstmt != dtr and localstmt != "=" and localstmt != ";":
                            ptr = ptr + localstmt
                            # print eval(ptr)
                    key[item] = eval(ptr)
        # print word_int
        ptr1 = ""
        for item in w_real:
            if item == dtr:
                ptr2 = line.partition(' ')[0]
                if ptr2 != "print":
                    for localstmt in line.split():
                        if localstmt != dtr and localstmt != "=" and localstmt != ";":
                            ptr1 = ptr1 + localstmt

                    w_real[item] = eval(ptr1)
                    # print word_real
    return;

def expr():
    return;

def term():
    return;

def factor():
    return;

def base():
    ptr = ''
    for localstmt in line.split():
        if localstmt != "print" and localstmt != ";":
            for item in key:
                if item == localstmt:
                    yacc = key.get(localstmt)
                    localstmt = "%d" % yacc
            for item in w_real:
                if item == localstmt:
                    yacc = w_real.get(localstmt)
                    localstmt = "%f" % yacc
            ptr = ptr + localstmt
    print(e.parse(ptr))
    return;

dtr = ''
line = ''
g = ''
key = {}
w_real = {}
f = open(sys.argv[1], "r")
data = f.readlines()
for word in data:
    line = word
    ptr1 = word.partition(' ')[0]
    if ptr1 != 'print' and ptr1 != 'real' and ptr1 != 'int':
        dtr = ptr1
        stmt()
    for ctr1 in word.split():
        dtr = ctr1
        if (ctr1 == 'int'):
            type()
        elif (ctr1 == 'real'):
            type()
        elif (ctr1 == 'print'):
            base()
f.close()
prog()