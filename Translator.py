import os
import json
import translators as ts
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed


def translate_value(key_value, input_language, target_language):
    key, value = key_value
    try:
        translation = ts.translate_text(
            value, from_language=input_language, to_language=target_language
        )
        return key, translation
    except Exception as e:
        print(f"[ERROR] Translating '{value}' to {target_language}: {e}")
        return key, value  # Return the original value in case of an error


def translate_values(json_data, input_language, target_language):
    translated_data = {}

    with ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(
                translate_value, (key, value), input_language, target_language
            ): key
            for key, value in json_data.items()
        }

        for future in tqdm(
            as_completed(futures),
            total=len(futures),
            desc=f"Translating to {target_language}",
            ncols=100,
        ):
            key, translation = future.result()
            translated_data[key] = translation

    return translated_data


if __name__ == "__main__":
    # Config
    input_file = "en_US.json"
    input_language = "en"
    output_folder = "./i18n/"
    target_languages = [
        "zh-cn",
        "en",
        "ar",
        "ru",
        "fr",
        "de",
        "es",
        "pt",
        "it",
        "ja",
        "ko",
        "el",
        "nl",
        "hi",
        "tr",
        "ms",
        "th",
        "id",
        "he",
        "pl",
        "cs",
        "hu",
        "fa",
        "bs",
        "fj",
        "ht",
        "ca",
        "hr",
        "lv",
        "lt",
        "ur",
        "uk",
        "c",
        "to",
        "sw",
        "sm",
        "sk",
        "af",
        "bn",
        "mg",
        "mt",
        "otq",
        "gu",
        "ta",
        "te",
        "pa",
        "am",
        "az",
        "ba",
        "be",
        "ceb",
        "cv",
        "eu",
        "ga",
    ]

    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    os.makedirs(output_folder, exist_ok=True)

    for target_language in target_languages:
        translated_data = translate_values(json_data, input_language, target_language)

        output_file = os.path.join(output_folder, f"{target_language}_{target_language.upper()}.json")
        
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)

        print(f"Translation to {target_language} completed and saved to {output_file}")
