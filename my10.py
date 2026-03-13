def main():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def date_to_day_of_year(date_str):
        day, month = map(int, date_str.split("."))
        return sum(days_in_month[:month - 1]) + day

    with open("input.txt", "r", encoding="utf-8") as file_in:
        lines = []
        for line in file_in:
            cleaned = line.strip()
            if cleaned:
                lines.append(cleaned)

    current_day_of_year = date_to_day_of_year(lines[0])
    cell_count = int(lines[1])
    output_cells = []

    for index in range(2, 2 + cell_count):
        cell_info = lines[index].split()
        cell_number = cell_info[0]
        deposit_day_of_year = date_to_day_of_year(cell_info[1])

        if current_day_of_year - deposit_day_of_year > 3:
            output_cells.append(cell_number)

    with open("output.txt", "w", encoding="utf-8") as file_out:
        for cell in output_cells:
            file_out.write(cell + "\n")


main()
