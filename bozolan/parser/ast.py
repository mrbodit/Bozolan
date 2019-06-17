class Compound:
    def __init__(self):
        self.children = []

class WhileLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class IfStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class NumberLiteral:
    def __init__(self, value):
        self.value = value

class StringLiteral:
    def __init__(self, value):
        self.value = value

class BooleanLiteral:
    def __init__(self, value):
        self.value = value

class Identifier:
    def __init__(self, identifier):
        self.value = identifier

class Declaration:
    def __init__(self, variable, expression):
        self.identifier = variable
        self.expression = expression

class Assignment:
    def __init__(self, variable, expression):
        self.identifier = variable
        self.expression = expression

class BinaryOperation:
    def __init__(self, operation, expression1, expression2):
        self.operation = operation
        self.left = expression1
        self.right = expression2

class Condition:
    def __init__(self, cond, expression1, expression2):
        self.condition = cond
        self.left = expression1
        self.right = expression2

class PrintStatement:
    def __init__(self, exp):
        self.argument = exp

class ReturnStatement:
    def __init__(self, exp):
        self.argument = exp

class FunctionDefinition:
    def __init__(self, identifier, arguments, body):
        self.identifier = identifier
        self.arguments = arguments
        self.body = body

class Identifiers:
    def __init__(self):
        self.children = []

class FunctionCall:
    def __init__(self, identifier, arguments):
        self.identifier = identifier
        self.arguments = arguments

class Epsilon:
    pass
