# SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER

knowledge_base = {
    "RAM Rusak": {
        "gejala": [
            "komputer sering restart",
            "layar blue screen",
            "bunyi beep saat startup"
        ],
        "solusi": "Bersihkan pin RAM atau ganti RAM."
    },
    "Power Supply Lemah": {
        "gejala": [
            "komputer mati tiba tiba",
            "tidak bisa menyala",
            "kipas tidak berputar"
        ],
        "solusi": "Periksa atau ganti PSU."
    },
    "Overheat Prosesor": {
        "gejala": [
            "komputer cepat panas",
            "komputer mati sendiri",
            "kipas berisik"
        ],
        "solusi": "Bersihkan kipas dan beri thermal paste."
    },
    "VGA Bermasalah": {
        "gejala": [
            "layar blank",
            "tampilan bergaris",
            "tidak ada display"
        ],
        "solusi": "Periksa atau ganti VGA."
    },
    "Hardisk Corrupt": {
        "gejala": [
            "loading lama",
            "file sering hilang",
            "error saat booting"
        ],
        "solusi": "Scan disk atau instal ulang OS."
    }
}

def diagnosa():
    print("\n=== SISTEM PAKAR DIAGNOSA KOMPUTER ===")
    print("Jawab dengan 'y' atau 't'\n")

    gejala_user = []

    # Ambil semua gejala unik
    semua_gejala = set()
    for data in knowledge_base.values():
        semua_gejala.update(data["gejala"])

    # Tanya user
    for g in semua_gejala:
        jawab = input(f"Apakah Anda mengalami '{g}'? (y/t): ").lower()
        if jawab == 'y':
            gejala_user.append(g)

    # Proses inferensi
    hasil = None
    max_cocok = 0
    total_gejala = 0

    for kerusakan, data in knowledge_base.items():
        cocok = len(set(data["gejala"]) & set(gejala_user))

        if cocok > max_cocok:
            max_cocok = cocok
            hasil = kerusakan
            total_gejala = len(data["gejala"])

    # Output
    print("\n=== HASIL DIAGNOSA ===")
    if hasil and max_cocok > 0:
        persentase = (max_cocok / total_gejala) * 100
        print(f"Kerusakan terdeteksi : {hasil}")
        print(f"Tingkat keyakinan   : {persentase:.0f}%")
        print(f"Solusi              : {knowledge_base[hasil]['solusi']}")
    else:
        print("Tidak terdeteksi kerusakan yang sesuai.")

# Main loop
if __name__ == "__main__":
    while True:
        diagnosa()
        ulang = input("\nIngin diagnosa lagi? (y/t): ").lower()
        if ulang != 'y':
            print("Terima kasih!")
            break