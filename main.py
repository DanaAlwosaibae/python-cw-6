# write your code here
person={ 
    'name':'senju',
     'age': 13,
     'hobbies':['boxing','runnig','drawing']
     }
print(person.get('name'))
print(person.get('age'))
person['age']='14'
person['contry']='japan'
print(person)

person['hobbies'].append('reading')

print(len(person))

def check_hobbies(person):
    if (len('hobbies'))>=3:
        print('wow you are amazing')
        
check_hobbies(person)



