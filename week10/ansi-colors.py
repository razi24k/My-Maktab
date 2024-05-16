# 256 bit colors
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i*16 + j)
        print(f"\u001b[38;5;{code}mDooset Daram")
    print(f"\u001B[0m")