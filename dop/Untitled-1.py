"""
second_per_hour=60**3
second_per_day=second_per_hour*24
print (second_per_day/second_per_hour)
print (second_per_day//second_per_hour)
yearsList=[1994,1995.1996,1998,1999]
print (yearsList)
print (yearsList[3])
a=len(yearsList)
print (a)
print(yearsList[-1])
things=["mozzarella", "cinderella", "salmonella"]
things[1]= things[1].capitalize()
things[0]=things[0].upper()
del things[2]
print (things)
suprise=["Groucho", 'Chico','Harpo']
n=suprise[2].lower()
suprise[2]=n[::-1].capitalize()
print(suprise)
"""

"""
#e2f={"dog":'chien', 'cat':'chat', 'walrus':'morse'}
#print (e2f)
#print(e2f['walrus'])
#b =dict(zip(e2f.values(), e2f.keys()))
#f2e=b.copy()
#f2e = dict(reversed(item) for item in e2f.items()).copy() 
#f2e{value: key for key, value in e2f.items()}
#f2e{v:k for k , v in e2f.items()}
#print (f2e)10
#print (f2e.keys())
#print(f2e['chien'])
#print(set(e2f.keys()))
"""

cats = ['Henri', 'Grumpy', 'Lucy']
octopi={}
emus={}
animals = {'cats':cats, 'octopi':octopi, 'emus':emus}
plants={}
other={}
life = {'animals': animals, 'plants': plants,'other': other}
print(life.keys())
print(animals.keys())
print(life['animals'])
print(life[animals ['cats']])
