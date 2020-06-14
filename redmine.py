import logging
from redminelib import Redmine
import settings


logging.basicConfig(filename='redmine.log', level=logging.INFO)

redmine = Redmine(settings.URL, key = settings.API_KEY, requests={'verify': False})

# for project in redmine.project.all():
#     print(project)


# project = redmine.project.get(333)
# issues = project.issues.get(131868)
# # list_item = []
# for item in issues:
#     print(item)


def issues_list():
    project = redmine.project.get(333)
    issues = project.issues.get(131868)
    list_item = []
    for item in issues:
        a = [item]
        list_item += a
        # print(a)
    return list_item
    
print(issues_list())


