import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

from kalkulator_aritmatika import menu_kalkulator_aritmatika
from kalkulator_suhu import menu_kalkulator_suhu
from kalkulator_bilangan import menu_kalkulator_bilangan
from kalkulator_ip import menu_kalkulator_ip

riwayat = []

def simpan_riwayat(entri):
    riwayat.append(entri)
    if len(riwayat) > 10:
        riwayat.pop(0)

def tampil_riwayat():
    print("\n=== RIWAYAT PERHITUNGAN ===")
    if not riwayat:
        print("Belum ada riwayat perhitungan.")
        return
    for i, r in enumerate(riwayat, 1):
        print(f"  {i}. {r}")
    print(f"Total: {len(riwayat)} entri")

def export_ke_txt():
    if not riwayat:
        print("Belum ada riwayat untuk di-export.")
        return

    nama_file = input("Nama file (tanpa ekstensi): ").strip()
    if not nama_file:
        nama_file = "hasil_kalkulator"
    nama_file += ".txt"

    try:
        with open(nama_file, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("  RIWAYAT PERHITUNGAN - KALKULATOR MULTI-FUNGSI\n")
            f.write("=" * 50 + "\n\n")
            for i, r in enumerate(riwayat, 1):
                f.write(f"  {i}. {r}\n")
            f.write(f"\nTotal: {len(riwayat)} entri\n")
            f.write("=" * 50 + "\n")
        print(f"Berhasil di-export ke '{nama_file}'!")
        simpan_riwayat(f"Export ke {nama_file}")
    except IOError as e:
        print(f"Gagal menulis file: {e}")

def menu_utama():
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║     SISTEM KALKULATOR MULTI-FUNGSI   ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Kalkulator Aritmatika            ║")
        print("║  2. Kalkulator Suhu                  ║")
        print("║  3. Kalkulator Konversi Bilangan     ║")
        print("║  4. Kalkulator IP Address            ║")
        print("║  5. Riwayat Perhitungan              ║")
        print("║  6. Export Hasil ke File             ║")
        print("║  0. Keluar                           ║")
        print("╚══════════════════════════════════════╝")

        pilih = input("Pilih menu: ").strip()

        if pilih == '1':
            menu_kalkulator_aritmatika(simpan_riwayat)
        elif pilih == '2':
            menu_kalkulator_suhu(simpan_riwayat)
        elif pilih == '3':
            menu_kalkulator_bilangan(simpan_riwayat)
        elif pilih == '4':
            menu_kalkulator_ip(simpan_riwayat)
        elif pilih == '5':
            tampil_riwayat()
        elif pilih == '6':
            export_ke_txt()
        elif pilih == '0':
            print("\nTerima kasih telah menggunakan Kalkulator Multi-Fungsi!")
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 0-6.")

if __name__ == '__main__':
    menu_utama()
