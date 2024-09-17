# NAMA  : Muhammad Miqdad A.J
# NPM   : 140810220005
# KELAS : A

import numpy as np
import math

# Fungsi untuk mengubah huruf menjadi angka
def huruf_ke_angka(huruf):
    return ord(huruf.upper()) - ord('A')

# Fungsi untuk mengubah angka menjadi huruf
def angka_ke_huruf(angka):
    return chr(angka + ord('A'))

# Fungsi enkripsi Hill Cipher
def enkripsi_hill(plaintext, kunci):
    # Ubah plaintext menjadi angka
    angka_pt = [huruf_ke_angka(h) for h in plaintext]
    
    ukuran_matriks = len(kunci)
    if len(angka_pt) % ukuran_matriks != 0:
        angka_pt += [huruf_ke_angka('X')] * (ukuran_matriks - len(angka_pt) % ukuran_matriks)  # Padding
    
    # Pisahkan dalam blok-blok matriks Nx1 (sesuai dengan ukuran matriks kunci)
    blok = [angka_pt[i:i+ukuran_matriks] for i in range(0, len(angka_pt), ukuran_matriks)]
    
    # Enkripsi setiap blok dengan matriks kunci
    hasil = []
    for b in blok:
        b = np.array(b).reshape(ukuran_matriks, 1)
        e = np.dot(kunci, b) % 26  # modulo 26 (jumlah huruf alfabet)
        hasil.append(e.flatten())
    
    # Ubah hasil enkripsi menjadi huruf
    hasil_akhir = ''.join([angka_ke_huruf(int(i)) for blok in hasil for i in blok])
    return hasil_akhir

# Fungsi untuk menghitung invers matriks modulo 26
def invers_matriks_modulo(matriks, mod):
    determinan = int(np.round(np.linalg.det(matriks)))
    print(f"Determinan matriks: {determinan}")  # Debug print

    # Cek apakah GCD dari determinan dan 26 adalah 1 (harus relatif prima)
    if math.gcd(determinan, mod) != 1:
        raise ValueError(f"Determinan {determinan} tidak memiliki invers modulo {mod}, kunci tidak valid.")
    
    invers_det = pow(determinan, -1, mod)  # Invers determinan modulo 26
    adjugate = np.round(np.linalg.inv(matriks) * determinan).astype(int) % mod
    return (invers_det * adjugate) % mod

# Fungsi dekripsi Hill Cipher
def dekripsi_hill(ciphertext, kunci):
    # Ubah ciphertext menjadi angka
    angka_ct = [huruf_ke_angka(h) for h in ciphertext]
    
    # Pisahkan dalam blok-blok matriks Nx1
    ukuran_matriks = len(kunci)
    blok = [angka_ct[i:i+ukuran_matriks] for i in range(0, len(angka_ct), ukuran_matriks)]
    
    # Invers matriks kunci
    kunci_invers = invers_matriks_modulo(kunci, 26)
    
    # Dekripsi setiap blok dengan matriks kunci invers
    hasil = []
    for b in blok:
        b = np.array(b).reshape(ukuran_matriks, 1)
        d = np.dot(kunci_invers, b) % 26
        hasil.append(d.flatten())
    
    # Ubah hasil dekripsi menjadi huruf
    hasil_akhir = ''.join([angka_ke_huruf(int(i)) for blok in hasil for i in blok])
    return hasil_akhir

# Fungsi untuk menerima input matriks kunci dari pengguna
def input_kunci(ukuran):
    print(f"Masukkan elemen-elemen matriks kunci ({ukuran}x{ukuran}):")
    kunci = []
    for i in range(ukuran):
        baris = []
        for j in range(ukuran):
            elemen = int(input(f"Elemen [{i+1},{j+1}]: "))
            baris.append(elemen)
        kunci.append(baris)
    return np.array(kunci)

# Fungsi untuk mencari kunci dari Hill Cipher
def cari_kunci(plaintext, ciphertext, ukuran):
    # Ubah plaintext dan ciphertext menjadi angka
    angka_pt = [huruf_ke_angka(h) for h in plaintext]
    angka_ct = [huruf_ke_angka(h) for h in ciphertext]
    
    # Periksa apakah panjang plaintext dan ciphertext sama
    if len(angka_pt) != len(angka_ct):
        print("Panjang plaintext dan ciphertext harus sama!")
        return

    P = np.array([[angka_pt[0], angka_pt[2]], [angka_pt[1], angka_pt[3]]])
    C = np.array([[angka_ct[0], angka_ct[2]], [angka_ct[1], angka_ct[3]]])
    
    try:
        # Cari invers matriks plaintext dan hitung kunci
        P_inv = invers_matriks_modulo(P, 26)
        kunci = np.dot(C, P_inv) % 26
        print("Matriks Kunci:")
        print(kunci)
    except ValueError as e:
        print(e)

# Fungsi utama untuk menampilkan menu
def menu():
    while True:
        print("\n=== Hill Cipher ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Kunci")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            # Enkripsi
            ukuran = int(input("Masukkan ukuran matriks (contoh: 2 untuk 2x2, dst): "))
            kunci = input_kunci(ukuran)
            plaintext = input("Masukkan plaintext (huruf A-Z): ").upper()
            ciphertext = enkripsi_hill(plaintext, kunci)
            print(f"Ciphertext: {ciphertext}")
        
        elif pilihan == "2":
            # Dekripsi
            ukuran = int(input("Masukkan ukuran matriks (contoh: 2 untuk 2x2, dst): "))
            kunci = input_kunci(ukuran)
            ciphertext = input("Masukkan ciphertext (huruf A-Z): ").upper()
            plaintext = dekripsi_hill(ciphertext, kunci)
            print(f"Plaintext: {plaintext}")
        
        elif pilihan == "3":
            # Cari kunci
            plaintext = input("Masukkan plaintext (huruf A-Z, sesuai ukuran matriks): ").upper()
            ciphertext = input("Masukkan ciphertext (huruf A-Z, sesuai ukuran matriks): ").upper()
            ukuran = int(input("Masukkan ukuran matriks (contoh: 2 untuk 2x2, dst): "))
            cari_kunci(plaintext, ciphertext, ukuran)
        
        elif pilihan == "4":
            # Keluar
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Main Program
if __name__ == "__main__":
    menu()