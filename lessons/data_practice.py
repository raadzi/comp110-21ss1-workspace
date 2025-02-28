from csv import DictReader


#opens the data file and creates a data table that is a list of dictionaries (rows)
#the column titles are the keys for the dictionaries
file_handle = open("data/survey.csv", encoding = "utf8")
csv_reader = DictReader(file_handle)
table: list[dict[str, str]] = []
for row in csv_reader:
    table.append(row)
file_handle.close()


#processing a column of the table to calculate the average perception of pace
##creates a list of percieved paces then calculates average pace
paces: list[float] = []
for row in table:
    pace: float = float(row["pace"])
    paces.append(pace)
average_pace: float = sum(paces) / len(paces)
print(f"Average percieved pace: {average_pace}")