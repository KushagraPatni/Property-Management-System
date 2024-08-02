from block import BlockChain
from models import Property, User
from models import Transaction
import default
import random
from hmac_ import *
import json


# initializing the blockchain
blockchain = BlockChain()


def verify_user(username, password):

    # ALICE
    random_challenge = generate_challenge()

    #BOB
    bit = random.randint(0, 1)

    #ALICE
    response = create_response(random_challenge, bit, password)

    for user in User.users:
        if user.username == username:
            curr_user = user
            break

    #BOB CHECKS
    expected_response = create_response(random_challenge, bit , curr_user.password)
    return verify_response(expected_response, response)

    # return False


def register():

    print('------------------------------------------------------------------ \n')
    print('Enter a username and password:')
    username = str(input("Username: "))

    # check if the username already exists
    for user in User.users:
        if user.username == username:
            print("Username already exists, choose another one \n")
            register()
            return

    password = str(input("Password  : "))

    if (username != '' and password != ''):
        User(username, password)
        print(f'\n {username} registered successfully!')
        return
    else:
        print("\n Username and/or password can't be empty, try again \n")
        register()


def viewWealth():
    
        print('------------------------------------------------------------------ \n')
        print('Enter the username of the user whose wealth you want to see: ')
        username = str(input())
    
        user_found = False
        for user in User.users:
            if user.username == username:
                user_found = True
                curr_user = user
    
        if not user_found:
            print("The specified user does not exist \n")
            return
        
        print('Enter your password  : ')
        pass1 = str(input())

        if(verify_user(username, pass1) == False):
            print("\n You have input the incorrect pin!")
            return

        print(f'\n {username} has {curr_user.wealth} coins')

def verify_transaction(transaction , current_owner, curr_user, property_chosen):
    random_challenge = generate_challenge()
    bit = random.randint(0, 1)

    secret = json.dumps(transaction.to_string())

    response = create_response(random_challenge, bit, secret)


    transaction_expected = Transaction(
        current_owner, curr_user, property_chosen)
    
    secret_expected = json.dumps(transaction_expected.to_string())

    expected_response = create_response(random_challenge, bit , secret_expected)
    return verify_response(expected_response, response)

    

def buy():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    
    if not user_found:
        print("\n User does not exist, create a user")
        return

    print('Enter your password  : ')
    pass1 = str(input())

    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return

    print('\n Enter the ID of the property you want to buy(-1 to go back): ')
    propertyId = int(input())

    if(propertyId == -1):
        return

    if(propertyId >= len(Property.properties)):
        print('This Property Does not exist, see below the valid properties \n')
        Property.viewProperties(Property)
        buy()
        return

    property_chosen = Property.properties[propertyId]

    if property_chosen.owner.username == username:
        print("You already own this property")
        return

    if (curr_user.wealth < property_chosen.amount):
        print("Insufficient funds")
        return

    if property_chosen.owner is not None:
        current_owner = property_chosen.owner
        current_owner.remove_property(property_chosen)
    else:
        current_owner = None

    transaction = Transaction(
        current_owner, curr_user, property_chosen)
    
    if(verify_transaction(transaction, current_owner, curr_user, property_chosen) == False):
        current_owner.add_property(property_chosen)
        return
    else:
        print("Transaction Verified, Adding to mine pool")

    property_chosen.transaction_history.append(transaction)
    prev_block = blockchain.last_block()
    block = blockchain.new_block(prev_block['hash'], transaction)

    # blockchain.mine_block_POW(block)

    curr_user.add_property(property_chosen)

    print(
        f"\n {curr_user.username} bought {property_chosen.name} successfully! \n {blockchain.last_block()['merkle_root']}")


def transaction_history():

    print('------------------------------------------------------------------ \n')
    print("Enter the ID of the property whose transaction history you want to see: ")
    propertyId = int(input())

    if propertyId >= len(Property.properties):
        print('Invalid selection, choose again \n')
        transaction_history()

    property_chosen = Property.properties[propertyId]

    for transaction in property_chosen.transaction_history:
        print(f'''
            Buyer: {transaction.buyer.username},
            Seller: {transaction.seller.username}
            Timestamp: {transaction.timestamp},
            TxnID: {transaction.transactionId}
        \n''')


def show_assets():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    else:
        print(f'\n -> Properties owned by {username} are:')
        curr_user.get_assets()


def addMoney():
    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    
    print('Enter your password  : ')
    pass1 = (input())

    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return

    print('Enter the amount you want to add: ')
    amount = int(input())
    curr_user.addMoney(amount)
    print(f'\n {amount} coins added to {username}')
        
    print(f'\n {username} now has {curr_user.wealth} coins')




def register_property():

    print('------------------------------------------------------------------ \n')
    print('Enter your username: ')
    username = str(input())

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    
    print('Enter your password  : ')
    pass1 = (input())

    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return

    
    else:
        print('Enter the name of the property:')
        name = input('')
        print('Enter the price of the property:')
        price = int(input(''))
        new_property = Property(name, price)
        curr_user.register_property(new_property)
        print(
            f'\n {new_property.name} registered in the system by {curr_user.username}')

def viewUser():
    username = input("Enter Username ")

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    
    print('Enter your password  : ')
    pass1 = (input())

    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return

    property = blockchain.get_transaction_by_user(username)

    for property_chosen in Property.properties:
        for transaction in property_chosen.transaction_history:
            if(transaction.buyer.username == username or transaction.seller.username == username):
                print(f'''
                    Property Name : {transaction.propertyName}
                    Buyer: {transaction.buyer.username},
                    Seller: {transaction.seller.username}
                    Timestamp: {transaction.timestamp},
                    TxnID: {transaction.transactionId}
                \n''')


def viewAllUser():
    for user in User.users:
        print(user.username)


def deregister():
    username = input("Enter Username ")

    user_found = False
    for user in User.users:
        if user.username == username:
            user_found = True
            curr_user = user

    if not user_found:
        print("The specified user does not exist \n")
        return
    
    print('Enter your password  : ')
    pass1 = (input())

    if(verify_user(username, pass1) == False):
        print("\n You have input the incorrect pin!")
        return
    
    propertyId = int(input("Enter Property ID to deregister "))
    property_chosen = Property.properties[propertyId]

    if(username != property_chosen.owner.username):
        print("You do not own this property")
        return
    
    Property.deregister(Property ,propertyId)

    print(f'{property_chosen.name} has been deregistered by {username}')




# main loop
while True:
    #3. View transaction history for a property
    print(""" \n ------------------------------------------------------------------ \n
    Choose an action:
        1. Register User
        2. See all users
        3. Register property
        4. De-Register Property
        5. View All Properties
        6. Buy Property
        7. View assets owned by a user
        8. View Balance
        9. Add Money
        10. ViewUser (Transaction History)
        11. Exit
    """)

    choice = (input())
    try:
        choice = int(choice)
    except:
        print("Invalid choice, choose again")
        continue

    if (choice == 1):
        register()
    elif (choice == 6):
        Property.viewProperties(Property)
        buy()
    elif (choice == 4):
        deregister()
        #transaction_history()
    elif (choice == 7):
        show_assets()
    elif (choice == 3):
        register_property()
    elif (choice == 5):
        Property.viewProperties(Property)
    elif (choice == 8):
        viewWealth()
    elif(choice == 10):
        viewUser()
    elif(choice == 9):
        addMoney()
    elif(choice == 2):
        viewAllUser()        
    elif (choice == 11):
        break
    else:
        print("Invalid choice, choose again")

