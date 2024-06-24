from contact_list import ContactList

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]


my_friends_list = ContactList('My Friends', friends)
print(my_friends_list)
(my_friends_list.add_contact({'name': "Triton", 'number': "111-1111"}))
print(my_friends_list)
my_friends_list.remove_contact('Bob')
print(my_friends_list)

my_work_buddies = ContactList('Work Buddies', work_buddies)
print(my_work_buddies)
friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)