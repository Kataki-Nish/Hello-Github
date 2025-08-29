message={"errors":{"error1":"{0} should be integer"}}
lst=[]
def gt(item):
    while True:
        try:
            x=int(input(f"{item}= ").lower.strip())
            if item=="Age":
                x=int(x)
                return x
            else:
                return x
        except ValueError:
            print(message["errors"]["error1"].format(item))
def get_menu():
    K=["Age","Math","English"]
    for o in K:
        lst.append(gt(o))
    
