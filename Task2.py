with open("data.txt","r") as f, open("even_numbers.txt","w") as g:
    b = f.read()
    for i in b:
        if i != " ":
            if int(i) % 2 == 0:
                g.write(f"{i} ")
