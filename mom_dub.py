import csv

with open('ms_file_result_dub_1.csv', 'w', newline='', encoding="utf-8") as file_rd_1:
    writer_rd_1=csv.writer(file_rd_1, delimiter=';')
    writer_rd_1.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )
with open('ms_file_result_dub_2.csv', 'w', newline='', encoding="utf-8") as file_rd_2:
    writer_rd_2=csv.writer(file_rd_2, delimiter=';')
    writer_rd_2.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )

                            
with open('ms_file_2.csv', 'r', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:      
        count=row
        n=0
        with open('ms_file_2.csv', 'r', newline='', encoding="utf-8") as file_1:
            reader_1 = csv.reader(file_1, delimiter=';')
            for row in reader_1:
                count_1=row
                if count[1:4] == count_1[1:4]:
                    if count[0]==count_1[0]:
                        b=1
                    else:
                        with open('ms_file_result_dub_2.csv', 'a', newline='', encoding="utf-8") as file_a:
                            writer_d2 = csv.writer(file_a, delimiter=';')
                            writer_d2.writerow(count)
                            





