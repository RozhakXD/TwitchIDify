# TwitchIDify 🎮
![TwitchIDify](https://github.com/user-attachments/assets/822bc92a-962e-4943-9d50-9a6dd9db4411)

**TwitchIDify** adalah solusi praktis untuk mencari informasi ID dan jumlah pengikut dari akun Twitch. Dengan memasukkan username, pengguna dapat langsung memperoleh detail tersebut dalam tampilan yang bersih dan responsif di perangkat apapun.

## 🚀 Fitur
- **Cari ID Pengguna Twitch**: Dapatkan ID pengguna hanya dengan memasukkan username.
- **Jumlah Pengikut**: Tampilkan jumlah pengikut pengguna yang ditemukan dalam format angka yang mudah dibaca.
- **Notifikasi Dinamis**: Notifikasi mengambang di pojok kanan atas untuk memberi tahu apakah pengguna ditemukan atau tidak.
- **Tampilan Responsif**: Desain modern dan responsif yang kompatibel di berbagai perangkat.

## 🌐 Akses Website
Anda dapat mengakses aplikasi ini secara online melalui URL berikut:

- [TwitchIDify](https://twitchidify.rozhak-dev.my.id/)

## 🔧 Instalasi
1. Clone repositori ini:
    ```bash
    git clone https://github.com/RozhakXD/TwitchIDify.git
    cd TwitchIDify
    ```
2. Pastikan Python dan Flask sudah terinstall di sistem Anda.
3. Install semua ketergantungan Python:
    ```bash
    pip install -r requirements.txt
    ```
4. Jalankan aplikasi Flask:
    ```bash
    python run.py
    ```

## 🛠️ Teknologi yang Digunakan
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Library**: Fetch API untuk komunikasi asinkron dengan backend

## 📸 Cuplikan Layar
![TwitchIDify Results](https://github.com/user-attachments/assets/55e8bb29-5ee7-4ead-a08b-e37687908e1c)

## 📖 Penggunaan
1. Masukkan username Twitch pada kolom input di halaman utama.
2. Klik Dapatkan ID untuk memulai pencarian.
3. Jika pengguna ditemukan, ID pengguna dan Jumlah pengikut akan ditampilkan.
4. Notifikasi akan muncul di pojok kanan atas untuk memberi tahu apakah pengguna ditemukan atau tidak.

## 💡 Catatan Penting
1. Pastikan koneksi internet stabil untuk mengambil data dari API Twitch (jika memerlukan integrasi API asli).
2. Endpoint `/api/twitch/{username}` harus berfungsi dengan baik di backend agar frontend dapat menerima data.

## ☕ Dukungan
Jika Anda menikmati proyek ini dan ingin memberikan dukungan, Anda bisa berdonasi melalui link berikut:

- [Trakteer](https://trakteer.id/rozhak_official/tip)
- [PayPal](https://paypal.me/rozhak9)
- [Saweria](https://saweria.co/rozhak9)

## 📜 Lisensi
Proyek ini dilisensikan di bawah MIT License - silakan lihat [LICENSE](https://github.com/RozhakXD/TwitchIDify/blob/main/LICENSE) untuk lebih jelasnya.
