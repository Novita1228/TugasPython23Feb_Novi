def celsius_ke_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15

def celsius_ke_reaumur(c):
    return c * 4 / 5

def fahrenheit_ke_celsius(f):
    return (f - 32) * 5 / 9

def fahrenheit_ke_kelvin(f):
    return fahrenheit_ke_celsius(f) + 273.15

def fahrenheit_ke_reaumur(f):
    return fahrenheit_ke_celsius(f) * 4 / 5

def kelvin_ke_celsius(k):
    return k - 273.15

def kelvin_ke_fahrenheit(k):
    return celsius_ke_fahrenheit(kelvin_ke_celsius(k))

def kelvin_ke_reaumur(k):
    return celsius_ke_reaumur(kelvin_ke_celsius(k))

def reaumur_ke_celsius(r):
    return r * 5 / 4

def reaumur_ke_fahrenheit(r):
    return celsius_ke_fahrenheit(reaumur_ke_celsius(r))

def reaumur_ke_kelvin(r):
    return celsius_ke_kelvin(reaumur_ke_celsius(r))

def klasifikasi_suhu(celsius):
    if celsius <= 0:
        return "Beku"
    elif celsius <= 15:
        return "Dingin"
    elif celsius <= 25:
        return "Normal"
    elif celsius <= 35:
        return "Panas"
    else:
        return "Sangat Panas"

def konversi_ke_celsius(nilai, skala):
    if skala == 'celsius':
        return nilai
    elif skala == 'fahrenheit':
        return fahrenheit_ke_celsius(nilai)
    elif skala == 'kelvin':
        return kelvin_ke_celsius(nilai)
    elif skala == 'reaumur':
        return reaumur_ke_celsius(nilai)

def konversi_suhu(nilai, dari, ke):
    tabel = {
        ('celsius', 'fahrenheit'): celsius_ke_fahrenheit,
        ('celsius', 'kelvin'): celsius_ke_kelvin,
        ('celsius', 'reaumur'): celsius_ke_reaumur,
        ('fahrenheit', 'celsius'): fahrenheit_ke_celsius,
        ('fahrenheit', 'kelvin'): fahrenheit_ke_kelvin,
        ('fahrenheit', 'reaumur'): fahrenheit_ke_reaumur,
        ('kelvin', 'celsius'): kelvin_ke_celsius,
        ('kelvin', 'fahrenheit'): kelvin_ke_fahrenheit,
        ('kelvin', 'reaumur'): kelvin_ke_reaumur,
        ('reaumur', 'celsius'): reaumur_ke_celsius,
        ('reaumur', 'fahrenheit'): reaumur_ke_fahrenheit,
        ('reaumur', 'kelvin'): reaumur_ke_kelvin,
    }
    if dari == ke:
        return nilai
    fungsi = tabel.get((dari, ke))
    if fungsi is None:
        raise ValueError("Konversi tidak valid!")
    return fungsi(nilai)

SIMBOL_SUHU = {
    'celsius': '°C',
    'fahrenheit': '°F',
    'kelvin': 'K',
    'reaumur': '°R'
}

def menu_konversi_suhu(simpan_riwayat):
    skala_list = ['celsius', 'fahrenheit', 'kelvin', 'reaumur']
    print("\nSkala: 1.Celsius  2.Fahrenheit  3.Kelvin  4.Reaumur")
    d = input("Dari (1-4): ").strip()
    k = input("Ke (1-4): ").strip()
    nilai = float(input("Nilai: "))

    dari = skala_list[int(d) - 1]
    ke = skala_list[int(k) - 1]
    hasil = konversi_suhu(nilai, dari, ke)
    cel = konversi_ke_celsius(nilai, dari)
    klas = klasifikasi_suhu(cel)

    print(f"Hasil: {hasil:.1f}{SIMBOL_SUHU[ke]}")
    print(f"Klasifikasi: {klas}")
    simpan_riwayat(f"{nilai}{SIMBOL_SUHU[dari]} → {hasil:.1f}{SIMBOL_SUHU[ke]} ({klas})")

def menu_tabel_konversi(simpan_riwayat):
    print("\nTabel konversi dari Celsius ke semua skala")
    mulai = int(input("Suhu awal (°C): "))
    akhir = int(input("Suhu akhir (°C): "))
    step = int(input("Step: "))

    print(f"\n{'°C':>8} {'°F':>10} {'K':>10} {'°R':>10} {'Klasifikasi':>15}")
    print("-" * 58)
    for c in range(mulai, akhir + 1, step):
        f = celsius_ke_fahrenheit(c)
        k = celsius_ke_kelvin(c)
        r = celsius_ke_reaumur(c)
        kl = klasifikasi_suhu(c)
        print(f"{c:>8.1f} {f:>10.1f} {k:>10.2f} {r:>10.1f} {kl:>15}")

def menu_klasifikasi_suhu(simpan_riwayat):
    nilai = float(input("\nMasukkan suhu (°C): "))
    klas = klasifikasi_suhu(nilai)
    print(f"Suhu {nilai}°C termasuk kategori: {klas}")
    simpan_riwayat(f"Klasifikasi {nilai}°C = {klas}")

def menu_kalkulator_suhu(simpan_riwayat):
    while True:
        print("\n=== KALKULATOR SUHU ===")
        print("1. Konversi Satuan")
        print("2. Tabel Konversi")
        print("3. Klasifikasi Suhu")
        print("0. Kembali")
        pilih = input("Pilih: ").strip()
        try:
            if pilih == '1':
                menu_konversi_suhu(simpan_riwayat)
            elif pilih == '2':
                menu_tabel_konversi(simpan_riwayat)
            elif pilih == '3':
                menu_klasifikasi_suhu(simpan_riwayat)
            elif pilih == '0':
                break
            else:
                print("Pilihan tidak valid!")
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
