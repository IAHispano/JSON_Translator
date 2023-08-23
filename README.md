# JSON Translator Script

This script is designed to translate values from a JSON file to multiple target languages using the Google Translate API. It utilizes the `googletrans` library for translation and provides an easy way to translate content across different languages.

## Features

- Translates values from a JSON file to multiple target languages.
- Handles errors and displays them for easy debugging.
- Creates a separate JSON file for each target language with translated content.
- Automatically creates the output folder if it doesn't exist.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python (version 3.6 or later)
- Required Python packages (install using `pip`):
  - `googletrans`
  - `tqdm`

## Usage

1. Place your input JSON file (e.g., `es_ES.json`) in the same directory as the script.
2. Configure the script by modifying the following variables in the script:
   - `input_file`: Name of your input JSON file.
   - `input_language`: Language code of the input content (e.g., "es" for Spanish).
   - `target_languages`: List of target language codes you want to translate to.
3. Open a terminal/command prompt and navigate to the script directory.
4. Run the script using the command:
python script_name.py
Replace `script_name.py` with the actual name of your script.
5. The translated JSON files will be saved in the `output` folder.

## Notes

- Keep in mind that the Google Translate API might have usage limitations and restrictions, especially if used extensively.
- Make sure to handle any API usage limits or authentication requirements according to the `googletrans` documentation.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This script was inspired by the need to translate content efficiently across languages.
- Thanks to the developers of `googletrans` and `tqdm` for their useful libraries.

Feel free to contribute, report issues, or suggest improvements!
