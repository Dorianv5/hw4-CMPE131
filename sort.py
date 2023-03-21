def sort_dictionary(dict):
    output = ()
    temp = sorted([(name, phone, age) for name, (phone, age) in dict.items()],key=lambda age: age[2])
    for i in temp:
        output += (i[:-1])
    return output
#print (sort_dictionary ({"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}))