import json


def parse_json_response(response_text: str):
    try:
        data = json.loads(response_text)
        if not isinstance(data, dict):
            raise ValueError("Çıktı bir JSON obje olmalı.")
        if "sorular" not in data:
            raise ValueError("JSON içinde 'sorular' alanı bulunamadı.")
        if not isinstance(data["sorular"], list):
            raise ValueError("'sorular' alanı bir liste olmalı.")
        return data["sorular"]
    except json.JSONDecodeError as e:
        raise ValueError(f"JSON parse hatası: {e}\n\nGelen cevap:\n{response_text}")


def validate_questions(data):
    required_fields = {"soru", "A", "B", "C", "D", "dogru_cevap", "aciklama"}

    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"{i}. soru bir obje değil.")

        missing = required_fields - set(item.keys())
        if missing:
            raise ValueError(f"{i}. soruda eksik alanlar var: {missing}")

        if item["dogru_cevap"] not in {"A", "B", "C", "D"}:
            raise ValueError(f"{i}. soruda dogru_cevap yalnızca A/B/C/D olabilir.")

    return True