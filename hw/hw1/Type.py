""" 
This script is used for defining the node types an node state

"""
from enum import Enum



class Results(Enum):
    """
    The possible result flag of a node, or the state of a node:
        
        SUCCESS 
        FAIL 
        RUNNING
    """
    SUCCESS = 1
    FAIL = 0
    RUNNING = 2


class NodeType(Enum):
    """ 
    Enumerats for some of the types of the Nodes:

        task 
        condition  
        composite  
    """
    task = 0
    condition = 1
    composite = 2


class CompositeType(Enum):
    """ 
    Enumerats for some of the type of the Composite Node:

        Sequence  
        Selection  
        Priority  
        RandomSequence  
        RandomSelection  
    """
    Sequence = 0
    Selection = 1
    Priority = 2
    RandomSequence = 3
    RandomSelection = 4


class DecoratorType(Enum):
    """ 
    Enumerats for some of the types of the Decorators:

        Negation 
        UntilFail 
        UntilSuccess 
        Timer 
    """
    Negation = 0
    UntilFail = 1
    UntilSuccess = 2
    Timer = 3
