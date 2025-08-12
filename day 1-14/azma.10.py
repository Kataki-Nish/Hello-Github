def if_s(a1):
    s=input(a1).lower().strip().capitalize()
    if s=="Exit":
        return "None"
    elif s=="Help":
        return "cont"
    return s
def loop_ch():
    while True:
        N=if_s("Name=")
        if N=="None":
            break
        elif N=="cont":
            print("Write Name (and) Age (and) City")
            continue
        A=if_s("Age=")
        if A=="None":
            break
        elif A=="cont":
            print("Write Name (and) Age (and) City")
            continue
        C=if_s("City=")
        if C=="None":
            break
        elif C=="cont":
            print("Write Name (and) Age (and) City")
            continue
        print(f"Name={N} Age={A} City={C}")
loop_ch()
        