from googletrans import Translator

translator = Translator()

def translate_text(text, source='auto', target='en'):
    try:
        translation = translator.translate(text, src=source, dest=target)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text  # Return original text if translation fails