import csv

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    f = open('table.html', 'a')
    f.write('''<!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
    }
    td {
      text-align: center;
    }
    </style>
    </head>
    <body>
    <table style="width:100%">\n''')

    for row in csv_reader:
        f.write(''' <tr>\n''')
        for cell in row:
            if len(cell) == 0:
                f.write(f'''     <td>{cell}</td>\n''')
            elif cell[0] == '*' and cell[len(cell) - 1] == '*':
                f.write(f'''     <td><strong>{cell[1:len(cell) - 1]}</strong></td>\n''')
            elif cell[0] == '_' and cell[len(cell) - 1] == '_':
                f.write(f'''     <td><u>{cell[1:len(cell) - 1]}</u></td>\n''')
            else:
                f.write(f'''     <td>{cell}</td>\n''')
        f.write(''' </tr>\n''')
    f.write('''</table>
    </body>
    </html>''')
    f.close()
