def open_file(name):
    f = open(name, 'r')
    content = f.read()
    f.close
    f = open(name, "w")
    f.write(add_struct(content))

def add_struct(content):
    content = content.replace(", ", ",")
    content = content.replace("{ ", "{")
    newc = ""
    sp = "\n"
    for c in content:
        if c in ("[", ",", "{"):
            newc += c
            sp += "" if c == "," else "  "
            newc += sp
        else:
            if c in ("}", "]"):
                sp = sp[0:len(sp)-2]
                newc += sp + c
            else:
                newc += c
    return newc

if __name__ == "__main__":
    open_file("/home/lr131/projects/pytest/Out")
