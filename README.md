Hello, I will explain how to scrap the web banking API, but I use the moota API. So moota is a platform for checking account balances and mutations automatically. Here I use the python programming language.

Okeyy, it's the tutorial time ... ^ - ^

You must create an account on the moota platform, click <a href="https://moota.co/" target="__blank">https://moota.co/</a>.
After you create an account, you will be directed to the Moota dashboard. After that, register your bank account by clicking 'Add Bank Account'. And will be directed to the form to fill in your bank account. To be able to add your bank account, you must first buy points or you can use the 'NEWUSER' promo code for new moota users. But the moota API cannot display your account balance and transfer when you first register your bank account. The Moota will display your account balance and transfer when you make a transaction.

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
    'Accept': 'application/json',
    'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx',
}

response = requests.get('https://app.moota.co/api/v1/balance', headers=headers)
```

Okay, because we want to display the account balance, we must use API / v1 / bank / {bank_id} / mutation / API using http request GET. 

```json
import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx',
}

response = requests.get('https://app.moota.co/api/v1/bank/{bank_id}/mutation/', headers=headers)
```

Note:
- xxxxxxxxxxxxxxx is your api moota text, you can get a token on the Moota web Settings page.
- {bank_id} Your Bank Account ID. To get an ID, please access ENDPOINT api / v1 / bank first.

Next we will make 2 menu choices:
1. Balance Check
2. Mutation Check

```json
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
```