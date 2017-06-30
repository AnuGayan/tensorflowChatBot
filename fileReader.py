import os

path = '/home/anusha/WSO2/NLP/WSO2ProductAgent/intents'

y = ([x for x in os.listdir(path) if x.endswith('.json')])

for name in y:
    data = open(path+"/"+name)