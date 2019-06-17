from enum import Enum


class Token:

    def __init__(self, token_type, value, line, column):
        self.type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return self.value + " (" + str(self.type) + ") "

    def __repr__(self):
        return self.value + " (" + str(self.type) + ") "


class TokenType(Enum):
    INDENTYFIKATOR = 'identifier'

    NUMER = 'number'
    STRING = 'string'
    BOOLEAN = 'boolean'

    BINARNY_OPERATOR = 'binary operator'

    PRZYPISANIE = 'assign'

    LNAWIAS = 'left parenthesis'
    PNAWIAS = 'right parenthesis'

    LWASY = 'left bracket'
    PWASY = 'rightbracket'

    KONIEC_INPUTU = 'end of input'

    NIEZNANE = 'unknown token'

    FUNKCJA = 'function'
    WYPISZ = 'print'
    ZMIENNA = 'variable'
    DOPOKI = 'while loop'
    JEZELI = 'if statement'
    ZWROC = 'return statement'

    KONIEC_WYRAZENIA = 'end of statement'
    PRZECINEK = ','