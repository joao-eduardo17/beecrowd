# 1942 - Top N
n = int(input())
c = 0
if n == 1:
    c = 1
elif n <= 3:
    c = 3
elif n <= 5:
    c = 5
elif n <= 10:
    c = 10
elif n <= 25:
    c = 25
elif n <= 50:
    c = 50
else:
    c = 100
print(f"Top {c}")


# 2339 - Aviões de Papel
n = input().split()
if (int(n[0]) * int(n[2])) <= int(n[1]):
    print("S")
else:
    print("N")

# 2374 - Pneu
dese = int(input())
pres = int(input())
print(dese-pres)

# 2388 - Tacógrafo
n = int(input())
total = 0
for c in range(n):
    x = input().split()
    total += (int(x[0]) * int(x[1]))
print(total)

# 2413 - Busca na Internet
l = int(input())
print(l*4)

# 2416 - Corrida
n = input().split()
print(f"{int(n[0]) % int(n[1])}")

# 2455 - Gangorra
n = input().split()
l1 = int(n[0]) * int(n[1])
l2 = int(n[2]) * int(n[3])
if l1 == l2:
    print(0)
elif l1 > l2:
    print(-1)
else:
    print(1)

# 2756 - Saída 10
print("       A")
print("      B B")
print("     C   C")
print("    D     D")
print("   E       E")
print("    D     D")
print("     C   C")
print("      B B")
print("       A")


