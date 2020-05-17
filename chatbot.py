from minicolumn import MiniColumn

mcol = MiniColumn(['chat.0.txt', 'chat.1.txt', 'chat.2.txt'], "tests/data")

print(mcol.get_hits("good morning"))

