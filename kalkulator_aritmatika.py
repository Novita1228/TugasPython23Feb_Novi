import math

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan!")
    return a / b

def pangkat(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        raise ValueError("Modulo dengan nol tidak diperbolehkan!")
    return a % b

def akar_kuadrat(a):
    if a < 0:
        raise ValueError("Tidak dapat menghitung akar kuadrat bilangan negatif!")
    return math.sqrt(a)

def fungsi_sin(x):
    return math.sin(math.radians(x))

def fungsi_cos(x):
    return math.cos(math.radians(x))

def fungsi_tan(x):
    return math.tan(math.radians(x))

def fungsi_log(x):
    if x <= 0:
        raise ValueError("Log hanya untuk bilangan positif!")
    return math.log10(x)

def fungsi_ln(x):
    if x <= 0:
        raise ValueError("Ln hanya untuk bilangan positif!")
    return math.log(x)

def tokenisasi(ekspresi):
    tokens = []
    i = 0
    while i < len(ekspresi):
        if ekspresi[i] == ' ':
            i += 1
            continue
        if ekspresi[i] in '+-*/%^':
            tokens.append(ekspresi[i])
            i += 1
        else:
            j = i
            while j < len(ekspresi) and (ekspresi[j].isdigit() or ekspresi[j] == '.'):
                j += 1
            tokens.append(float(ekspresi[i:j]))
            i = j
    return tokens

def evaluasi_ekspresi(ekspresi):
    tokens = tokenisasi(ekspresi)
    langkah_detail = []

    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in '*/%^':
            a = tokens[i - 1]
            op = tokens[i]
            b = tokens[i + 1]
            if op == '*':
                hasil = perkalian(a, b)
            elif op == '/':
                hasil = pembagian(a, b)
            elif op == '%':
                hasil = modulo(a, b)
            elif op == '^':
                hasil = pangkat(a, b)
            tokens[i - 1:i + 2] = [hasil]
            langkah_detail.append(f"{a} {op} {b} = {hasil}")
        else:
            i += 1

    i = 0
    while i < len(tokens):
        if isinstance(tokens[i], str) and tokens[i] in '+-':
            a = tokens[i - 1]
            op = tokens[i]
            b = tokens[i + 1]
            if op == '+':
                hasil = penjumlahan(a, b)
            elif op == '-':
                hasil = pengurangan(a, b)
            tokens[i - 1:i + 2] = [hasil]
            langkah_detail.append(f"{a} {op} {b} = {hasil}")
        else:
            i += 1

    return tokens[0], langkah_detail

def menu_operasi_dasar(simpan_riwayat):
    print("\n--- Operasi Dasar ---")
    print("Operator: +, -, *, /, ^, %, √")
    op = input("Pilih operator: ").strip()

    if op == '√':
        a = float(input("Masukkan bilangan: "))
        hasil = akar_kuadrat(a)
        print(f"√{a} = {hasil}")
        simpan_riwayat(f"√{a} = {hasil}")
        return

    a = float(input("Bilangan pertama: "))
    b = float(input("Bilangan kedua: "))

    if op == '+':
        hasil = penjumlahan(a, b)
    elif op == '-':
        hasil = pengurangan(a, b)
    elif op == '*':
        hasil = perkalian(a, b)
    elif op == '/':
        hasil = pembagian(a, b)
    elif op == '^':
        hasil = pangkat(a, b)
    elif op == '%':
        hasil = modulo(a, b)
    else:
        print("Operator tidak valid!")
        return

    print(f"{a} {op} {b} = {hasil}")
    simpan_riwayat(f"{a} {op} {b} = {hasil}")

def menu_operasi_ilmiah(simpan_riwayat):
    print("\n--- Operasi Ilmiah ---")
    print("1. sin  2. cos  3. tan  4. log  5. ln")
    pilih = input("Pilih fungsi (1-5): ").strip()
    x = float(input("Masukkan nilai: "))

    if pilih == '1':
        hasil = fungsi_sin(x)
        label = f"sin({x}°)"
    elif pilih == '2':
        hasil = fungsi_cos(x)
        label = f"cos({x}°)"
    elif pilih == '3':
        hasil = fungsi_tan(x)
        label = f"tan({x}°)"
    elif pilih == '4':
        hasil = fungsi_log(x)
        label = f"log({x})"
    elif pilih == '5':
        hasil = fungsi_ln(x)
        label = f"ln({x})"
    else:
        print("Pilihan tidak valid!")
        return

    print(f"{label} = {hasil}")
    simpan_riwayat(f"{label} = {hasil}")

def menu_ekspresi_berantai(simpan_riwayat):
    print("\n--- Ekspresi Berantai ---")
    print("Contoh: 5 + 3 * 2 - 4 / 2")
    ekspresi = input("Masukkan ekspresi: ").strip()
    hasil, langkah = evaluasi_ekspresi(ekspresi)
    print(f"Langkah: {', '.join(langkah)}")
    print(f"Hasil: {hasil}")
    simpan_riwayat(f"{ekspresi} = {hasil}")

def menu_kalkulator_aritmatika(simpan_riwayat):
    while True:
        print("\n=== KALKULATOR ARITMATIKA ===")
        print("1. Operasi Dasar")
        print("2. Operasi Ilmiah")
        print("3. Ekspresi Berantai")
        print("0. Kembali")
        pilih = input("Pilih: ").strip()
        try:
            if pilih == '1':
                menu_operasi_dasar(simpan_riwayat)
            elif pilih == '2':
                menu_operasi_ilmiah(simpan_riwayat)
            elif pilih == '3':
                menu_ekspresi_berantai(simpan_riwayat)
            elif pilih == '0':
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
