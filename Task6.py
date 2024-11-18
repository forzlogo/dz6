list_ = []
s=''
with open("message.txt","r", encoding='utf-8') as f, open("encrypted_message.txt","w") as g:
    b=0
    a = f.read()
    list_.append(a)
    for i in a:
        list_.insert((b-3),i)
        b+=1
    for i in list_:
        s+=i
    c = g.write(s)
