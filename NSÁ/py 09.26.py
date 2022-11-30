print("Számológép")
szam1=float(input("Szám 1: "))
szam2=float(input("Szám 2: "))
muv=input("Művelet: ")
if muv=="+":
    print(szam1,muv,szam2,"=",(szam1+szam2))
elif muv=="-":
    print(szam1,muv,szam2,"=",(szam1-szam2))
elif muv=="*":
    print(szam1,muv,szam2,"=",(szam1*szam2))
elif muv=="/":
    print(szam1,muv,szam2,"=",(szam1/szam2))
elif muv=="%":
    print(szam1,muv,szam2,"=",(szam1%szam2))
else:
    print("Hibás művelet!")

