HEKS_KARAKTER = '0123456789ABCDEF'

def validasi_bilangan(nilai_str, basis):
    karakter_valid = HEKS_KARAKTER[:basis]
    for ch in nilai_str.upper():
        if ch not in karakter_valid:
            return False
    return True

def basis_ke_desimal_manual(nilai_str, basis):
    nilai_str = nilai_str.upper().lstrip('0') or '0'
    desimal = 0
    langkah = []
    panjang = len(nilai_str)

    for i, ch in enumerate(nilai_str):
        posisi = panjang - 1 - i
        digit = HEKS_KARAKTER.index(ch)
        kontribusi = digit * (basis ** posisi)
        desimal += kontribusi
        langkah.append(f"{digit}×{basis}^{posisi}={kontribusi}")

    return desimal, langkah

def desimal_ke_basis_manual(desimal, basis):
    if desimal == 0:
        return '0', ["0 / {} = 0 sisa 0".format(basis)]

    sisa_list = []
    langkah = []
    n = desimal

    while n > 0:
        sisa = n % basis
        hasil_bagi = n // basis
        langkah.append(f"{n:>4} / {basis} = {hasil_bagi:<4} sisa {HEKS_KARAKTER[sisa]} ↑")
        sisa_list.append(HEKS_KARAKTER[sisa])
        n = hasil_bagi

    sisa_list.reverse()
    hasil_str = ''.join(sisa_list)
    return hasil_str, langkah

def konversi_antar_basis(nilai_str, basis_asal, basis_tujuan):
    if basis_asal == 10:
        desimal = int(nilai_str)
        langkah_ke_des = [f"{nilai_str} sudah dalam desimal"]
    else:
        desimal, langkah_ke_des = basis_ke_desimal_manual(nilai_str, basis_asal)

    if basis_tujuan == 10:
        hasil = str(desimal)
        langkah_dari_des = [f"Hasil desimal: {desimal}"]
    else:
        hasil, langkah_dari_des = desimal_ke_basis_manual(desimal, basis_tujuan)

    return hasil, desimal, langkah_ke_des, langkah_dari_des

def penjumlahan_basis(a_str, b_str, basis):
    a_str = a_str.upper()
    b_str = b_str.upper()
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)

    carry = 0
    hasil = []
    proses = []

    for i in range(max_len - 1, -1, -1):
        d_a = HEKS_KARAKTER.index(a_str[i])
        d_b = HEKS_KARAKTER.index(b_str[i])
        total = d_a + d_b + carry
        carry = total // basis
        digit_hasil = total % basis
        hasil.append(HEKS_KARAKTER[digit_hasil])
        proses.append(f"Kolom {max_len-i}: {HEKS_KARAKTER[d_a]}+{HEKS_KARAKTER[d_b]}+carry({carry})={HEKS_KARAKTER[digit_hasil]} carry={carry}")

    if carry > 0:
        hasil.append(HEKS_KARAKTER[carry])
        proses.append(f"Carry akhir: {HEKS_KARAKTER[carry]}")

    hasil.reverse()
    return ''.join(hasil), proses

def pengurangan_basis(a_str, b_str, basis):
    a_str = a_str.upper()
    b_str = b_str.upper()
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)

    borrow = 0
    hasil = []
    proses = []

    for i in range(max_len - 1, -1, -1):
        d_a = HEKS_KARAKTER.index(a_str[i]) - borrow
        d_b = HEKS_KARAKTER.index(b_str[i])
        if d_a < d_b:
            d_a += basis
            borrow = 1
        else:
            borrow = 0
        digit_hasil = d_a - d_b
        hasil.append(HEKS_KARAKTER[digit_hasil])
        proses.append(f"Kolom {max_len-i}: {d_a}-{HEKS_KARAKTER[d_b]}={HEKS_KARAKTER[digit_hasil]} borrow={borrow}")

    hasil.reverse()
    hasil_str = ''.join(hasil).lstrip('0') or '0'
    return hasil_str, proses

def menu_konversi_basis(simpan_riwayat):
    print("\n--- Konversi Basis ---")
    nama_basis = {10: 'Desimal', 2: 'Biner', 8: 'Oktal', 16: 'Heksadesimal'}
    print("1. Desimal (10)  2. Biner (2)  3. Oktal (8)  4. Heksadesimal (16)")
    d = input("Dari (1-4): ").strip()
    k = input("Ke (1-4): ").strip()
    basis_map = {'1': 10, '2': 2, '3': 8, '4': 16}
    basis_asal = basis_map.get(d)
    basis_tujuan = basis_map.get(k)

    if not basis_asal or not basis_tujuan:
        print("Pilihan tidak valid!")
        return

    nilai = input("Nilai: ").strip()

    if basis_asal != 10 and not validasi_bilangan(nilai, basis_asal):
        print(f"Nilai tidak valid untuk basis {basis_asal}!")
        return

    hasil, desimal, langkah1, langkah2 = konversi_antar_basis(
        nilai, basis_asal, basis_tujuan
    )

    print(f"\nLangkah Konversi ({nama_basis[basis_asal]} → {nama_basis[basis_tujuan]}):")
    if basis_asal != 10:
        print(f"  {nama_basis[basis_asal]} → Desimal:")
        for l in langkah1:
            print(f"    {l}")
        print(f"  = {desimal}")
    if basis_tujuan != 10:
        print(f"  Desimal → {nama_basis[basis_tujuan]}:")
        for l in langkah2:
            print(f"    {l}")

    print(f"\nHasil: {hasil}")

    if basis_tujuan == 2:
        verif = bin(desimal)[2:]
    elif basis_tujuan == 8:
        verif = oct(desimal)[2:]
    elif basis_tujuan == 16:
        verif = hex(desimal)[2:].upper()
    else:
        verif = str(desimal)
    status = "✓" if hasil.upper() == verif.upper() else "✗"
    print(f"Verifikasi: {verif} {status}")

    simpan_riwayat(f"{nilai} (basis {basis_asal}) → {hasil} (basis {basis_tujuan})")

def menu_aritmatika_non_desimal(simpan_riwayat):
    print("\n--- Aritmatika Non-Desimal ---")
    print("Basis: 1. Biner (2)  2. Oktal (8)  3. Heksadesimal (16)")
    pil = input("Pilih basis (1-3): ").strip()
    basis_map = {'1': 2, '2': 8, '3': 16}
    basis = basis_map.get(pil)
    if not basis:
        print("Pilihan tidak valid!")
        return

    nama = {2: 'Biner', 8: 'Oktal', 16: 'Heksadesimal'}
    a = input(f"Bilangan pertama ({nama[basis]}): ").strip()
    b = input(f"Bilangan kedua ({nama[basis]}): ").strip()

    if not validasi_bilangan(a, basis) or not validasi_bilangan(b, basis):
        print(f"Nilai tidak valid untuk basis {basis}!")
        return

    print("Operasi: 1. Penjumlahan (+)  2. Pengurangan (-)")
    op = input("Pilih (1-2): ").strip()

    if op == '1':
        hasil, proses = penjumlahan_basis(a, b, basis)
        simbol = '+'
    elif op == '2':
        hasil, proses = pengurangan_basis(a, b, basis)
        simbol = '-'
    else:
        print("Pilihan tidak valid!")
        return

    print(f"\nProses ({nama[basis]}):")
    for p in proses:
        print(f"  {p}")
    print(f"\n{a} {simbol} {b} = {hasil} (basis {basis})")
    simpan_riwayat(f"{a} {simbol} {b} = {hasil} (basis {basis})")

def menu_kalkulator_bilangan(simpan_riwayat):
    while True:
        print("\n=== KALKULATOR BILANGAN ===")
        print("1. Konversi Basis")
        print("2. Operasi Aritmatika Biner/Oktal/Heks")
        print("0. Kembali")
        pilih = input("Pilih: ").strip()
        try:
            if pilih == '1':
                menu_konversi_basis(simpan_riwayat)
            elif pilih == '2':
                menu_aritmatika_non_desimal(simpan_riwayat)
            elif pilih == '0':
                break
            else:
                print("Pilihan tidak valid!")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
