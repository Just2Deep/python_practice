# using regex to find patterns

import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r'[a-zA-Z0-9-._]+@[a-zA-Z0-9-]+\.[a-zA-z]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
