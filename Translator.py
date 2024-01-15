import json
import translators as ts
from tqdm import tqdm
import os


def translate_values(json_data, input_language, target_language):
    translated_data = {}

    for key, value in tqdm(
        json_data.items(), desc=f"Translating to {target_language}", ncols=100
    ):
        try:
            translation = ts.translate_text(
                value, from_language=input_language, to_language=target_language
            )
            translated_data[key] = translation
        except Exception as e:
            print(f"[ERROR] Translating '{value}' to {target_language}: {e}")

    return translated_data


if __name__ == "__main__":
    # Config
    input_file = "en_US.json"
    input_language = "en"
    output_folder = "./i18n/"
    target_languages = [
        "es",
        "zh-cn",
        "hi",
        "ar",
        "bn",
        "pt",
        "pr-br",
        "ru",
        "ja",
        "pa",
        "de",
        "jv",
        "ms",
        "wu",
        "te",
        "vi",
        "ko",
        "fr",
        "mr",
        "ta",
        "ur",
        "tr",
        "it",
        "th",
        "gu",
        "fa",
        "pl",
        "uk",
        "ro",
        "nl",
        "hu",
    ]

    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for target_language in target_languages:
        translated_data = translate_values(json_data, input_language, target_language)

        os.makedirs(output_folder, exist_ok=True)

        output_file = (
            f"{output_folder}/{target_language}_{target_language.upper()}.json"
        )
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)

        print(f"Translation to {target_language} completed and saved to {output_file}")
