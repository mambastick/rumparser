import requests
from bs4 import BeautifulSoup
import json
import matplotlib.pyplot as plt


# Функция для получения HTML-страницы
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Функция для парсинга данных с HTML-страницы
def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = {}

    # Пример парсинга текстов из всех тегов
    for tag in soup.find_all():
        tag_name = tag.name
        tag_text = tag.get_text(strip=True)
        if tag_text:
            if tag_name not in data:
                data[tag_name] = []
            data[tag_name].append(tag_text)

    return data


# Функция для построения графика
def plot_data(data):
    # Считаем количество каждого типа тега
    tags_count = {tag: len(texts) for tag, texts in data.items()}

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.bar(tags_count.keys(), tags_count.values(), color='skyblue')
    plt.xlabel('HTML Tags')
    plt.ylabel('Count')
    plt.title('Distribution of HTML Tags on the Page')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Сохранение графика
    plt.savefig('tags_distribution.png')
    plt.show()


# Основная функция
def main():
    url = 'https://rosunimed.ru'  # Введите URL нужного сайта
    html = get_html(url)
    data = parse_data(html)

    # Сохранение данных в JSON файл
    with open('parsed_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Data saved to parsed_data.json")

    # Построение и сохранение графика
    plot_data(data)
    print("Plot saved to tags_distribution.png")


if __name__ == '__main__':
    main()
