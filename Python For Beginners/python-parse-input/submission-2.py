from typing import List

def read_integers() -> List[int]:
    info=input("")
    list_of_string=info.split(",")
    list_of_int=[]
    for string in list_of_string:
        list_of_int.append(int(string))

    return list_of_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
