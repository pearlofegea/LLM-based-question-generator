def build_prompt(metin: str, soru_sayisi: int = 5, zorluk: str = "orta", soru_tipi: str = "çoktan seçmeli") -> str:
    return f"""
Sen deneyimli bir Türk öğretmensin.

Görevin:
Aşağıdaki metne dayanarak Türkçe, kaliteli ve açık {soru_sayisi} adet {soru_tipi} soru üretmek.

Kurallar:
- Sorular sadece verilen metne dayanmalı.
- Metinde olmayan bilgi ekleme.
- Her sorunun yalnızca 1 doğru cevabı olmalı.
- Her soru 4 şıklı olmalı: A, B, C, D
- Şıklar mantıklı ve birbirine yakın olmalı.
- Sorular {zorluk} zorluk seviyesinde olmalı.
- Sorular açık, net ve sınav diliyle yazılmalı.
- Her soru için kısa bir açıklama yaz.
- Çıktıyı sadece geçerli JSON olarak ver.
- JSON dışında hiçbir metin yazma.

Çıktı formatı tam olarak şöyle olmalı:
{{
  "sorular": [
    {{
      "soru": "Soru metni",
      "A": "A şıkkı",
      "B": "B şıkkı",
      "C": "C şıkkı",
      "D": "D şıkkı",
      "dogru_cevap": "A",
      "aciklama": "Kısa açıklama"
    }}
  ]
}}

Metin:
{metin}
""".strip()