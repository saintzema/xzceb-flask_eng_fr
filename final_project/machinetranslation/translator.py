"""Module to Translate English & French"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""Function to translate English to French"""
def english_to_french(english_text):
    authenticator = IAMAuthenticator('{apikey}')
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

    language_translator.set_service_url('{url}')

    french_text = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-fr').get_result()

    print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french_text

"""Function to translate French to English"""
def french_to_english(french_text):
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

    language_translator.set_service_url(url)

    english_text = language_translator.translate(
    text='Bonjour',
    model_id='fr-en').get_result()

    print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return english_text
