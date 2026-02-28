import os
def mask(ph):
    ph = ph.strip()
    return ph[:2] + "******" + ph[-2:]
def total(*args):
    return sum(args)
def save(fname, content):
    with open(fname, "w") as f:
        f.write(content)
def log(lfile, entry):
    with open(lfile, "a") as lf:
        lf.write(entry + "\n")
def ticket(**kw):
    print("\nMOVIE TICKET")
    for k, v in kw.items():
        print(f"{k.capitalize()}: {v}")
    print("\n")
    txt = "MOVIE TICKET\n"
    for k, v in kw.items():
        txt += f"{k.capitalize()}: {v}\n"
    txt += "\n"
    return txt
