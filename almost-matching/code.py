ANSWER = True
input1 = [item for item in "a*baa**ba**aa".split("*") if item]
input2 = [item for item in "*ca*b**a*baaa".split("*") if item]
re_input1 = ["[a-zA-Z]{0,4}" + item + "[a-zA-Z]{0,4}" for item in "a*baa**ba**aa".split("*") if item]
re_input2 = ["[a-zA-Z]{0,4}" + item + "[a-zA-Z]{0,4}" for item in "*ca*b**a*baaa".split("*") if item]

import re

result1 = []
result2 = []
for index in range(0,len(input1)):
    result1.append(bool(re.match(input1[index], re_input2[index])))
for index in range(0,len(input1)):
    result2.append(bool(re.match(re_input1[index], input2[index])))

print input1, re_input2, result1
print re_input1, input2, result2


