import sys
class Ev:
    def __init__(self):
        self.vars = {}
    def ev(self, s):
        lines = [x for x in s.split("\n") if x.strip() != ""]
        pc = 0
        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case 'while':
                    if self.ev_expr(line.split(maxsplit=1)[1]) != 0: pc += 1
                    else: 
                        while lines[pc].split(maxsplit=1)[0] != 'end':
                            pc += 1
                        pc += 1
                case 'end':
                    while lines[pc].split(maxsplit=1)[0] != 'while': pc -= 1
                case 'print':
                    expr =  line.split(maxsplit=1)[1] if len(line.split()) > 1 else ""
                    res = self.ev_expr(expr)
                    print(res)
                    pc += 1
                case _:
                    if "=" in line:
                        var_name, expr = line.split("=", 1)
                        var_name = var_name.strip()
                        self.vars[var_name] = self.ev_expr(expr.strip())
                    else:
                        res = self.ev_expr(line)
                    pc += 1
    def ev_expr(self, s):
        toks = s.split()
        if not toks:
            return 0
            
        res = self.get_val(toks[0])
        i = 1
        while i < len(toks):
            op = toks[i]
            val = self.get_val(toks[i+1])
            
            if op == "+": res += val
            elif op == "-": res -= val
            elif op == "*": res *= val
            elif op == "/": res = int(res / val)
            elif op == ">=": res = 1 if res >= val else 0
            elif op == "<=": res = 1 if res <= val else 0
            elif op == "==": res = 1 if res == val else 0
            elif op == ">": res = 1 if res > val else 0
            elif op == "<": res = 1 if res < val else 0
            elif op == "%":res = res % val
            elif op == "==":res = 1 if res == val else 0
            
                        
            i += 2
        return res

    def get_val(self, tok):
        if tok.isdigit() or (tok.startswith('-') and tok[1:].isdigit()):
            return int(tok)
        return self.vars.get(tok, 0)

Ev().ev(open(sys.argv[1]).read())