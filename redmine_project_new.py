import logging
import csv

from redminelib import Redmine

import settings


logging.basicConfig(filename='redmine.log', level=logging.INFO)
redmine = Redmine(settings.URL, key=settings.API_KEY, requests={'verify':False})

# for project in redmine.project.all():
#     print(project.id, project.name)


def get_extended_issue_new():
    issues = redmine.issue.filter(project_id=2, limit=30).values()
    extended_issue_list = []

    for issue_info in issues:
        id_issue = issue_info.get('id')
        custom_fields = issue_info.get('custom_fields')
        subject = issue_info.get('subject')
        status = issue_info.get('status')
        priority = issue_info.get('priority')
        description = issue_info.get('description')
        created_on = issue_info.get('created_on')
        updated_on = issue_info.get('updated_on')
        extended_issue = {}
        
        extended_issue['id'] = id_issue
        extended_issue['subject'] = subject
        extended_issue['status'] = status['name']
        extended_issue['priority'] = priority['name']
        for fields in custom_fields:
            
            extended_issue[fields['name']] = fields.setdefault('value', '')

        extended_issue['description'] = description.replace('\r\n', ' ')
        extended_issue['created_on'] = created_on
        extended_issue['updated_on'] = updated_on
        extended_issue_list.append(extended_issue)
    return extended_issue_list


extended_issue_list = get_extended_issue_new()
# print(extended_issue_list)


with open('export.csv', 'w', encoding='utf-8') as export_issue:
    column = [
        'Исполнитель ТП',
        'id',
        'status',
        'priority',
        'subject',
        'Секция НЭП',
        'Jira',
        'Тип запроса',
        'Способ решения',
        'Сервис НЭП',
        'Срок',
        'Сервис Фабр.',
        'ТП №',
        'description',
        'created_on',
        'updated_on',
        'SLA'
        ]
    column_export_writer = csv.DictWriter(export_issue, column, delimiter=';')
    column_export_writer.writeheader()

    for column_list in extended_issue_list:
        column_export_writer.writerow(column_list)