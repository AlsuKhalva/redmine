import logging


from redminelib import Redmine

import settings


logging.basicConfig(filename='redmine.log', level=logging.INFO)

redmine = Redmine(settings.URL, key = settings.API_KEY, requests={'verify': False})

# for project in redmine.project.all():
#     print(project)


# project = redmine.project.get(333)
# issues = project.issues.get(131868)
# for item in issues:
#     print(item)

def get_extended_issue(issue_id):
    issue = project.issues.get(issue_id)
    id_issue = issue.id
    custom_fields = issue.custom_fields
    list_custom_fields = list(custom_fields)
    subject = issue.subject
    assigned_to =issue.assigned_to
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

    return extended_issue

project = redmine.project.get(333)

extended_issue = get_extended_issue(131868)


print(extended_issue)
extended_issue_list = []

extended_issue_list.append(extended_issue) 


