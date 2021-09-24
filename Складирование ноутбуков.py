A1,B1,C1 = int(input()), int(input()), int(input())
A2,B2,C2 = int(input()), int(input()), int(input())
K=(A1 * B1 * C1 >= A2 * B2 * C2)
N1 = (A1 // A2) * (B1 // B2) * (C1 // C2)
N2 = (A1 // A2) * (B1 // C2) * (C1 // B2)
N3 = (A1 // B2) * (B1 // A2) * (C1 // C2)
N4 = (A1 // B2) * (B1 // C2) * (C1 // A2)
N5 = (A1 // C2) * (B1 // A2) * (C1 // B2)
N6 = (A1 // C2) * (B1 // B2) * (C1 // A2)
if K and N1 >= N2 and N1 >= N3 and N1 >= N4 and N1 >= N5 and N1 >= N6:
    print(N1)
elif K and N2 >= N1 and N2 >= N3 and N2 >= N4 and N2 >= N5 and N2 >= N6:
    print(N2)
elif K and N3 >= N1 and N3 >= N2 and N3 >= N4 and N3 >= N5 and N3 >= N6:
    print(N3)
elif K and N4 >= N1 and N4 >= N3 and N4 >= N2 and N4 >= N5 and N4 >= N6:
    print(N4)
elif K and N5 >= N1 and N5 >= N3 and N5 >= N4 and N5 >= N2 and N5 >= N6:
    print(N5)
elif K and N6 >= N1 and N6 >= N3 and N6 >= N4 and N6 >= N5 and N6 >= N2:
    print(N6)
else:
    print(0)

