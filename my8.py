def main():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    with open("input.txt", "r", encoding="utf-8") as file_in:
        steps = [int(line.strip()) for line in file_in]

    monthly_avg = []
    start = 0

    for days in days_in_month:
        month_steps = steps[start:start + days]
        avg = round(sum(month_steps) / days)
        monthly_avg.append(avg)
        start += days

    with open("output.txt", "w", encoding="utf-8") as file_out:
        for avg in monthly_avg:
            file_out.write(str(avg) + "\n")


main()
