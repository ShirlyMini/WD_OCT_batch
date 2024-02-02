import re

content="""Python is dynamically typed and garbage-collected. It supports multiple programming paradigms,including structured (particularly procedural), object-oriented and functional programming.It is often described as a 'batteries included' language due to its comprehensive standard library."""

# print(re.findall("\w+", content))

# print(re.split("\s+", content))
# print(re.split(", | \s+", content))

# x = re.match(".*", content)# exactly should match the content
# print(x)
# print(x.group())
#
# x = re.search("procedural", content)# partial match
# print(x)
# print(x.group())


x = re.sub("\W", "00", content)
print(x)