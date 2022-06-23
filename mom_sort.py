import csv
from ntpath import join

#Формирования файлов с номерами
"""n=1
with open('ms_file_1.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer=csv.writer(csvfile, delimiter=';')
    writer.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )

with open('msort_file_1.csv', 'r', newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        #print(', '.join(row))
        trans_1=row[0]
        trans_2=row[1]
        trans_3=row[2]
        trans_4=row[3]
        with open('ms_file_1.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(
                [n,trans_1,trans_2,trans_3,trans_4]
            )
            n+=1

n=1
with open('ms_file_2.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer=csv.writer(csvfile, delimiter=';')
    writer.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )

with open('msort_file_2.csv', 'r', newline='',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        #print(', '.join(row))
        trans_1=row[0]
        trans_2=row[1]
        trans_3=row[2]
        trans_4=row[3]
        with open('ms_file_2.csv', 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(
                [n,trans_1,trans_2,trans_3,trans_4]
            )
            n+=1

"""
with open('ms_file_result_non_1.csv', 'w', newline='', encoding="utf-8") as file_rn_1:
    writer_rn_1=csv.writer(file_rn_1, delimiter=';')
    writer_rn_1.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )
with open('ms_file_result_dub_1.csv', 'w', newline='', encoding="utf-8") as file_rd_1:
    writer_rd_1=csv.writer(file_rd_1, delimiter=';')
    writer_rd_1.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )

with open('ms_file_result_non_2.csv', 'w', newline='', encoding="utf-8") as file_rn_2:
    writer_rn_2=csv.writer(file_rn_2, delimiter=';')
    writer_rn_2.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )
with open('ms_file_result_dub_2.csv', 'w', newline='', encoding="utf-8") as file_rd_2:
    writer_rd_2=csv.writer(file_rd_2, delimiter=';')
    writer_rd_2.writerow(
        ["Номер","Фамилия","Имя","отчество","Дата рождения"]
    )



with open('ms_file_1.csv', 'r', newline='',encoding="utf-8") as file_1:
    reader_1 = csv.reader(file_1, delimiter=';')
    for row in reader_1:
        count=row
        with open('ms_file_2.csv', 'r', newline='', encoding="utf-8") as file_2:
            reader_2 = csv.reader(file_2, delimiter=';')
            n=0
            for row in reader_2:
                count_a=row
                if count[1:4]==count_a[1:4]:
                    n+=1
                    if n>1:
                        with open('ms_file_result_dub_1.csv', 'a', newline='', encoding="utf-8") as file_a:
                            writer_d2 = csv.writer(file_a, delimiter=';')
                            writer_d2.writerow(
                                count_a
                                )
            if n==0:
                with open('ms_file_result_non_1.csv', 'a', newline='', encoding="utf-8") as file_b:
                    writer_n1 = csv.writer(file_b, delimiter=';')
                    writer_n1.writerow(
                        count
                        )


with open('ms_file_2.csv', 'r', newline='',encoding="utf-8") as file_2:
    reader_2 = csv.reader(file_2, delimiter=';')
    for row in reader_2:
        count=row
        with open('ms_file_1.csv', 'r', newline='', encoding="utf-8") as file_1:
            reader_1 = csv.reader(file_1, delimiter=';')
            n=0
            for row in reader_1:
                count_b=row
                if count[1:4]==count_b[1:4]:
                    n+=1
                    if n>1:
                        with open('ms_file_result_dub_2.csv', 'a', newline='', encoding="utf-8") as file_a:
                            writer_d2 = csv.writer(file_a, delimiter=';')
                            writer_d2.writerow(
                                count_b
                                )
            if n==0:
                with open('ms_file_result_non_2.csv', 'a', newline='', encoding="utf-8") as file_b:
                    writer_n1 = csv.writer(file_b, delimiter=';')
                    writer_n1.writerow(
                        count
                        )
            


