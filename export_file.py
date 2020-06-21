import csv

from redmine_project import

with open('export.csv', 'w', encoding='utf-8') as export_issue:

    column = ['id', 'status', 'priority', 'subject', 'assigned_to', 'Секция НЭП', 'Jira', 'Тип запроса', 'Способ решения', 'Сервис НЭП', 'Срок', 'Сервис Фабр.', 'ТП №',  'description', 'created_on', 'updated_on']
    column_export_writer = csv.DictWriter(export_issue, column, delimiter=';')
    column_export_writer.writeheader()

    for column_list in extended_issue_list:
        column_export_writer.writerow(column_list)