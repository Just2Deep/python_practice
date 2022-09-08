# using regex to find patterns

import re

emails = '''
            CoreyMSchafer@gmail.com
            corey.schafer@university.edu
            corey-321-schafer@my-work.net
         '''
pattern = re.compile(r'[a-zA-Z0-9-._]+@[a-zA-Z0-9-]+\.[a-zA-z]+')

matches = pattern.finditer(emails)

# for match in matches:
#     print(match)


urls = '''
        https://www.google.com
        http://coreyms.com
        https://youtube.com
        https://www.nasa.gov
       '''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     # print(match.group(0))
#     print(match.group(2) + match.group(3))
