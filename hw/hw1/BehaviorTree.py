"""
define the whole behavior tree in a dictionary
"""

from Node import *
from TaskFunctions import *
from ConditionFunctions import *

# a list of contains a string of the every node's name 
node_names = ["n%s"%i for i in range(23)]
# a list of instance of node class
n = list(node_names)

# instantiate every node in the behavior tree
n[22] = node(NodeType.task, function=clean_spot,
           decorator=DecoratorType.Timer, dargs=3)
n[21] = node(NodeType.condition, function=dusty_check)
n[20] = node(NodeType.task, function=clean)
n[19] = node(NodeType.composite, composite=CompositeType.Sequence,
           child=[n[21], n[22]])
n[18] = node(NodeType.composite, composite=CompositeType.Selection,
           child=[n[19], n[20]])
n[17] = node(NodeType.condition, function=battery_check,
           args=30, decorator=DecoratorType.Negation)
n[16] = node(NodeType.task, function=done_general)
n[15] = node(NodeType.composite, composite=CompositeType.Sequence,
           child=[n[17], n[18]], decorator=DecoratorType.UntilFail)
n[14] = node(NodeType.composite,
           composite=CompositeType.Sequence, child=[n[15], n[16]])
n[13] = node(NodeType.condition, function=general_check)
n[12] = node(NodeType.task, function=done_spot)
n[11] = node(NodeType.task, function=clean_spot,
           decorator=DecoratorType.Timer, dargs=3)
n[10] = node(NodeType.condition, function=spot_check)
n[9] = node(NodeType.composite,
          composite=CompositeType.Sequence, child=[n[13], n[14]])
n[8] = node(NodeType.composite, composite=CompositeType.Sequence,
          child=[n[10], n[11], n[12]])
n[7] = node(NodeType.task, function=dock)
n[6] = node(NodeType.task, function=go_home)
n[5] = node(NodeType.task, function=find_home)
n[4] = node(NodeType.condition, function=battery_check, args=30)
n[3] = node(NodeType.task, function=do_nothing)
n[2] = node(NodeType.composite,
          composite=CompositeType.Selection, child=[n[8], n[9]])
n[1] = node(NodeType.composite, composite=CompositeType.Sequence,
          child=[n[4], n[5], n[6], n[7]])

# the root node of the behavior tree
n[0] = node(NodeType.composite,
          composite=CompositeType.Priority, child=[n[1], n[2], n[3]])

# a dict with element of {node name: node instance} 
tree = {}
for i in range(len(node_names)):
    tree[node_names[i]] = n[i]
    n[i].name = node_names[i]

