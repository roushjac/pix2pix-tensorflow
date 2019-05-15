# Took this script from https://stackoverflow.com/questions/52918051/how-to-convert-pb-to-tflite-format

import tensorflow as tf
gf = tf.GraphDef()   
m_file = open('models/edges2shoes_AtoB/graph.pb','rb')
gf.ParseFromString(m_file.read())

node_names = 'models/edges2shoes_AtoB/graphnames.txt'

with open(node_names, 'a') as the_file:
    for n in gf.node:
        the_file.write(n.name+'\n')

file = open(node_names,'r')
data = file.readlines()
print("output name = ")
print(data[len(data)-1])

print("Input name = ")
file.seek ( 0 )
print(file.readline())