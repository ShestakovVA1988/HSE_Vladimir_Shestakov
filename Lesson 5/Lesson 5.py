import json, csv, re

def task_1():
    with open('traders.txt', 'r') as f:
        innens = f.readlines()
        innens = [inn.strip() for inn in innens]

    with open('traders.json', 'r') as f:
        data = json.load(f)
        data = {dct['inn']: dct for dct in data}


    with open('traders.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for inn in innens:
            dct = data.get(inn)
            r_1 = dct.get('inn')
            r_2 = dct.get('ogrn')
            r_3 = dct.get('address')
            writer.writerow([r_1, r_2, r_3])



def task_2():
    email_pattern = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')

    with open('1000_efrsb_messages.json', 'r') as f:
        data = json.load(f)

    result = {}
    for dct in data:
        inn = dct.get('publisher_inn')
        text = dct.get('msg_text')
        emails = list(set(re.findall(email_pattern, text)))
        if emails:
            result[inn] = emails
    with open('emails.json', 'w') as f:
        json.dump(result, f)


task_1()
task_2()