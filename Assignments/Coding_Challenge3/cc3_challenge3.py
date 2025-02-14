import csv


year_list, month_list, value_list = [], [], []

with open("co2-ppm-daily.csv") as co2:


    csv_reader = csv.reader(co2, delimiter=",")

    line_count = 0


    next(csv_reader)

    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
        if month not in month_list:
            month_list.append(month)


        value_list.append(float(row[1]))
        line_count = line_count + 1

print(min(value_list))
print ("Total Minimum = " + str(min(value_list)))
print ("Total Maximum = " + str(max(value_list)))
print ("Total Average = " + str(float(sum(value_list) / int(line_count))))


year_value_dict = {}

for year in year_list:
    temp_year_list = []
    with open("co2-ppm-daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')

        next(csv_reader)

        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                temp_year_list.append(float(row[1]))

    year_value_dict[year] = str(sum(temp_year_list) / len(temp_year_list))

print ("Annual averages = " + str(year_value_dict))


spring_season_list = []
summer_season_list = []
autumn_season_list = []
winter_season_list = []
with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')

    next(csv_reader)

    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        if month_co2 == '03' or month_co2 == '04' or month_co2 == '05':
            spring_season_list.append(float(row[1]))
        if month_co2 == '06' or month_co2 == '07' or month_co2 == '08':
            summer_season_list.append(float(row[1]))
        if month_co2 == '09' or month_co2 == '10' or month_co2 == '11':
            autumn_season_list.append(float(row[1]))
        if month_co2 == '12' or month_co2 == '01' or month_co2 == '02':
            winter_season_list.append(float(row[1]))
#         Where did the numbers for each month come from? Were they created when the month_co2 list was created?

print ("Spring average = " + str(sum(spring_season_list) / len(spring_season_list)))
print ("Summer average = " + str(sum(summer_season_list) / len(summer_season_list)))
print ("Autumn average = " + str(sum(autumn_season_list) / len(autumn_season_list)))
print ("Winter average = " + str(sum(winter_season_list) / len(winter_season_list)))


average = sum(value_list) / len(value_list)
anomaly = {}

with open("co2-ppm-daily.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    next(csv_reader)


    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")
        anomaly[year_co2] = float(row[1]) - average

print ("Anomaly for years = " + str(anomaly))