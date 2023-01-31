import re

mail = ['meow@gmail.com <meow@gmail.com>', ' quack <quack@ntu.edu.tw>', ' gurumeow@guru.com <gurumeow@guru.com>', ' furufuru@Gamil.com <furufuru@Gmail.com>']


clean_address = [ ]
sub1 = '<'
sub2 = '>'

for address in mail:
    idx1 = address.index(sub1)
    idx2 = address.index(sub2)
    res = ''

    for idx in range (idx1 + len(sub1), idx2):
        res = res + address[idx]
    
    clean_address.append(res.lower())

mail_type = []
for address in clean_address:
    x = re.findall('\@(\S+)', address)
    mail_type.append(x)


classify = []
for adr in mail_type:
    if adr not in classify:
        classify.append(adr)

stat = []
for adr in classify:
    c = mail_type.count(adr)
    res = f'{c} from {adr}'
    stat.append(res)

stat.sort(reverse=True)

for i in stat:
    print(i)
