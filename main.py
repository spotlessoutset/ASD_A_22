# =============================================
# STRUKTUR ORGANISASI KELAS
# KELOMPOK  : 22
# ANGGOTA   : 1. Ibra Arifa Istara
#             2. Ayyash Syauqi Syahadah
#             3. Muhammad Adiyoga Danendra
# =============================================

from collections import deque
import json

# Mengubah objek Anggota menjadi dictionary
def anggota_ke_dict(node):
    return {
        "nama": node.nama,
        "jabatan": node.jabatan,
        "bawahan": [anggota_ke_dict(b) for b in node.bawahan]
    }

# Mengubah dictionary kembali menjadi objek Anggota
def dict_ke_anggota(data):
    node = Anggota(data["nama"], data["jabatan"])
    node.bawahan = [dict_ke_anggota(b) for b in data["bawahan"]]
    return node

# 5.
# Menyimpan struktur ke file JSON
def simpan_file(organisasi):
    if organisasi.root is None:
        print("Tidak ada data untuk disimpan.")
        return
    
    data = anggota_ke_dict(organisasi.root)
    
    try:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Struktur berhasil disimpan ke 'data.json'")
    except Exception as e:
        print("Terjadi kesalahan saat menyimpan:", e)

# 6.
# Membuka struktur dari file JSON
def buka_file(organisasi):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        
        organisasi.root = dict_ke_anggota(data)
        print("Struktur berhasil dimuat dari 'data.json'")
        return True
    except FileNotFoundError:
        print("File tidak ditemukan!")
    except Exception as e:
        print("Terjadi kesalahan saat memuat:", e)
        return False

# ==========================================
# Class Node
# ==========================================

# Merepresentasikan satu anggota dalam struktur organisasi.
class Anggota:
    # Inisialisasi anggota dengan nama, jabatan, dan list bawahan kosong
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.bawahan = []

# ==========================================
# Class Riwayat
# ==========================================

# Menampilkan 5 anggota terakhir yang dihapus
class Riwayat:
    def __init__(self):
        self.queue = deque(maxlen=5)

    def tambah(self, node):
        self.queue.appendleft(anggota_ke_dict(node))

    def tampilkan(self):
        if not self.queue:
            print("Belum ada anggota yang dihapus.")
            return
    
        # Reukursif buat nampilin node beserta seluruh bawahannya
        def tampilkan_node(data, tingkat=0): 
            indentasi = "    " * tingkat + ("|_ " if tingkat > 0 else "")
            print(f"{indentasi}{data['nama']} ({data['jabatan']})")
            for bawahan in data['bawahan']:
                tampilkan_node(bawahan, tingkat + 1)
    
        print("\n===5 Anggota Terakhir yang Dihapus===")
        for i, data in enumerate(self.queue, 1):
            print(f"{i}.")
            tampilkan_node(data)

# ==========================================
# Class Struktur Data
# ========================================== 

# Mengelola struktur organisasi kelas berbasis tree.
class Struktur:
    # Inisialisasi tree dengan root Ketua Kelas
    def __init__(self, nama_ketua):
        if nama_ketua:
            self.root = Anggota(nama_ketua, "Ketua Kelas")
        else:
            self.root = None

    # 1.
    # Menampilkan seluruh struktur organisasi secara rekursif
    def tampilkan_struktur(self, node=None, tingkat=0):
        if self.root is None:
            print("Struktur organisasi kosong.")
            return
            
        if node is None and tingkat == 0:
            node = self.root

        indentasi = "  " * tingkat + ("|_ " if tingkat > 0 else "")
        print(f"{indentasi}{node.nama} ({node.jabatan})")

        for bawahan in node.bawahan:
            self.tampilkan_struktur(bawahan, tingkat + 1)

    # Mencari node anggota berdasarkan nama secara rekursif
    def cari_bawahan(self, node, nama_target):
        if node is None:
            return None
        if node.nama.lower() == nama_target.lower():
            return node
            
        for bawahan in node.bawahan:
            hasil = self.cari_bawahan(bawahan, nama_target)
            if hasil:
                return hasil
        return None

    # Mencari node parent (atasan langsung) dari anggota
    def cari_parent(self, node, nama_target):
        if node is None:
            return None
        for bawahan in node.bawahan:
            if bawahan.nama.lower() == nama_target.lower():
                return node
            hasil = self.cari_parent(bawahan, nama_target)
            if hasil:
                return hasil
        return None

    # 2.
    # Menambahkan anggota baru sebagai bawahan dari atasan
    def tambah_anggota(self, nama_atasan, nama_baru, jabatan_baru):
        atasan = self.cari_bawahan(self.root, nama_atasan)
        if atasan:
            anggota_baru = Anggota(nama_baru, jabatan_baru)
            atasan.bawahan.append(anggota_baru)
            print(f"Berhasil menambahkan {nama_baru} sebagai {jabatan_baru}.")
        else:
            print(f"Gagal: Atasan dengan nama '{nama_atasan}' tidak ditemukan!")

    # 3.
    # Menghapus anggota beserta seluruh bawahannya dari struktur
    def hapus_anggota(self, nama_target, riwayat):
        if self.root is None:
            print("Struktur kosong.")
            return
        
        if self.root.nama.lower() == nama_target.lower():
            print("Peringatan: Tidak dapat menghapus Ketua Kelas dari sini!")
            return

        parent = self.cari_parent(self.root, nama_target)
        if parent:
            target_node = self.cari_bawahan(self.root, nama_target)
            riwayat.tambah(target_node)                              
            parent.bawahan = [b for b in parent.bawahan if b.nama.lower() != nama_target.lower()]
            print(f"Berhasil menghapus '{nama_target}' beserta seluruh bawahannya dari struktur.")
        else:
            print(f"Anggota dengan nama '{nama_target}' tidak ditemukan!")

    # 4.
    # Mengubah data anggota (nama dan/atau jabatan)
    def update_anggota(self, nama_target, nama_baru, jabatan_baru):
        anggota = self.cari_bawahan(self.root, nama_target)
        if anggota:
            nama_lama = anggota.nama
            # Jika input tidak kosong, perbarui datanya
            if nama_baru.strip():
                anggota.nama = nama_baru
            if jabatan_baru.strip():
                anggota.jabatan = jabatan_baru
            print(f"Berhasil memperbarui data '{nama_lama}'.")
        else:
            print(f"Anggota dengan nama '{nama_target}' tidak ditemukan!")

    # 5.
    # Mencari dan menampilkan detail informasi anggota
    def cari_anggota(self, nama_target):
        hasil = self.cari_bawahan(self.root, nama_target)
        if hasil:
            print(f"\n===Data Anggota===")
            print(f"Nama    : {hasil.nama}")
            print(f"Jabatan : {hasil.jabatan}")
            if hasil.bawahan:
                print("Bawahan:")
                for b in hasil.bawahan:
                    print(f" - {b.nama} ({b.jabatan})")
            else:
                print("Status  : Tidak memiliki bawahan.")
        else:
            print("Anggota tidak ditemukan.")

# Fungsi utama program, menampilkan menu dan menangani input user
def main():
    # Pilihan awal untuk membuat struktur baru atau memuat struktur sebelumnya
    print("\n--- Struktur Organisasi Kelas ---\n",
          "1. Buat Struktur Organisasi Baru\n",
          "2. Load Struktur Organisasi Sebelumnya\n",)
    
    pilihan = input("Masukkan pilihan: ")

    # Inisialisasi struktur baru
    if pilihan == "1":
        nama_ketua = input("Masukkan nama ketua kelas: ")
        organisasi = Struktur(nama_ketua)
        riwayat = Riwayat()

    # Load struktur dari file JSON
    elif pilihan == "2":
        organisasi = Struktur(None)
        riwayat = Riwayat()
        valid = buka_file(organisasi)
        if not valid:
            print("Silakan buat struktur organisasi baru sebagai gantinya.")
            nama_ketua = input("Masukkan nama ketua kelas: ")
            organisasi = Struktur(nama_ketua)
    else:
        print("Pilihan tidak valid!")
        return

    print("\n--- Struktur Organisasi Kelas ---")
    organisasi.tampilkan_struktur()
    while True:
        print("\n"
            "========= Struktur Organisasi Kelas =========\n",
            "1. Tampilkan Struktur Organisasi\n",
            "2. Tambah Anggota\n",
            "3. Hapus Anggota\n",
            "4. Update Anggota\n",
            "5. Cari Anggota\n",
            "6. Simpan Struktur\n",
            "7. Load Struktur\n",
            "8. Tampilkan Riwayat Hapus\n",
            "0. Keluar"
        )

        pilihan = input("Masukkan pilihan: ")


        # IF ELSE INPUT USER

        if pilihan == "1":
            organisasi.tampilkan_struktur()
        elif pilihan == "2":
            nama_atasan = input("Masukkan nama atasan: ")
            nama_baru = input("Masukkan nama anggota baru: ")
            jabatan_baru = input("Masukkan jabatan anggota baru: ")
            organisasi.tambah_anggota(nama_atasan, nama_baru, jabatan_baru)
        elif pilihan == "3":
            nama_target = input("Masukkan nama anggota yang ingin dihapus: ")
            organisasi.hapus_anggota(nama_target, riwayat)
        elif pilihan == "4":
            nama_target = input("Masukkan nama anggota yang ingin diubah: ")
            print("\n(Kosongkan dan tekan Enter pada bagian yang tidak ingin diubah)")
            nama_baru = input("Masukkan nama baru: ")
            jabatan_baru = input("Masukkan jabatan baru: ")
            organisasi.update_anggota(nama_target, nama_baru, jabatan_baru)
        elif pilihan == "5":
            nama_target = input("Masukkan nama anggota yang ingin dicari: ")
            organisasi.cari_anggota(nama_target)
        elif pilihan == "6":
            simpan_file(organisasi)
        elif pilihan == "7":
            buka_file(organisasi)
        elif pilihan == "8":
            riwayat.tampilkan()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
