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
| `REPEAT` | Pops a count and a string, then pushes the repeated string. |
| `REVERSE` | Pops a string and pushes its reverse. |
| `EVEN` | Pops a number and pushes "True" (even) or "False" (odd). |
| `DUP` | Copies the top value of the stack. |
| `COMPARE` | Pops two values, pushes "True" if equal, else "False" |

---

### Examples

**python monarch.py examples/is_palindrome.txt**


Enter word: racecar


True


**python monarch.py examples/multiply.txt**


First number: 5


Second number: 4


20


**python monarch.py examples/repeater.txt**


Enter character to repeat: a


Enter how many times: 4


aaaa


**python monarch.py examples/cat.txt**


Enter text: hello


hello


Note on cat: This takes a full string input and prints it back by popping it from the stack.

