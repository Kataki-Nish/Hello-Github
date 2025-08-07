
while True:
    n=int(input())
    while n<=1:
        print("Number should be more than 1")
        n=int(input())
    M=[i for i in range(1,n) if n%i==0]
    print(M)