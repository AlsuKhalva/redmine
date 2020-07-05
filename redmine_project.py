import logging
import csv

from redminelib import Redmine

import settings


logging.basicConfig(filename='redmine.log', level=logging.INFO)

redmine = Redmine(settings.URL,key=settings.API_KEY,requests={'verify': False})


def get_extended_issue():
    project = redmine.project.get(settings.project_id)
    issue_id_list = get_id_list()
    extended_issue_list = []

    for issue_id in issue_id_list:
        issue = project.issues.get(issue_id)
        print(issue)
        print(type(issue))

        id_issue = issue.id
        custom_fields = issue.custom_fields
        list_custom_fields = list(custom_fields)
        subject = issue.subject
        assigned_to = issue.assigned_to
        status = issue.status
        priority = issue.priority
        description = issue.description
        created_on = issue.created_on
        updated_on = issue.updated_on
        extended_issue = {}

        for fields in list_custom_fields:
            extended_issue[fields.name] = fields.value

        extended_issue['id'] = id_issue
        extended_issue['subject'] = subject
        extended_issue['assigned_to'] = assigned_to.name
        extended_issue['status'] = status.name
        extended_issue['priority'] = priority.name
        extended_issue['description'] = description.replace('\r\n', ' ')
        extended_issue['created_on'] = created_on
        extended_issue['updated_on'] = updated_on
        extended_issue_list.append(extended_issue)
    return extended_issue_list


def get_id_list():
    
    issues = redmine.issue.filter(project_id=settings.project_id, limit=3).values()
    get_issue_id_list = list(issues)

    id_list = [items['id'] for items in get_issue_id_list]

    return id_list


extended_issue_list = get_extended_issue()
print(extended_issue_list)


with open('export.csv', 'w', encoding='utf-8') as export_issue:

    column = ['id', 'status', 'priority', 'subject', 'assigned_to', 'Секция НЭП', 'Jira',
              'Тип запроса', 'Способ решения', 'Сервис НЭП', 'Срок', 'Сервис Фабр.', 'ТП №',
              'description', 'created_on', 'updated_on']
    column_export_writer = csv.DictWriter(export_issue, column, delimiter=';')
    column_export_writer.writeheader()

    for column_list in extended_issue_list:
        column_export_writer.writerow(column_list)