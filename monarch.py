import sys

class Monarch:
    def __init__(self):
        self.stack = [] #empty list
        self.variables = {}  #empty dictionary

    def run(self, code):
        lines = code.splitlines()
        for line in lines:
            parts = line.strip().split(" ", 1)
            if not parts[0]: continue
            
            command = parts[0].upper()
            arg = parts[1] if len(parts) > 1 else None

            try:
                self.execute(command, arg)
            except Exception as e:
                print(f"Error on line '{line}': {e}")

    def execute(self, cmd, arg):
        # 1. PUSH: Add to stack
        if cmd == "PUSH":
            if arg.startswith('"') or arg.startswith("'"):
                self.stack.append(arg[1:-1])
            else:
                self.stack.append(int(arg))

        # 2. PRINT: Pop and display
        elif cmd == "PRINT":
            print(self.stack.pop())

        # 3. INPUT: Get user input and push to stack
        elif cmd == "INPUT":
            val = input(arg[1:-1] if arg else "")
            self.stack.append(val)

        # 4. ADD: Pop two, add them, push result
        elif cmd == "ADD":
            b = int(self.stack.pop())
            a = int(self.stack.pop())
            self.stack.append(a + b)

        # 5. MUL: Pop two, multiply, push result
        elif cmd == "MUL":
            b = int(self.stack.pop())
            a = int(self.stack.pop())
            self.stack.append(a * b)

        # 6. REPEAT: Pop count, pop char, push result
        elif cmd == "REPEAT":
            count = int(self.stack.pop())
            char = str(self.stack.pop())
            self.stack.append(char * count)

        # 7. REVERSE: Pop string, push reversed string
        elif cmd == "REVERSE":
            s = str(self.stack.pop())
            self.stack.append(s[::-1])

        # 8. EVEN: Pop int, push "True" if even else "False"
        elif cmd == "EVEN":
            val = int(self.stack.pop())
            self.stack.append("True" if val % 2 == 0 else "False")

        # 9. DUP: Duplicate top of stack 
        elif cmd == "DUP":
            self.stack.append(self.stack[-1])
        
        elif cmd == "COMPARE":
            b = self.stack.pop()
            a = self.stack.pop()
            self.stack.append("True" if str(a) == str(b) else "False")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            Monarch().run(f.read())