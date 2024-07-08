def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = [float(line.split(",")[1].strip()) for line in file]
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            return total, average
    except FileNotFoundError:
        print(f"File with path{path} was not found.")
        return 0, 0
    except Exception as e:
        print(f"An error occured during file processing: {e}")
        return 0, 0

file_path = "salary_file.txt"
total, average = total_salary(file_path)
print(f"Total salary amount: {total}, Average salary amount: {average}")