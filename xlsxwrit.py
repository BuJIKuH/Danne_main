import xlsxwriter
from domashnyaya import array_domashnyaya
from professionalnaya_liniya import array_professional
from limited import array_limited
from dmk_travel import array_travel
from brendirovannaya import array_brendirovannaya

def writer(domashnyaya, limited, professionalnaya_liniya, dmk_travel,brendirovannaya):
    book = xlsxwriter.Workbook(r"/Users/bujikuh/Desktop/Cosmetics compain/Danne/Danne.xlsx")
    page_1 = book.add_worksheet('Домашняя линия')
    page_2 = book.add_worksheet('Профессиональная линия')
    page_3 = book.add_worksheet('Линия DMK Limited')
    page_4 = book.add_worksheet('DMK Travel')
    page_5 = book.add_worksheet('Брендированные аксессуары')

    bold = book.add_format({'bold': True})

    headers = ['Наименование', "Краткое описание", " Описание", "Ссылка на фото товара", "Цена", "Примечание"]
    for col, h in enumerate(headers):
        page_1.write_string(0, col, h, cell_format=bold)
        page_2.write_string(0, col, h, cell_format=bold)
        page_3.write_string(0, col, h, cell_format=bold)
        page_4.write_string(0, col, h, cell_format=bold)
        page_5.write_string(0, col, h, cell_format=bold)

    page_1.set_column('A:A', 15)
    page_1.set_column('B:B', 22)
    page_1.set_column('C:C', 50)
    page_1.set_column('D:D', 25)
    page_1.set_column('E:E', 10)
    page_1.set_column('F:F', 30)

    page_2.set_column('A:A', 15)
    page_2.set_column('B:B', 22)
    page_2.set_column('C:C', 50)
    page_2.set_column('D:D', 25)
    page_2.set_column('E:E', 10)
    page_2.set_column('F:F', 30)

    page_3.set_column('A:A', 15)
    page_3.set_column('B:B', 22)
    page_3.set_column('C:C', 50)
    page_3.set_column('D:D', 25)
    page_3.set_column('E:E', 10)
    page_3.set_column('F:F', 30)

    page_4.set_column('A:A', 15)
    page_4.set_column('B:B', 22)
    page_4.set_column('C:C', 50)
    page_4.set_column('D:D', 25)
    page_4.set_column('E:E', 10)
    page_4.set_column('F:F', 30)

    page_5.set_column('A:A', 15)
    page_5.set_column('B:B', 22)
    page_5.set_column('C:C', 50)
    page_5.set_column('D:D', 25)
    page_5.set_column('E:E', 10)
    page_5.set_column('F:F', 30)


    row = 1
    column = 0

    for item in domashnyaya():
        page_1.write(row, column, item[0])
        page_1.write(row, column + 1, item[1])
        page_1.write(row, column + 2, item[2])
        page_1.write(row, column + 3, item[3])
        # page_1.write(row, column + 4, item[4])
        row += 1
    row = 1
        #
    for item in professionalnaya_liniya():
        page_2.write(row, column, item[0])
        page_2.write(row, column + 1, item[1])
        page_2.write(row, column + 2, item[2])
        page_2.write(row, column + 3, item[3])
        # page_2.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in limited():
        page_3.write(row, column, item[0])
        page_3.write(row, column + 1, item[1])
        page_3.write(row, column + 2, item[2])
        page_3.write(row, column + 3, item[3])
        # page_3.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in dmk_travel():
        page_4.write(row, column, item[0])
        page_4.write(row, column + 1, item[1])
        page_4.write(row, column + 2, item[2])
        page_4.write(row, column + 3, item[3])
        # page_4.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in brendirovannaya():
        page_5.write(row, column, item[0])
        page_5.write(row, column + 1, item[1])
        page_5.write(row, column + 2, item[2])
        page_5.write(row, column + 3, item[3])
        # page_5.write(row, column + 4, item[4])
        row += 1

    book.close()

writer(array_domashnyaya, array_professional, array_travel, array_limited, array_brendirovannaya)