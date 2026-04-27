import sys

class Monarch:
    def __init__(self):
        self.stack = [] 
        self.variables = {} 

    def run(self, code):
        self.lines = code.splitlines()
        self.current_line = 0 
        
        while self.current_line < len(self.lines):
            line = self.lines[self.current_line]
            self.current_line += 1 
            
            parts = line.strip().split(" ", 1)
            if not parts[0]: continue
            
            command = parts[0].upper()
            arg = parts[1] if len(parts) > 1 else None
            self.execute(command, arg)

    def execute(self, cmd, arg):
        if cmd == "PUSH":
            if arg.startswith('"') or arg.startswith("'"):
                self.stack.append(arg[1:-1])
            else:
                self.stack.append(int(arg))

        elif cmd == "PRINT":
            print(self.stack.pop())

        elif cmd == "INPUT":
            val = input(arg[1:-1] if arg else "")
            self.stack.append(val)

        elif cmd == "ADD":
            b = int(self.stack.pop())
            a = int(self.stack.pop())
            self.stack.append(a + b)

        elif cmd == "MUL":
            b = int(self.stack.pop())
            a = int(self.stack.pop())
            self.stack.append(a * b)

        elif cmd == "REVERSE":
            s = str(self.stack.pop())
            self.stack.append(s[::-1])

        elif cmd == "EVEN":
            val = int(self.stack.pop())
            self.stack.append("True" if val % 2 == 0 else "False")

        elif cmd == "DUP":
            self.stack.append(self.stack[-1])
        
        elif cmd == "COMPARE":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append("True" if str(a) == str(b) else "False")
        
        elif cmd == "STORE":
            self.variables[arg] = self.stack.pop()

        elif cmd == "LOAD":
            self.stack.append(self.variables[arg])

        elif cmd == "SUB":
            b = int(self.stack.pop())
            a = int(self.stack.pop())
            self.stack.append(a - b)

        # JUMP
        elif cmd == "JUMP":
            if int(self.stack.pop()) > 0:
                self.current_line = int(arg) - 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            Monarch().run(f.read())