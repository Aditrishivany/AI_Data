import re
# text="python is powerful"
# result=re.search("powerful",text)
# if result:
#     print("Match found",result.group())

# tex="my num is 1234567890 and 0987654321"
# number=re.findall("\d{10}",tex)
# print(number)

# for match in re.finditer("\d{10}",tex):
#     print("match found at index:", match.start(),"to",match.end())

text="my phone number is 1234567890"
masked=re.sub("\d{6}","******",text)
print(masked)