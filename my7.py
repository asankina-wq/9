def main():
    with open("input.txt", "r", encoding="utf-8") as file_in:
        numbers = [int(line.strip()) for line in file_in if line.strip()]

    filtered_numbers = []
    for num in numbers:
        if num != 100:
            filtered_numbers.append(num)

    with open("input.txt", "w", encoding="utf-8") as file_out:
        for num in filtered_numbers:
            file_out.write(f"{num}\n")


main()
