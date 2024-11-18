with open("input.txt","r", encoding='utf-8') as f, open("output.txt","w") as g:
    b = f.read()
    c = b.upper()
    g.write(c)
