# Monarch

Monarch is a stack-based esoteric programming language. It uses a **LIFO** (Last-In, First-Out) stack to store data and perform operations.

### Instruction Set

| Instruction | Description |
| :--- | :--- |
| `PUSH [val]` | Adds a number or "string" to the top of the stack. |
| `PRINT` | Removes and prints the top value. |
| `INPUT "msg"` | Takes user input and pushes it to the stack. |
| `ADD` | Pops two numbers, adds them, and pushes the result. |
| `MUL` | Pops two numbers, multiplies them, and pushes the result. |
| `REVERSE` | Pops a string and pushes its reverse. |
| `EVEN` | Pops a number and pushes "True" (even) or "False" (odd). |
| `DUP` | Copies the top value of the stack. |
| `COMPARE` | Pops two values, pushes "True" if equal, else "False" |
| `STORE` | Pops the top value and saves it to a variable name. |
| `SUB` | Pops two numbers, subtracts them ($a - b$), and pushes the result. |
| `JUMP` | Pops a value; if it's $> 0$, jumps the program to that line number. |
| `LOAD` | Pushes the value of a saved variable onto the stack. |

---

### Examples

```text
python monarch.py examples/is_palindrome.txt
```

Enter word to check: 

racecar

Original word was: 

racecar

Reversed word is: 

racecar

Is Palindrome? 

True

```text
python monarch.py examples/multiply.txt
```

First number: 5


Second number: 4


20

```text
python monarch.py examples/repeater.txt
```

Enter character: a

How many times: 4

a

a

a

a

```text
python monarch.py examples/cat.txt
```

Enter text: hello


hello


Note on cat: This takes a full string input and prints it back by popping it from the stack.

