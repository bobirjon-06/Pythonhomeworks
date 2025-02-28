import csv

def read_grades(filename):
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}

    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    averages = {}
    for subject in subject_totals:
        averages[subject] = subject_totals[subject] / subject_counts[subject]

    return averages

def write_average_grades(filename, averages):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, average in averages.items():
            writer.writerow([subject, round(average, 1)])

def main():
    input_file = 'grades.csv'
    output_file = 'average_grades.csv'

    with open(input_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Subject', 'Grade'])
        writer.writerow(['Alice', 'Math', '85'])
        writer.writerow(['Bob', 'Science', '78'])
        writer.writerow(['Carol', 'Math', '92'])
        writer.writerow(['Dave', 'History', '74'])

    grades = read_grades(input_file)
    averages = calculate_average_grades(grades)
    write_average_grades(output_file, averages)

    print("Averages written to", output_file)

if __name__ == '__main__':
    main()