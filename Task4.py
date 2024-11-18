s = ""
with open("story.txt","r") as f, open("new_story.txt","w") as g:
    a = f.read()
    b = a.split()
    for i in b:
        if i == "Python":
            s+="Java "
        else:
            s+=(f"{i} ")
    c = g.write(s)
