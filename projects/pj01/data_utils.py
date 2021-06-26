from csv import DictReader

file_handle = open("data/survey.csv", encoding = "utf8")
csv_reader = DictReader(file_handle)

table: list[dict[str, str]] = []
for row in csv_reader:
    print(row)

