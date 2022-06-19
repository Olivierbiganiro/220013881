
# write your code here
list= int(input("Enter the number friends joining (including you):\n"))
if list<=0:
   print("No one is joining for the party")
else: 
    list_dict ={}
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(1,list+1):
        y = input()
        list_dict.update({y:0})
    print(list_dict)
    
    #END OF PROJECT OF STAGE 1
    
    import random
print("Enter the number of friends joining (including you):")
number = input()
if int(number) == 0 or int(number) < 0:
    print("No one is joining for the party")
else:
    people_invited = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(number)):
        names = input()
        people_invited.update({ names: 0})
    print("Enter the total bill value:")
    bilamount = input()
    names_of_friends = list(people_invited.keys())
    bill_amount_for_every_one = float(float(bilamount) / int(number))
    for b in names_of_friends:
        people_invited.update({b: round(bill_amount_for_every_one, 2)})
    print(people_invited)
    
    
    #END OF STAGE 2
    
    import random
print("Enter the number of friends joining (including you):")
numbe= input()
if int(numbe) == 0 or int(numbe) < 0:
    print("No one is joining for the party")
else:
    people_invited = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(numbe)):
        names_of_invited = input()
        people_invited.update({ names_of_invited: 0})
    print("Enter the total bill value:")
    bilamount = input()
    friend_name = list(people_invited.keys())
    bill_amount_for_every_one = float(float(bilamount) / int(numbe))
    for b in friend_name:
        people_invited.update({b: round(bill_amount_for_every_one, 2)})
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if(response.upper() == "YES"):
        random_lucky = random.choice(friend_name)
        print("{} is the lucky one!".format(random_lucky))
    else:
        print("No one is going to be lucky")

        
            #END OF STAGE 3
          
          import random
print("Enter the number of friends joining (including you):")
number = input()
if int(number) == 0 or int(number) < 0:
    print()
    print("No one is joining for the party")
else:
    friends_invited = {}
    print("Enter the name of every friend (including you), each on a new line:")
    
    for a in range(int(number)):
        friend_name = input()
        friends_invited.update({ friend_name: 0})  
    print("Enter the total bill value:")
    amount = input()
    friends_names = list(friends_invited.keys())
    amount_for_every_one = int(amount) / int(number)
    for b in friends_names:
        friends_invited.update({b: round(float(amount_for_every_one), 2)})
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    
    choice_answer = input()
    if choice_answer.upper() == "YES":
        lucky_friend = random.choice(friends_names)
        print("{} is lucky one!".format(lucky_friend))
        for c in friends_names:
            if c == lucky_friend:
                friends_invited.update({c: 0})
            else:
                amount_for_every_one = float(amount) / float((int(number) - 1))
                friends_invited.update({c: round(float(amount_for_every_one),2)})
        print(friends_invited)
    else:
        print("No one is going to be lucky")
        print(friends_invited)

  #END OF STAGE 4
