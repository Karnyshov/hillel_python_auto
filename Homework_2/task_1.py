import tabulate

print("-"*34)
print("| \\a  | Bell (alert)             |")
print("| \\b  | Backspace                |")
print("| \\n  | New line                 |")
print("| \\t  | Horizontal tab           |")
print("| \\\\  | Backslash \\              |")
print("| \\\"  | Double quotation mark \"  |")
print("| \\\'  | Single quotation mark \'  |")
print("-"*34)

table = [["\\a", "Bell (alert)"],
         ["\\b", "Backspace"],
         ["\\n", "New line"],
         ["\\t", "Horizontal tab "],
         ["\\\\", "Backslash \\"],
         ["\\\"", "Double quotation mark \""],
         ["\\\'", "Single quotation mark \'"]
         ]

print(tabulate.tabulate(table, tablefmt="pretty"))
