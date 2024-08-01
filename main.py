meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetuhuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
     
else:
    print("kata kunci tidak ditemukan")
