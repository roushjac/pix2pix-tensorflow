# Taken from a stackoverflow thread - https://stackoverflow.com/questions/45823662/can-we-use-pbtxt-instead-of-pb-file-in-using-tensor-flow-model
# Entering filenames/paths into script directly, could make more robust
# by using command line arguments instead

import tensorflow as tf
from google.protobuf import text_format

with open('/models/edges2shoes_AtoB/graph.pbtxt') as f:
  txt = f.read()
gdef = text_format.Parse(txt, tf.GraphDef())

tf.train.write_graph(gdef, '/models/edges2shoes_AtoB', 'graph.pb', as_text=False)