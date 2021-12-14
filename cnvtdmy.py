with open("date_list.txt", "r") as file: 
    line = file.read().split("\n")

    date_list = []

    for date in line:

        if "-" in date:

            ##### CASE: Jan-2000 #####
            if date.startswith("Jan") or date.startswith("Feb") or date.startswith("Mar") or date.startswith("Apr") or date.startswith("May") or date.startswith("Jun") or date.startswith("Jul") or date.startswith("Aug") or date.startswith("Sep") or date.startswith("Oct") or date.startswith("Nov") or date.startswith("Dec"):
                month = date[0:3]
                if month == "Jan":
                    number = "01"
                elif month == "Feb":
                    number = "02"
                elif month == "Mar":
                    number = "03"
                elif month == "Apr":
                    number = "04"
                elif month == "May":
                    number = "05"
                elif month == "Jun":
                    number = "06"
                elif month == "Jul":
                    number = "07"
                elif month == "Aug":
                    number = "08"
                elif month == "Sep":
                    number = "09"
                elif month == "Oct":
                    number = "10"
                elif month == "Nov":
                    number = "11"
                elif month == "Dec":
                    number = "12"
                year = date[4:8]
                str_date = year + "-" + number + "-" + "XX"

            ##### CASE: 01-Jan-2000 #####
            else:
                day = date[0:2]
                month = date[3:6]
                if month == "Jan":
                    number = "01"
                elif month == "Feb":
                    number = "02"
                elif month == "Mar":
                    number = "03"
                elif month == "Apr":
                    number = "04"
                elif month == "May":
                    number = "05"
                elif month == "Jun":
                    number = "06"
                elif month == "Jul":
                    number = "07"
                elif month == "Aug":
                    number = "08"
                elif month == "Sep":
                    number = "09"
                elif month == "Oct":
                    number = "10"
                elif month == "Nov":
                    number = "11"
                elif month == "Dec":
                    number = "12"
                year = date[7:11]
                str_date = year + "-" + number + "-" + day

        ##### CASE: 2000 #####
        elif "-" not in date:
            str_date = date + "-" + "XX" + "-" + "XX"

        date_list.append(str_date)

    f = open("date.txt", "w")
    for line in date_list:
        f.write(str(line))
        f.write("\n")
    f.close()
