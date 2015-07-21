__author__ = 'cpalmer'


def parse(string):
    axioms = []
    while len(string) > 0:
        inside_paren = isolate_parens(string)
        while inside_paren != '':
            axioms.append(inside_paren)
            remove_paren(string)
            inside_paren = isolate_parens(string)


def error_check(string):
    i = 0
    while i < len(string)-1:
        if string[i] == '~' or string[i] == '*' or string[i] == '+':
            if string[i+1] == '*' or string[i+1] == '+':
                print "syntax error"
                exit(-1)
        i += 1


def remove_paren(string):
    i = 0
    while i < len(string):
        if string[i] == '(':
            beginparen = i
            while i < len(string):
                if string[i] == ')':
                    endparen = i
                    return string[0:beginparen+1] + string[endparen:len(string)-1]

                else:
                    i += 1
            print "missmatched parens"
            exit(-1)

        elif string[i] == ')':
            print"missmatched parens"
            exit(-1)

        else:
            i += 1

    return ''


def isolate_parens(string):
    i = 0
    while i < len(string):
        if string[i] == '(':
            beginparen = i
            while i < len(string):
                if string[i] == ')':
                    endparen = i
                    return string[beginparen+1:endparen]

                else:
                    i += 1
            print "missmatched parens"
            exit(-1)

        elif string[i] == ')':
            print"missmatched parens"
            exit(-1)

        else:
            i += 1

    return ''


'''
def parse_ands(string):


def parse_ors(string):


def parse_negations(string):


def solve():

'''