# Photo Sorter

Photo Sorter adalah aplikasi berbasis Python menggunakan Tkinter untuk menyortir foto dalam jumlah banyak dengan cara yang mudah dan cepat.

## Fitur

- Menampilkan foto dari folder utama.
- Memindahkan foto ke salah satu dari lima folder yang telah ditentukan.
- Menghapus foto dengan memindahkannya ke folder khusus "deleted".
- Navigasi otomatis ke foto berikutnya setelah aksi dilakukan.

## Instalasi

1. Pastikan Python sudah terinstall di sistem Anda.
2. Install dependensi yang dibutuhkan:
   ```bash
   pip install pillow
   ```
3. Buat folder utama untuk menyimpan foto yang akan disortir:
   ```
   photos/  (letakkan foto-foto di sini)
   ```
4. Jalankan aplikasi dengan perintah:
   ```bash
   python main.py
   ```

## Cara Penggunaan

1. Masukkan semua foto yang ingin disortir ke dalam folder `photos`.
2. Jalankan program.
3. Foto pertama akan ditampilkan di aplikasi.
4. Gunakan tombol:
   - **Delete** untuk menghapus foto (memindahkannya ke folder `deleted`).
   - **Folder 1 - Folder 5** untuk memindahkan foto ke folder yang sesuai.
5. Setelah tombol ditekan, aplikasi otomatis menampilkan foto berikutnya.
6. Lanjutkan proses hingga semua foto tersortir.

## Struktur Folder

```
photo_sorter/
├── main.py
├── photos/  # Folder utama berisi foto yang belum disortir
├── folder1/  # Folder tujuan 1
├── folder2/  # Folder tujuan 2
├── folder3/  # Folder tujuan 3
├── folder4/  # Folder tujuan 4
├── folder5/  # Folder tujuan 5
└── deleted/  # Folder untuk foto yang dihapus
```


