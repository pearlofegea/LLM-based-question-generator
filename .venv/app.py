import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from prompt_builder import build_prompt
from validator import parse_json_response, validate_questions

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY bulunamadı. .env dosyanı kontrol et.")

client = genai.Client(api_key=GEMINI_API_KEY)

BASE_DIR = Path(__file__).resolve().parent


def read_text_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
    return path.read_text(encoding="utf-8")


def save_questions(data, output_path: str):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def soru_uret(metin: str, soru_sayisi: int = 5, zorluk: str = "orta", soru_tipi: str = "çoktan seçmeli"):
    prompt = build_prompt(
        metin=metin,
        soru_sayisi=soru_sayisi,
        zorluk=zorluk,
        soru_tipi=soru_tipi
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    response_text = response.text.strip()
    data = parse_json_response(response_text)
    validate_questions(data)
    return data


def main():
    input_file = BASE_DIR / "sample_texts" / "biyoloji.html"
    output_file = BASE_DIR / "outputs" / "sorular.json"

    metin = read_text_file(str(input_file))
    sorular = soru_uret(metin, soru_sayisi=5, zorluk="orta", soru_tipi="çoktan seçmeli")
    save_questions(sorular, str(output_file))

    print("Sorular başarıyla üretildi.")
    print(f"Kayıt yeri: {output_file}")

    for i, soru in enumerate(sorular, start=1):
        print(f"\nSoru {i}: {soru['soru']}")
        print(f"A) {soru['A']}")
        print(f"B) {soru['B']}")
        print(f"C) {soru['C']}")
        print(f"D) {soru['D']}")
        print(f"Doğru Cevap: {soru['dogru_cevap']}")
        print(f"Açıklama: {soru['aciklama']}")


if __name__ == "__main__":
    main()