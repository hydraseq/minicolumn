from minicolumn import MiniColumn

mcol = MiniColumn(['chat.0.txt', 'chat.1.txt', 'chat.2.txt'], "tests/data")

sent = "read junk"
print(mcol.evaluate(sent))
print("-------------")
print(mcol.get_hits(sent))

