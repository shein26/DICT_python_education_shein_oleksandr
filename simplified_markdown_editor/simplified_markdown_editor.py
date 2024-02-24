# simplified_markdown_editor.py

def help_message():
    """
    Функція для виведення довідкового повідомлення з доступними командами форматування.
    """
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def apply_formatting(formatter, text):
    """
    Функція, яка застосовує форматування до тексту та повертає текст із відповідними тегами Markdown.
    """
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "header":
        level = int(input("Level: > "))
        if 1 <= level <= 6:
            return "#" * level + " " + text + "\n"
        else:
            print("The level should be within the range of 1 to 6.")
            return ""
    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "ordered-list":
        num_rows = int(input("Number of rows: > "))
        if num_rows <= 0:
            print("The number of rows should be greater than zero.")
            return ""
        lines = [input(f"Row #{i}: > ") for i in range(1, num_rows + 1)]
        return "\n".join([f"{i + 1}. {line}" for i, line in enumerate(lines)]) + "\n"
    elif formatter == "unordered-list":
        num_rows = int(input("Number of rows: > "))
        if num_rows <= 0:
            print("The number of rows should be greater than zero.")
            return ""
        lines = [input(f"Row #{i}: > ") for i in range(1, num_rows + 1)]
        return "\n".join([f"* {line}" for line in lines]) + "\n"
    elif formatter == "new-line":
        return "\n"
    else:
        print("Unknown formatting type or command")
        return ""

def main():
    formatted_text = ""  # Змінна для зберігання отриманого форматованого тексту

    while True:
        user_input = input("Choose a formatter: > ")

        if user_input == "!help":
            help_message()
        elif user_input == "!done":
            with open("output.md", "w") as file:
                file.write(formatted_text)  # Зберігаємо форматований текст у файл output.md
            print("Saving and quitting...")
            break
        else:
            formatted_text += apply_formatting(user_input, input("Text: > "))

        print(formatted_text)

if __name__ == "__main__":
    main()
