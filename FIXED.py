class BukuTelepon:
    def __init__(self):
        self.kontak = {}

    def tambah_kontak(self, nama, nomor_hp):
        nama_clean = nama.strip()
        
        # Fix 1: nomor HP harus angka
        if not nomor_hp.isdigit():
            print("[ERROR] Nomor HP harus angka!")
            return
            
        # Fix 2: cek duplikasi nama
        if nama_clean in self.kontak:
            print("[WARNING] Kontak sudah ada.")
            return
            
        self.kontak[nama_clean] = nomor_hp
        print("[SUCCESS] Kontak disimpan.")

    def cari_kontak(self, keyword):
        print(f"\n--- Hasil Pencarian: '{keyword}' ---")
        ditemukan = False
        
        # Fix 3: pencarian disamakan huruf kecilnya (case-insensitive)
        for nama, nomor in self.kontak.items():
            if keyword.lower() in nama.lower():
                print(f"- {nama}: {nomor}")
                ditemukan = True
                
        if not ditemukan:
            print("Kontak tidak ditemukan.")

    def hapus_kontak(self, nama):
        if nama in self.kontak:
            del self.kontak[nama]
            print(f"[SUCCESS] Kontak '{nama}' berhasil dihapus.")
        else:
            print(f"[ERROR] Kontak '{nama}' tidak ditemukan, gagal menghapus!")


# --- SIMULASI PENGUJIAN ---
if __name__ == "__main__":
    app = BukuTelepon()

    print("=== Uji Defect 1: Validasi Nomor HP ===")
    app.tambah_kontak("Budi", "081234abcd!!")  

    print("\n=== Uji Defect 2: Mencegah Overwrite ===")
    app.tambah_kontak("Andi", "08111111111")
    app.tambah_kontak("Andi", "08999999999") 

    print("\n=== Uji Defect 3: Pencarian Case-Insensitive ===")
    app.tambah_kontak("Siti Aminah", "08555555555")
    app.cari_kontak("siti")