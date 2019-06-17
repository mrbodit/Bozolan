from bozolan.tokens_and_lexer.lexer import *
from bozolan.parser.parser import *
from bozolan.code_generator.generator import *


try:
    tokens = tokenize("../input_files_in_bozolan/factorial.no")
    ast = Parser(tokens).parse()
    code = CodeGenerator(ast).generate()
    print(code)
    print("___________________________________________________________________________")
    tokens = tokenize("../input_files_in_bozolan/code_generation_sample.no")
    ast = Parser(tokens).parse()
    code = CodeGenerator(ast).generate()
    print(code)
    print("___________________________________________________________________________")
    tokens = tokenize("../input_files_in_bozolan/tokenize_sample.no")
    ast = Parser(tokens).parse()
    code = CodeGenerator(ast).generate()
    print(code)





    with open("../output_python_files/out.py", "w") as out_file:
        out_file.write(code)
except Exception as e:
    print(str(e))