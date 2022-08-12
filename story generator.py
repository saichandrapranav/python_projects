import random
when = ['today','yesterday','august 12','A long time ago']
who = ['a cat','a dog','I','a rabbit']
residence = ['india','america','israel','russia']
went = ['park','coffe shop','library','arcade']
happened = ['drank coffe','solved a mystery','read a book','played videogames']
print(random.choice(when) + ' , ' + random.choice(who) + ' from ' + random.choice(residence) + ' went to ' + random.choice(went) + ' and ' + random.choice(happened))