import json

# Load the JSON file
f = open('/programming/Json_Prac/Json_text.json', 'r')

raw_data = f.read()

j_data = json.loads(raw_data)
check_length = len(j_data)
#print(check_length)

n = 0
for i in range(len(j_data)):
    what = j_data[i]
    n += 1
    print(" ")
    print(f'第{n}個')
    #print(what)
    #print(len(what))
    #print(type(what))

    if 'data' in what:
        extract = what['data']
        print(what['data']) #be ware of the ['what you want']

        print(len(extract))
        print(type(extract))

        if len(extract) == 0:
            print('meh')
        else:
            print(what['data'][0]['post']) 
            # what is a dictionary, and has a key called data, which is a list. and I want the first item in the list which is [0]. what['data'][0] is a another dictionary, so I should tell it what I want is the value stored under the key ['post] 
            #print(extract)

            decode = what['data'][0]['post'].encode('latin1').decode('utf8')
            print(decode)


f.close()
#print(data)
#print(read_data['data'])