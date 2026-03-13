def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        lines = [line.rstrip("\n") for line in file_in]

    try:
        lines_count = int(lines[0])
    except (ValueError, IndexError):
        with open("output.txt", "w", encoding="utf-8") as file_out:
            file_out.write("ERROR")
        return

    real_count = len(lines) - 1

    with open("output.txt", "w", encoding="utf-8") as file_out:
        if real_count == lines_count:
            file_out.write("YES")
        else:
            file_out.write("NO")



main()
