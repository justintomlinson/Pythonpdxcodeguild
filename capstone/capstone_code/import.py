import xlrd
import csv

#def import_data_file('filename')


def excel_to_csv(excel_file, sheetname, csv_file):
    wbook = xlrd.open_workbook(excel_file)
    wsheet = wbook.sheet_by_name(sheetname)
    new_csv = open(csv_file, 'w', encoding='utf8')
    wr = csv.writer(new_csv, quoting=csv.QUOTE_ALL)

    for rows in range(wsheet.nrows):
        wr.writerow(wsheet.row_values(rows))

    new_csv.close()



