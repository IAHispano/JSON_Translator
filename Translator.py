import json
from googletrans import Translator
from tqdm import tqdm
import os

def translate_values(json_data, input_language, target_language):
    translator = Translator()
    translated_data = {}

    for key, value in tqdm(json_data.items(), desc=f"Translating to {target_language}", ncols=100):
        try:
            translation = translator.translate(value, src=input_language, dest=target_language)
            translated_data[key] = translation.text
        except Exception as e:
            print(f"[ERROR] Translating '{value}' to {target_language}: {e}")

    return translated_data

if __name__ == "__main__":
    input_file = "es_ES.json"  # Name of your input JSON file
    input_language = "es"  # Input language code (e.g., "zh-cn" for Chinese)
    target_languages = ["en", "zh-cn", "es", "hi", "ar", "bn", "pt", "ru", "ja", "pa", "de", "jv", "ms", "wu", "te",
                   "vi", "ko", "fr", "mr", "ta", "ur", "tr", "it", "th", "gu", "fa", "pl", "uk", "ro", "nl", "hu"]

    # Add more language codes as needed

    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    for target_language in target_languages:
        translated_data = translate_values(json_data, input_language, target_language)

        output_folder = "./output"
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

        output_file = f"{output_folder}/{target_language}_{target_language.upper()}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(translated_data, f, ensure_ascii=False, indent=2)

        print(f"Translation to {target_language} completed and saved to {output_file}")
