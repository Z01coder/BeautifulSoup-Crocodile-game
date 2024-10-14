import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса

        soup = BeautifulSoup(response.content, features="html.parser")
        english_words = soup.find(name="div", id="random_word").text.strip()
        word_definition = soup.find(name="div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def translate_to_russian(text):
    translator = Translator()
    try:
        translated = translator.translate(text, src='en', dest='ru')
        return translated.text
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text  # Возвращаем оригинальный текст, если перевод не удался

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово, попробуйте позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Перевод слова и его определения
        word_ru = translate_to_russian(word)
        word_definition_ru = translate_to_russian(word_definition)

        print(f"Значение слова - {word_definition_ru} (оригинал: {word_definition})")
        user = input("Какое это слово? ")

        if user == word_ru:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_ru} (оригинал: {word})")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
if __name__ == "__main__":
    word_game()
