Hello, I will explain how to scrap the web banking API, but I use the moota API. So moota is a platform for checking account balances and mutations automatically. Here I use the python programming language.

Okeyy, it's the tutorial time ... ^ - ^

You must create an account on the moota platform, click <a href="https://moota.co/" target="__blank">https://moota.co/</a>.
After you create an account, you will be directed to the Moota dashboard. After that, register your bank account by clicking 'Add Bank Account'. And will be directed to the form to fill in your bank account. To be able to add your bank account, you must first buy points or you can use the 'NEWUSER' promo code for new moota users. But the moota API cannot display your account balance and mutation when you first register your bank account. The Moota will display your account balance and mutation when you make a transaction.

After you have finished registering your bank account, it's time we use the moota API click <a href="https://app.moota.co/developer/docs" target="__blank">https://app.moota.co/developer/docs</a>. Okay, this time we will display account balances and mutations.

The first step:
In order to connect with our program, we must use the base url and moota authentication. How to use it, we must use the python request library to connect with API moota and use libary json so we can process json.

```json
import requests
import json
```

And for how to use the following:

```json
import requests

headers = {
    "Accept': 'application/json",
    "Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx",
}

response = requests.get('https://app.moota.co/api/v1/balance', headers=headers)
```

Okay, because we want to display the account balance, we must use API / v1 / bank / {bank_id} / mutation / API using http request GET. 

```json
import requests

headers = {
    "Accept': 'application/json",
    "Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx",
}

response = requests.get('https://app.moota.co/api/v1/bank/{bank_id}/mutation/', headers=headers)
```

Note:
- xxxxxxxxxxxxxxx is your api moota text, you can get a token on the Moota web Settings page.
- {bank_id} Your Bank Account ID. To get an ID, please access ENDPOINT api / v1 / bank first.

Next we will make 2 menu choices:
1. Balance Check
2. Mutation Check

the code is like this
```json
def menu():
    menu = ["Balance Check","Mutation Check"]
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
```

Next we create a function to display account balances. The code is like this
```json
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
```

So the function above accepts the parameter from the response and I use the mutation endpoint, and because in moota there is no endpoint to display the account balance. So I use a mutation endpoint, because there is a key account balance. So the function above only shows the account balance.

The next function is to display mutations. The code is like this
```json
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
```

Because the moota API does not provide date parameters to display mutations based on the date range. So I use key date to be compared to the variables that I made from date and to date. And if the condition of the date range is correct, it will be filtered into an array of mutations.


Finally I made the back_to_menu function. The code is like this
```json
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
```

oupsss, I almost forgot, I want to add the last mutation feature, when selecting the check mutation menu, there are 2 choices:
1. Based on date range<br/>
2. Last mutation<br/>

add the 'last' variable to take the last mutation, like this
```json
last = requests.get('https://app.moota.co/api/v1/bank/{bank_id}/mutation/recent', headers = headers)
```

The code is like this
```json
def mutation_check(get_api_moota, last):
    menu = ['Based on date range','Last mutation']
    print()
    for i in range(len(menu)):
        print("%d. %s"%(i+1, menu[i]))
    while True:
        menu = input("Select menu [1 - 2]: ")
        if menu == '1':
            date_range(get_api_moota)
            break
        elif menu == '2':
            last_month(last)
            break
        else:
            print("Invalid choice. Try again")
            
def date_range(mutation_tm):
    data = json.loads(mutation_tm.text)
    array_mutation = []
    while True:        
        frm = input('From in YYYY-MM-DD format : ')
        to = input('To in YYYY-MM-DD format : ')
        if len(frm) == 10 and len(to) == 10:            
            year, month, day = map(int, frm.split('-'))
            date_from = datetime.date(year, month, day)
            year, month, day = map(int, to.split('-'))
            date_to = datetime.date(year, month, day)
            break
        else:
            print("Incorrect date format. Try again!")
            
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

def last_month(mutation_last):
    data = json.loads(mutation_last.text)
    j = json.dumps(data, indent = 2)
    print(j)
    back_to_menu()  
```
Output:<br/>
## Check account balance
<img src="output/1.JPG"><br/>


## Check mutations
<img src="output/3.JPG"><br/>
<img src="output/4.JPG"><br/>
<img src="output/5.JPG">
