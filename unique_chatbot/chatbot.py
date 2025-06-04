"""Contoh chatbot sederhana dengan fokus solusi.

Script ini hanyalah kerangka awal. Anda dapat memperluas fungsionalitasnya
menggunakan model bahasa open source maupun layanan API yang relevan.
"""

import random

# Daftar contoh permasalahan dan jawaban sederhana
PROBLEMS = {
    "lingkungan": [
        "Kurangi penggunaan plastik sekali pakai dan mulai program daur ulang lokal.",
        "Pertimbangkan menggunakan energi terbarukan seperti panel surya."],
    "kesehatan": [
        "Biasakan pola makan seimbang dan olahraga teratur.",
        "Lakukan pemeriksaan kesehatan rutin untuk deteksi dini."],
    "bisnis": [
        "Optimalkan alur kerja dengan alat otomasi yang sesuai kebutuhan.",
        "Analisis pasar untuk menemukan ceruk pelanggan potensial."]
}

def respond_to_query(topic: str) -> str:
    """Berikan jawaban acak berdasarkan topik."""
    topic = topic.lower()
    if topic in PROBLEMS:
        return random.choice(PROBLEMS[topic])
    return "Maaf, topik tersebut belum didukung."

def main():
    print("SentientOps Chatbot - Mode Percakapan Sederhana")
    print("Ketik 'keluar' untuk menghentikan.")
    while True:
        user_input = input("Anda: ").strip()
        if user_input.lower() == "keluar":
            break
        response = respond_to_query(user_input)
        print("Bot :", response)

if __name__ == "__main__":
    main()
