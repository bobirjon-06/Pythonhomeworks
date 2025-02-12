def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition = [uni[2] for uni in universities]
    return students, tuition

def mean(value):
    return sum(value) / len(value)

def median(value):
    sorted_value = sorted(value)
    n = len(sorted_value)
    mid = n // 2
    if n% 2 == 0:
        return (sorted_value[mid-1]+sorted_value[mid])
    else:
        return sorted_value[mid]
    
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, tuition, = enrollment_stats(universities)

totalstudents = sum(students)
totaltuition = sum (tuition)
stmean = mean(students)
tumean = mean(tuition)
stmedian = median(students)
tumedian = median(tuition)

print(
    f"Total students: {totalstudents:,}\n" 
    f"Total tuition: {totaltuition:,}\n"
    f"Student mean: {stmean:,.2f}\n"
    f"Student median: {stmedian:,}\n"
    f"Tuition mean: {tumean:,.2f}\n"
    f"Tuition medianL {tumedian:,}\n"
)