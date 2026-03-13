def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        text = file_in.readlines()

    with open("output.txt", "w", encoding="utf-8") as file_out:
        for line in text:
            if line.startswith(("A", "a")):
                file_out.write(line)


main()
