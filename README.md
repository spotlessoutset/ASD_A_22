# Kelompok22-TPLA
Struktur Organisasi Kelas
# 🏫 Class Organization Structure (Tree CLI)
Aplikasi berbasis **Command Line Interface (CLI)** sederhana untuk mengelola struktur organisasi kelas menggunakan konsep struktur data **Tree (Pohon)** di Python. Aplikasi ini mendukung penambahan, penghapusan, pencarian, pembaruan data anggota, penyimpanan ke file JSON, serta riwayat penghapusan anggota.
Jangan biarkan hierarki organisasi kelasmu berantakan seperti kabel earphone di dalam saku! Tatap masa depan kelas yang lebih terstruktur dengan aplikasi ini. 😎

---

## ✨ Fitur Utama
Aplikasi ini dilengkapi dengan operasi dasar *Tree* yang telah disesuaikan untuk manajemen organisasi:
* **Buat & Load Struktur:** Mulai dari awal dengan ketua baru atau muat data lama dari file `data.json`.
* **Tampilkan Struktur:** Visualisasi hierarki organisasi dalam bentuk diagram teks rekursif (`|_`).
* **Tambah Anggota:** Menyisipkan anggota baru sebagai bawahan langsung dari atasan tertentu.
* **Hapus Anggota:** Menghapus anggota dari struktur (sekaligus menghapus seluruh bawahan di bawahnya secara otomatis).
* **Update Data Anggota:** Mengubah nama atau jabatan anggota tanpa merusak struktur hierarki yang sudah ada.
* **Cari Detail Anggota:** Melihat informasi nama, jabatan, serta siapa saja bawahan langsung dari anggota tersebut.
* **Penyimpanan JSON:** Simpan progres struktur kelas Anda kapan saja ke file `data.json`.
* **Riwayat Hapus (Baru!):** Menyimpan 5 operasi penghapusan terakhir beserta seluruh subtree-nya untuk referensi.

---

## 🚀 Cara Menjalankan
### Prasyarat
Pastikan Anda sudah menginstal Python di komputer Anda (versi 3.x direkomendasikan). Aplikasi ini hanya menggunakan modul bawaan (`json`, `collections`), jadi tidak perlu menginstal *library* pihak ketiga tambahan.
### Langkah-langkah
1. **Clone repositori ini** ke komputer Anda:
```bash
git clone https://github.com/spotlessoutset/ASD_A_22.git
cd ASD_A_22
```
2. **Jalankan aplikasi** melalui terminal/command prompt:
```bash
python main.py
```

---

## 📖 Pratinjau Menu Utama
Saat menjalankan aplikasi, Anda akan disuguhkan menu interaktif seperti berikut:
```text
=============================================
========= Struktur Organisasi Kelas =========
=============================================
 1. Tampilkan Struktur Organisasi
 2. Tambah Anggota
 3. Hapus Anggota
 4. Update Data Anggota
 5. Cari Anggota
 6. Simpan Struktur
 7. Load Struktur
 8. Tampilkan Riwayat Hapus
 0. Keluar
=============================================
```
### Contoh Visualisasi Struktur:
```text
Budi (Ketua Kelas)
  |_ Siti (Sekretaris)
  |_ Andi (Bendahara)
    |_ Joko (Seksi Kebersihan)
```
### Contoh Visualisasi Riwayat Hapus:
```text
===5 Anggota Terakhir yang Dihapus===
1.
Andi (Bendahara)
    |_ Joko (Seksi Kebersihan)
```

---

## 🛠️ Konsep Struktur Data
Aplikasi ini menggunakan representasi **General Tree** di mana:
* `Class Anggota` bertindak sebagai **Node**, menyimpan data berupa `nama`, `jabatan`, dan *list* `bawahan` (anak pohon).
* `Class Struktur` bertindak sebagai pengelola pohon (*Tree Manager*), yang menangani algoritma pencarian mendalam (**Depth-First Search**) secara rekursif untuk menemukan atasan atau bawahan.
* `Class Riwayat` bertindak sebagai **deletion history**, menyimpan 5 operasi hapus terakhir menggunakan `deque` dengan `maxlen=5`. Setiap entri menyimpan snapshot lengkap dari node yang dihapus beserta seluruh subtree-nya.

> ⚠️ **Catatan Penting:** Penghapusan Ketua Kelas (Root Node) dibatasi di dalam menu hapus biasa demi menjaga agar struktur pohon tidak rusak total.

---

## 🤝 Kontribusi
Punya ide untuk menambahkan fitur visualisasi berbasis grafis atau fitur menarik lainnya? *Pull Request* selalu terbuka untuk siapa saja!
1. *Fork* Repositori ini
2. Buat *Branch* baru (`git checkout -b fitur-keren`)
3. *Commit* perubahan Anda (`git commit -m 'Menambahkan fitur keren'`)
4. *Push* ke *Branch* tersebut (`git push origin fitur-keren`)
5. Buat *Pull Request* baru
