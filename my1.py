def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        text = file_in.read()

    text_upper = text.upper()

    with open("output.txt", "w", encoding="utf-8") as file_out:
        file_out.write(text_upper)


main()




