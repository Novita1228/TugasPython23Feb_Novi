def ip_ke_biner(ip_str):
    oktet = ip_str.strip().split('.')
    if len(oktet) != 4:
        raise ValueError("Format IP tidak valid! Gunakan format x.x.x.x")
    biner_oktet = []
    for o in oktet:
        n = int(o)
        if n < 0 or n > 255:
            raise ValueError(f"Oktet {n} tidak valid (harus 0-255)!")
        bits = ''
        if n == 0:
            bits = '0'
        else:
            temp = n
            while temp > 0:
                bits = str(temp % 2) + bits
                temp //= 2
        biner_oktet.append(bits.zfill(8))
    return '.'.join(biner_oktet)

def hitung_subnet_mask(prefix):
    if prefix < 0 or prefix > 32:
        raise ValueError("Prefix harus antara 0-32!")
    mask_bits = '1' * prefix + '0' * (32 - prefix)
    oktet = []
    for i in range(0, 32, 8):
        oktet_bits = mask_bits[i:i+8]
        nilai = 0
        for j, bit in enumerate(oktet_bits):
            nilai += int(bit) * (2 ** (7 - j))
        oktet.append(str(nilai))
    return '.'.join(oktet)

def hitung_network_address(ip_str, prefix):
    oktet_ip = list(map(int, ip_str.split('.')))
    mask_str = hitung_subnet_mask(prefix)
    oktet_mask = list(map(int, mask_str.split('.')))
    network = [str(oktet_ip[i] & oktet_mask[i]) for i in range(4)]
    return '.'.join(network)

def hitung_broadcast_address(ip_str, prefix):
    oktet_ip = list(map(int, ip_str.split('.')))
    mask_str = hitung_subnet_mask(prefix)
    oktet_mask = list(map(int, mask_str.split('.')))
    broadcast = [str(oktet_ip[i] | (255 - oktet_mask[i])) for i in range(4)]
    return '.'.join(broadcast)

def hitung_jumlah_host(prefix):
    if prefix >= 31:
        return 0
    return (2 ** (32 - prefix)) - 2

def menu_kalkulator_ip(simpan_riwayat):
    while True:
        print("\n=== KALKULATOR IP ADDRESS (BONUS) ===")
        print("1. Analisis IP Address")
        print("2. Konversi IP ke Biner")
        print("0. Kembali")
        pilih = input("Pilih: ").strip()
        try:
            if pilih == '1':
                ip = input("Masukkan IP Address (contoh: 192.168.1.10): ").strip()
                prefix = int(input("Masukkan Prefix Length (contoh: 24): "))

                subnet = hitung_subnet_mask(prefix)
                network = hitung_network_address(ip, prefix)
                broadcast = hitung_broadcast_address(ip, prefix)
                host = hitung_jumlah_host(prefix)
                ip_bin = ip_ke_biner(ip)

                print(f"\n{'='*40}")
                print(f"  IP Address    : {ip}/{prefix}")
                print(f"  IP (Biner)    : {ip_bin}")
                print(f"  Subnet Mask   : {subnet}")
                print(f"  Network Addr  : {network}")
                print(f"  Broadcast Addr: {broadcast}")
                print(f"  Jumlah Host   : {host}")
                print(f"  Range Host    : {network} - {broadcast}")
                print(f"{'='*40}")
                simpan_riwayat(f"IP {ip}/{prefix} → Net:{network} Bcast:{broadcast} Host:{host}")

            elif pilih == '2':
                ip = input("Masukkan IP Address: ").strip()
                biner = ip_ke_biner(ip)
                print(f"IP Biner: {biner}")
                simpan_riwayat(f"IP {ip} → {biner}")

            elif pilih == '0':
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError as e:
            print(f"Error: {e}")
