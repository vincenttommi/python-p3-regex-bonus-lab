import re
my_pattern = r"[A-Z][a-z']{3,5}\s[a-z']{4,}\s[a-z']{1,}\s[a-z']{3,}\s[a-z]{2,}[\.,]?\s[a-z]{3,}[\.\?]"
my_regex = re.compile(my_pattern)