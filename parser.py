"""
This is the parsing library for the prolame language. It uses the Ply bindings
to lex and yacc to parse the program and store all of the individual
components (facts, rules, queries) as their own ASTs in global lists
"""

import ply.lex as lex
import ply.yacc as yacc


tokens = ("LPAREN", "RPAREN", "NOT", "VAR", "NUMBER", "PERIOD", "ENTAILED",
          "IDENT", "COMMA", "PLUS", "MINUS", "TIMES", "MOD", "QUESTION")

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_PERIOD = r"\."
t_COMMA = r","
t_QUESTION = r"\?"

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_MOD = r"%"

t_NOT = r"not"
t_ENTAILED = r":-"

t_VAR = r"[A-Z][a-zA-Z0-9_]*"
t_NUMBER = r"\d+"
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_IDENT(t):
    r"[a-z][A-Za-z0-9_]*"
    if t.value == "not":
        t.type = "NOT"
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    exit(1)


precedence = (
    ('left', 'PLUS', 'MINUS', 'MOD', 'TIMES'),
)


def p_program(p):
    """program : program rule
               | program fact
               | program query
               | program declaration
               | """
    # Don't do anything


def p_declaration(p):
    """declaration : IDENT NUMBER PERIOD"""

    # save this predicate and its arity in the global table
    Program.predicates[p[1]] = int(p[2])


def p_fact(p):
    """fact : IDENT LPAREN params RPAREN PERIOD
            | NOT IDENT LPAREN params RPAREN PERIOD"""
    
    # Add this fact to the global table of facts
    if p[1] == "not":
        Program.facts.append((-1, p[2], p[4]))
    else:
        Program.facts.append((1, p[1], p[3]))


def p_query(p):
    """query : QUESTION IDENT LPAREN params RPAREN PERIOD"""
    
    # Add this query to the global table of queries 
    Program.queries.append((p[2], p[4]))


def p_params(p):
    """params : var_expr
              | params COMMA var_expr"""

    # Return a list of parameters
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_var_expr(p):
    """var_expr : VAR
                | NUMBER
                | var_expr PLUS var_expr
                | var_expr MINUS var_expr
                | var_expr MOD var_expr
                | var_expr TIMES var_expr"""

    # Return either the single term or a tuple of terms
    if len(p) > 2:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = p[1]
        if p[0].isdigit():
            p[0] = int(p[0])


def p_predicate(p):
    """predicate : IDENT LPAREN params RPAREN
                 | NOT IDENT LPAREN params RPAREN"""

    # Return the truth/falsity, predicate, and parameters
    if p[1] == "not":
        p[0] = (-1, p[2], p[4])
    else:
        p[0] = (1, p[1], p[3])


def p_antecedents(p):
    """antecedents : predicate
                   | predicate COMMA antecedents"""

    # Return a list of all the antecedents
    if len(p) < 3:
        p[0] = [p[1]]

    else:
        ret = p[3][:]
        ret.append(p[1])
        p[0] = ret


def p_rule(p):
    "rule : predicate ENTAILED antecedents PERIOD"
    
    # return consequent and antecedents
    Program.rules.append((p[1], p[3]))


def p_error(p):
    if p:
         print(f"Syntax error at token '{p.value}' on line {p.lineno}")
    else:
         print("Syntax error at EOF")
    exit()

class Program:
    """Singleton class that stores some globals"""
    max = 100
    next_variable = 1
    predicates = {}
    rules = []
    facts = []
    queries = []
    clauses = []
    arithmetics = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "%": lambda x, y: x % y,
        "*": lambda x, y: int(x * y)
    }
    predicateToVariable = None
    variableToStatement = {}

    def next_var():
        """Return next available boolean variable indetifier and increment"""
        Program.next_variable += 1
        return Program.next_variable - 1


def parseProgram(program):
    """Run the parser"""
    lexer = lex.lex()
    lexer.input(program)
    yacc.yacc()
    yacc.parse(program)