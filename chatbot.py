from minicolumn import MiniColumn

mcol = MiniColumn(['chat.0.txt', 'chat.1.txt', 'chat.2.txt'], "tests/data")

sent = "read hello"
for elem in mcol.evaluate(sent):
    print(elem)
    print('-')
    for thing in elem:
        print("->", thing)
print("-------------")
print(mcol.get_hits(sent))

