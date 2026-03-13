def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        text = [line.strip() for line in file_in if line.strip()]

    try:
        a = int(text[0])
        b = int(text[1])
        c = int(text[2])
        result = a / b + c

        with open("output.txt", "w", encoding="utf-8") as file_out:
            file_out.write(str(result))

    except ZeroDivisionError:
        with open("output.txt", "w", encoding="utf-8") as file_out:
            file_out.write("division by 0")

    except ValueError:
        with open("output.txt", "w", encoding="utf-8") as file_out:
            file_out.write("data error")


main()
