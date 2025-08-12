while True:
    try:
        s=input("String=").lower().strip()
        w=input("Word=").lower().strip()
        w_len=len(w)
        s_b1=s.index(w)
        s_b2=s_b1+(w_len-1)
        rs_b1=s.rindex(w)
        rs_b2=s_b1+(w_len-1)
        print(f"{s_b1}_{s_b2}")
        print(f"{rs_b1}_{rs_b2}")
        print()
    except IndexError:
        print("Please chose a word that exist in the string")