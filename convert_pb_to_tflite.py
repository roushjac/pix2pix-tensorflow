import tensorflow as tf
gf = tf.GraphDef()   
m_file = open('models/edges2shoes_AtoB/graph.pb','rb')
gf.ParseFromString(m_file.read())

for node in gf.node:
    print(node.name)