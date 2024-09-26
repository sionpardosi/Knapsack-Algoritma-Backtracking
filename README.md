# Knapsack Problem with Backtracking

Diberikan sejumlah item dengan berat dan nilai tertentu, serta sebuah ransel dengan kapasitas tertentu. Tugas Anda adalah memilih item-item untuk dimasukkan ke dalam ransel sehingga nilai total item-item yang dipilih maksimal, tanpa melebihi kapasitas ransel.

## Batasan Tambahan:
1. Setiap item memiliki jumlah maksimal yang dapat dipilih.
2. Algoritma backtracking harus digunakan untuk menyelesaikan masalah ini. Tidak boleh menggunakan greedy algorithm.
3. Setiap kombinasi item yang memungkinkan harus dieksplorasi menggunakan backtracking.

## Input:
Sebuah daftar item, masing-masing item memiliki:
1. Berat (𝑤𝑖): Berat item ke-i.
2. Nilai (𝑣𝑖): Nilai item ke-i.
3. Jumlah maksimal (𝑚𝑖): Jumlah maksimal item ke-i yang bisa dipilih.
4. Kapasitas maksimal ransel (W).

## Soal:
Diberikan daftar 8 item berikut:

Kapasitas ransel (W): 20 kg.

## Tugas:
1. Tentukan kombinasi item yang bisa dipilih sehingga nilai total item maksimal tanpa melebihi kapasitas ransel 20 kg.
2. Tentukan berapa unit dari masing-masing item yang dipilih untuk mencapai nilai maksimal tersebut.

## Output:
- Kombinasi item dan jumlah yang dipilih.
- Nilai maksimum yang bisa didapatkan.

## Instruksi Penyelesaian Algoritma Backtracking:
- Eksplorasi semua kemungkinan kombinasi item. Untuk setiap item, pilih dari 0 hingga jumlah maksimal yang diperbolehkan.
- Setiap kali memilih suatu jumlah untuk item, periksa apakah kapasitas ransel melebihi batas. Jika melebihi, lakukan backtrack.
- Jika kapasitas tidak terlampaui, lanjutkan ke item berikutnya.
- Simpan solusi terbaik (nilai tertinggi) yang ditemukan selama proses eksplorasi.

## Langkah-langkah:
- Mulai dengan ransel kosong dan kapasitas 20 kg.
- Untuk setiap item, pilih antara 0 hingga jumlah maksimal item tersebut, cek apakah masih memungkinkan berdasarkan kapasitas ransel.
- Jika memungkinkan, tambahkan nilai item ke dalam ransel, dan periksa apakah nilai total lebih baik dari solusi sebelumnya.
- Jika kapasitas ransel terlampaui, kembalikan (backtrack) dan coba opsi lain.
- Setelah semua kombinasi dicoba, kembalikan kombinasi item yang memberikan nilai maksimal.
