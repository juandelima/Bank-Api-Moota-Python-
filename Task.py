'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -> api_toke
Token bisa Anda dapatkan di halaman Settings web Moota.


{bank_id}
ID Akun Bank anda. Untuk mendapatkan ID, silahkan akses ENDPOINT api/v1/bank terlebih dahulu.
'''

import requests
import json
import datetime

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
}

get_api_moota = requests.get('https://app.moota.co/api/v1/bank/{bank_id}/mutation', headers = headers)

def menu():
    menu = ['Balance Check','Mutation Check']
    for i in range(len(menu)):
        print("%d. %s"%(i+1, menu[i]))
    while True:
        menu = input("Select menu [1 - 2]: ")
        if menu == '1':
            balance_check(get_api_moota)
            break
        elif menu == '2':
            mutation_check(get_api_moota)
            break
        else:
            print("Invalid choice. Try again")

def back_to_menu():
    while True:
        print()
        try_again = input("Back to menu ? (y/n): ")
        if try_again == 'y' or try_again == 'Y':
            menu()
            break
        elif try_again == 'n' or try_again == 'N':
            break
        else:
            print("Invalid choice. Try again")
            
def balance_check(c_balance):
    data = json.loads(c_balance.text)
    for d in data['data']:
        del d['account_number']
        del d['date']
        del d['description']
        del d['amount']
        del d['type']
        del d['note']
        del d['created_at']
        del d['mutation_id']
    j = json.dumps(data['data'][0], indent = 2)
    print()
    print(j)
    
    back_to_menu()

def mutation_check(mutation_tm):
    data = json.loads(mutation_tm.text)
    array_mutation = []
    frm = input('From in YYYY-MM-DD format : ')
    year, month, day = map(int, frm.split('-'))
    date_from = datetime.date(year, month, day)
    to = input('To in YYYY-MM-DD format : ')
    year, month, day = map(int, to.split('-'))
    date_to = datetime.date(year, month, day)
    for i in range(len(data['data'])):
        get_date = json.dumps(data['data'][i]['date'])
        get_date_str = get_date[1:11]
        date_time_obj = datetime.datetime.strptime(get_date_str, '%Y-%m-%d')
        if date_from <= date_time_obj.date() <= date_to:
            array_mutation.append(data['data'][i])
            
    if array_mutation != []:
        filtered_mutation = json.dumps(array_mutation, indent = 2)
        print()
        print(filtered_mutation)
    else:
        print()
        print("There are no transactions in the date range entered")
        
    back_to_menu()
    

if __name__ == '__main__':
    menu()
