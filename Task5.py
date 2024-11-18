with open("part1.txt","r") as f, open("part2.txt","r") as g, open("full_text.txt","a") as h:
    a = f.read()
    b = g.read()
    c = h.write(a + b)
    
    
