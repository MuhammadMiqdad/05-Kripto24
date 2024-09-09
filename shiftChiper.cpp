// NAMA  : Muhammad Miqdad A.J
// NPM   : 140810220005
// KELAS : A

#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

// Fungsi untuk enkripsi teks menggunakan Shift Cipher
string encrypt_shift(const string &text, int s) {
    string result = "";
    for (size_t i = 0; i < text.length(); i++) {
        char charac = text[i];
        if (isupper(charac)) {
            result += char(((charac - 'A' + s) % 26) + 'A'); // Enkripsi huruf kapital
        } else if (islower(charac)) {
            result += char(((charac - 'a' + s) % 26) + 'a'); // Enkripsi huruf kecil
        } else {
            result += charac; // Karakter non-huruf tidak diubah
        }
    }
    return result;
}

// Fungsi untuk dekripsi teks menggunakan Shift Cipher
string decrypt_shift(const string &cipher, int s) {
    string result = "";
    for (size_t i = 0; i < cipher.length(); i++) {
        char charac = cipher[i];
        if (isupper(charac)) {
            result += char(((charac - 'A' - s + 26) % 26) + 'A'); // Dekripsi huruf kapital
        } else if (islower(charac)) {
            result += char(((charac - 'a' - s + 26) % 26) + 'a'); // Dekripsi huruf kecil
        } else {
            result += charac; // Karakter non-huruf tidak diubah
        }
    }
    return result;
}

// Fungsi untuk enkripsi file menggunakan Shift Cipher
void encrypt_file(const string &input_file, const string &output_file, int s) {
    ifstream input_f(input_file);
    ofstream output_f(output_file);
    string line;

    while (getline(input_f, line)) {
        output_f << encrypt_shift(line, s) << endl;
    }

    input_f.close();
    output_f.close();
}

// Fungsi untuk dekripsi file menggunakan Shift Cipher
void decrypt_file(const string &input_file, const string &output_file, int s) {
    ifstream input_f(input_file);
    ofstream output_f(output_file);
    string line;

    while (getline(input_f, line)) {
        output_f << decrypt_shift(line, s) << endl;
    }

    input_f.close();
    output_f.close();
}

// Fungsi untuk menampilkan menu
void menu() {
    cout << "\nMenu:" << endl;
    cout << "1. Enkripsi Teks" << endl;
    cout << "2. Dekripsi Teks" << endl;
    cout << "3. Enkripsi File" << endl;
    cout << "4. Dekripsi File" << endl;
    cout << "5. Keluar" << endl;
}

// Fungsi utama
int main() {
    while (true) {
        menu();
        string pilihan;
        cout << "Masukkan pilihan (1-5): ";
        cin >> pilihan;

        if (pilihan == "1") {
            string text;
            int s;
            cout << "Masukkan teks yang ingin dienkripsi: ";
            cin.ignore();
            getline(cin, text);
            cout << "Masukkan key (angka shift): ";
            cin >> s;
            string encrypted_text = encrypt_shift(text, s);
            cout << "Teks terenkripsi: " << encrypted_text << endl;
        } else if (pilihan == "2") {
            string text;
            int s;
            cout << "Masukkan teks yang ingin didekripsi: ";
            cin.ignore();
            getline(cin, text);
            cout << "Masukkan key (angka shift): ";
            cin >> s;
            string decrypted_text = decrypt_shift(text, s);
            cout << "Teks terdekripsi: " << decrypted_text << endl;
        } else if (pilihan == "3") {
            string input_file, output_file;
            int s;
            cout << "Masukkan nama file input: ";
            cin >> input_file;
            cout << "Masukkan nama file output: ";
            cin >> output_file;
            cout << "Masukkan key (angka shift): ";
            cin >> s;
            encrypt_file(input_file, output_file, s);
            cout << "File " << input_file << " telah dienkripsi menjadi " << output_file << endl;
        } else if (pilihan == "4") {
            string input_file, output_file;
            int s;
            cout << "Masukkan nama file input: ";
            cin >> input_file;
            cout << "Masukkan nama file output: ";
            cin >> output_file;
            cout << "Masukkan key (angka shift): ";
            cin >> s;
            decrypt_file(input_file, output_file, s);
            cout << "File " << input_file << " telah didekripsi menjadi " << output_file << endl;
        } else if (pilihan == "5") {
            cout << "Keluar Program !!!" << endl;
            break;
        } else {
            cout << "Pilihan tidak valid. Silakan coba lagi." << endl;
        }
    }

    return 0;
}
