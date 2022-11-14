from typing import NamedTuple
import re


class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int


#Keywords Explanation
'''
asm: To declare that a block of code is to be passed to the assembler.
auto: A storage class specifier that is used to define objects in a block.
break: Terminates a switch statement or a loop.
case: Used specifically within a switch statement to specify a match for the statement’s expression.
catch: Specifies actions taken when an exception occurs.
char: Fundamental data type that defines character objects.
class: To declare a user-defined type that encapsulates data members and operations or member functions.
const: To define objects whose value will not alter throughout the lifetime of program execution.
continue:- Transfers control to the start of a loop.
default:- Handles expression values in a switch statement that are not handled by case.
delete: Memory deallocation operator.
do: indicate the start of a do-while statement in which the sub-statement is executed repeatedly until the value of the expression is logical-false.
double:  Fundamental data type used to define a floating-point number.
else: Used specifically in an if-else statement.
enum: To declare a user-defined enumeration data type.
extern: An identifier specified as extern has external linkage to the block.
float:- Fundamental data type used to define a floating-point number.
for: Indicates the start of a statement to achieve repetitive control.
friend: A class or operation whose implementation can access the private data members of a class.
goto: Transfer control to a specified label.
if: Indicate the start of an if statement to achieve selective control.
inline: A function specifier that indicates to the compiler that inline substitution of the function body is to be preferred to the usual function call implementation.
int: Fundamental data type used to define integer objects.
long: A data type modifier that defines a 32-bit int or an extended double.
new: Memory allocation operator.
operator: Overloads a c++ operator with a new declaration.
private: Declares class members which are not visible outside the class.
protected: Declares class members which are private except to derived classes
public: Declares class members who are visible outside the class.
register: A storage class specifier that is an auto specifier, but which also indicates to the compiler that an object will be frequently used and should therefore be kept in a register.
return: Returns an object to a function's caller.
short: A data type modifier that defines a 16-bit int number.
signed: A data type modifier that indicates an object's sign is to be stored in the high-order bit.
sizeof: Returns the size of an object in bytes.
static: The lifetime of an object-defined static exists throughout the lifetime of program execution.
struct: To declare new types that encapsulate both data and member functions.
switch: This keyword used in the “Switch statement”.
template: parameterized or generic type.
this:  A class pointer points to an object or instance of the class.
throw: Generate an exception.
try: Indicates the start of a block of exception handlers.
typedef: Synonym for another integral or user-defined type.
union: Similar to a structure, struct, in that it can hold different types of data, but a union can hold only one of its members at a given time.
unsigned: A data type modifier that indicates the high-order bit is to be used for an object.
virtual: A function specifier that declares a member function of a class that will be redefined by a derived class.
void: Absent of a type or function parameter list.
volatile: Define an object which may vary in value in a way that is undetectable to the compiler.
while: Start of a while statement and end of a do-while statement.

'''
def tokenize(code):
    # Cpp keywords;
    keywords_cpp = {'asm','operator','new','template','private',
                    'this','protected','this','throw','catch','try',
                    'class','friend','virtual','inline','delete',
                    'auto', 'break', 'case', 'char',
                    'dynamic_cast', 'dynamic_cast', 'reinterpret_cast',
                    'bool', 'explicit', 'static_cast', 'false', 'typeid',
                    'const_cast', 'mutable', 'true', 'typename', 'using', 'wchar_t'
                    'const', 'continue', 'default', 'do',
                    'double', 'else', 'enum', 'extern',
                    'float', 'for', 'goto', 'if',
                    'int', 'long', 'register', 'return',
                    'short', 'signed', 'sizeof', 'static',
                    'struct', 'switch', 'typedef', 'union',
                    'unsigned', 'void', 'volatile', 'while'}
    # each element in the token_specification list is a named tuple that represents a possible token
    token_specification = [
        # we use a namedtuple in here. It's like a normal tuple but with named fields.
        # So we can get the values using names.
        ('assignment_operator', r'=|(/=)|\*=|%=|\+=|-=|>>=|<<=|&=|^=|\|='),  # assignment-operator identifier
        ('unary_operator', r'\*|\&|\+|\-|\!|\~|\/|\|'),
        ('letter_', r'A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|_'),
        ('digit', r'0|1|2|3|4|5|6|7|8|9|_')
    ]

    # This creates a regular expression that contains all the expressions u wrote in the token_specification list.
    # it uses the property that the regular expression a|b will get either a or b .
    # The syntax uses an idea called list comprehension to create a one line code.
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1
    line_start = 0
    # This for loop iterates over all the found matches in the input code and then creates a token for each match.
    # The finditer method can be found in the python documentation linked in the Task page.
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start

        # The yield statement is part f a concept called generators in python.
        yield Token(kind, value, line_num, column)


def main():
    # ToDo: U have to add the file handling logic in here and then pass the code to the tokenize() function.
    statement = '+ = - a A B T h l'
    for token in tokenize(statement):
        print(token)


if __name__ == '__main__':
    main()
