import json

# info = {
    # "name":"Narek",
#     "age":17
# }


# with open("info.json","w") as file:
    # json.dump(info,file,indent=4,ensure_ascii=False)

# with open("info.json","r") as file:
#     result = json.load(file) 
# info = input()

# print(result.get(info, 'chka'))

# def naughty_or_nice(data):
#     with  open(data,"r") as file:
#         dct = json.load(file)
        # nice = 0
#         naughty = 0
#         for i in dct.values():
#             for j in i.values():
#                 if j == "Nice":
#                     nice += 1
#                 elif j == "Naughty":
#                     naughty += 1     
#         if naughty > nice:
#             return "Naughty!"
#         elif naughty <= nice:
#                 return "Nice!"

# print(naughty_or_nice("info.json"))

# contains_seventh_son_of_seventh_son = {
#     'name': 'A',
#     'gender': 'male',
#     'children': [
#         {'name': 'B',
#          'gender': 'male',
#          'children': []},
#         {'name': 'C',
#          'gender': 'male',
#          'children': []},
#         {'name': 'D',
#          'gender': 'male',
#          'children': []},
#         {'name': 'E',
#          'gender': 'male',
#          'children': []},
#         {'name': 'F',
#          'gender': 'male',
#          'children': []},
#         {'name': 'G',
#          'gender': 'male',
#          'children': []},
#         {'name': 'H', # This is the seventh son
#          'gender': 'male',
#          'children':[
#             {'name': 'I',
#              'gender': 'male',
#              'children': []},
#             {'name': 'J',
#              'gender': 'male',
#              'children': []},
#             {'name': 'K',
#              'gender': 'male',
#              'children': []},
#             {'name': 'L',
#              'gender': 'male',
#              'children': []},
#             {'name': 'M',
#              'gender': 'male',
#              'children': []},
#             {'name': 'N',
#              'gender': 'male',
#              'children': []},
#             {'name': 'O', # This is the sventh son of the seventh son
#              'gender': 'male',
#              'children': []}
#          ]}
#     ]
# }

# for i,k in enumerate(contains_seventh_son_of_seventh_son['children']):
#     if i == 6:
#         for i,d 

matrix = [[1,2,3],
          [4,5,6], 
          [7,8,9]]
lst = []
for i in range(len(matrix)):
    for j in range(i+1):
        matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

for i in range(len(matrix)):
    matrix[i] = matrix[i][::-1]
print(matrix)