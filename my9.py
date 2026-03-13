import os

def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        lines = [line.rstrip("\n") for line in file_in]

    even_lines = lines[1::2]

    os.makedirs("simple", exist_ok=True)

    with open("simple/output.txt", "w", encoding="utf-8") as file_out:
        for line in even_lines:
            file_out.write(line + "\n")


main()
