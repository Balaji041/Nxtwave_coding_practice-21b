names=input()
list_names=names.split()
for i in list_names:
    if i[0].upper()==i[-1].upper():
        print("True")
    else:
        print("False")

"""

input:water Noon river
output:
False
True
True
"""
