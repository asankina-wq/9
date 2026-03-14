def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        text = file_in.readlines()

    with open("output.txt", "w", encoding="utf-8") as file_out:
        for line in text:
            if line.strip():
                file_out.write(line[0])


main()
