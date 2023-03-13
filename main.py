from pprint import pprint
import csv
import re

def group_data(data_file):
    """функция для группировки данных"""
    group_list = list()
    pattern = r'(\+7|8)?\s*?\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})[\s,]?\(?(доб.)?\s?(\d{4})?\)?'
    substitution = r'+7(\2)\3-\4-\5 \6 \7'
    for item in data_file:
        f_i_o = ' '.join(item[:3]).split(' ')
        pattern_change = re.sub(pattern, substitution, item[5])
        result = [f_i_o[0], f_i_o[1], f_i_o[2], item[3], item[4],
                    re.sub(rf'{pattern}', substitution, item[5]),
                    item[6]]
        result[5] = result[5].rstrip()
        group_list.append(result)
    group_list.sort()
    # pprint(group_list)    
    return group_list

def merge_duplicated_data(contacts):
    """функция, объединяющая все дублирующие записи о человеке в одну"""
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": 
                    contact[2] = new_contact[2]
                if contact[3] == "": 
                    contact[3] = new_contact[3]
                if contact[4] == "": 
                    contact[4] = new_contact[4]
                if contact[5] == "": 
                    contact[5] = new_contact[5]
                if contact[6] == "": 
                    contact[6] = new_contact[6]
    address_book = list()
    for i in contacts:
        if i not in address_book:
            address_book.append(i)
    # pprint(address_book)
    return address_book

if __name__ == '__main__':

    with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)
    address_book = group_data(contacts_list)
    address_book = merge_duplicated_data(address_book)

    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(address_book)
        
