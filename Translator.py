import json
from googletrans import Translator
from tqdm import tqdm  # Importa la librería tqdm para la barra de progreso

def translate_values(json_data, input_language, target_language):
    translator = Translator()
    translated_data = {}

    for key, value in tqdm(json_data.items(), desc="Traduciendo", ncols=100):
        translation = translator.translate(value, src=input_language, dest=target_language)
        translated_data[key] = translation.text

    return translated_data

if __name__ == "__main__":  
    input_file = "input.json"  # Nombre de tu archivo JSON de entrada
    target_language = "ru"  # Código del idioma objetivo (ejemplo: "es" para español)
    input_language = "zh-cn" # Código del idioma input (ejemplo: "zh-cn" para chino)

    with open(input_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    translated_data = translate_values(json_data, input_language, target_language)

    output_file = f"output_{target_language}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

    print("Traducción completada y guardada en", output_file)
