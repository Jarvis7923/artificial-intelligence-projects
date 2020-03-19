import numpy as np
from enum import Enum

from Board import *

from Type import *


class node:
    """
    The node class for some possible nodes in bahavior tree representation. 
    
    parameters:

        Type.NodeType type: emuerable, the type of the node.
        Type.Composite composite: enumerable, the type of composite node
        Type.Decorator decorator: enumerable, the type of decorator
        list child: list of instance of node  
        var dargs: arguments of decorator
        function: function evaluated in the node
        var args: arguments of function
    """

    def __init__(self,
                type,
                composite=None, 
                child=[],
                decorator=None, 
                dargs=None,
                function=None,
                args=None):
        # strings for prompt
        self.name = "" # node name
        self.func_info = "" # information from the function
        self.indent = 0 # indent for the prompt
        self.type = type.name
        self.composite = ""
        self.decorator = ""
        if decorator is not None:
            self.decorator = decorator.name
        
        # record the index of the running child
        self.RunningChildId = 0
        self.state = Results.SUCCESS
        # embedded timer for timer
        self.time = 1
        self.args = args
        self.dargs = dargs
        if type is NodeType.composite:
            if len(child) > 0:
                self.child = child
            else:
                raise Exception("Child of composite can not be None")
            if composite is not None:
                self.composite = composite.name
                self.NodeFunc = CompositeFunctions(composite)
            else:
                raise Exception("Composite can not be None")
        elif type is NodeType.task:
            if function is not None:
                self.NodeFunc = function
            else:
                raise Exception("Function of a task node can not be None")
        elif type is NodeType.condition:
            if function is not None:
                self.NodeFunc = function
            else:
                raise Exception("Function of a condition node can not be None")
        else:
            raise Exception("Invaid node Types")

        self.DecoFunc = DecoratorFunctions(decorator)

    def run(self):
        """
        node.run() is to evaluate the function of the node. The decorator function is executed after the main function of the node to change the state of the node accordingly
        """
        self.pre_log()
        self.NodeFunc(self)
        self.DecoFunc(self)
        self.post_log()
        return self.state

    def pre_log(self):
        """
        print the prompt before the node.run() is executed in desired format, indent 
        """
        name = self.name 
        type = self.type
        comp = self.composite
        deco = self.decorator
        if comp != '':
            comp = '<%s>'%comp
        else:
            type = '[%s]'%type
        print(self.indent*4*' ' + ' |-- ' + name + ': ' + type + ' ' + comp + ' ' + deco, end='\n')

    def post_log(self):
        """
        print the prompt after the node.run() is executed in desired format. It will show the indent, function info and the status of the node
        """
        if self.composite != '':
            print((self.indent)*4*' ' + ' |-- ' + self.name + ' ' + self.composite + " --> " + self.state_info())
        else:
            print((self.indent)*4*' ' + 5*' ' + self.func_info + " --> " + self.state_info())

        
    def state_info(self):
        """
        transfer the enumerables in Results into strings
        """
        return self.state.name

def CompositeFunctions(type):
    """
    According to the argument type, return the corresponding composite function 
    """
    if type == CompositeType.Selection:
        return Selection
    elif type == CompositeType.Sequence:
        return Sequence
    elif type == CompositeType.Priority:
        return Priority
    elif type == CompositeType.RandomSequence:
        return RandomSequence
    elif type == CompositeType.RandomSelection:
        return RandomSelection
    else:
        raise Exception("Undefined composite type")

def Selection(node):
    """
    The param "node" is the current Selection node.
    
    Children of the Selection node are evaluated in order(from left to right), it returns Returns.SUCCESS 
    as soon as one of the children succeed, otherwise it returns Returns.FAIL.
    If one of the children is RUNNING, the evaluation will start from the child node with index node.RunningChildId to the last child. 
    """
    for i in range(node.RunningChildId, len(node.child)):
        node.child[i].indent = node.indent + 1
        flag = node.child[i].run() 
        if flag is Results.SUCCESS:
            node.state = Results.SUCCESS
            node.RunningChildId = 0
            return
        elif flag is Results.RUNNING:
            node.RunningChildId = i
            node.state = Results.RUNNING
            return 
    node.RunningChildId = 0
    node.state = Results.FAIL

def Sequence(node):
    """
    The param "node" is the current Sequence node.
    
    Children of the sequence node are evaluated in order(from left to right), it returns Returns.FAIL 
    as soon as one of the children fails, otherwise it returns Returns.SUCCESS. 
    If one of the children is RUNNING, the evaluation will start from the child node with index node.RunningChildId to the last child. 
    """
    for i in range(node.RunningChildId, len(node.child)):
        node.child[i].indent = node.indent + 1
        flag = node.child[i].run() 
        if flag is Results.FAIL:
            node.state = Results.FAIL
            node.RunningChildId = 0
            return
        elif flag is Results.RUNNING:
            node.RunningChildId = i
            node.state = Results.RUNNING
            return 
    node.RunningChildId = 0
    node.state = Results.SUCCESS

def Priority(node):
    """
    The priority node is like the selection node, but the children are evaluated 
    in the order of priority regardless of the RUNNING states;

    The param "node" is the current Priority node.
    """
    for i in range(0, len(node.child)):
        node.child[i].indent = node.indent + 1
        flag = node.child[i].run() 
        if flag is Results.SUCCESS:
            node.state = Results.SUCCESS
            node.RunningChildId = 0
            return
        elif flag is Results.RUNNING:
            node.RunningChildId = i
            node.state = Results.RUNNING
            return 
    node.RunningChildId = 0
    node.state = Results.FAIL


def DecoratorFunctions(type):
    """
    According to the argument type, return the corresponding decorator function 
    """
    if type is None:
        return EmptyDecorator
    elif type == DecoratorType.Negation:
        return Negation
    elif type == DecoratorType.UntilFail:
        return UntilFail
    elif type == DecoratorType.UntilSuccess:
        return UntilSuccess
    elif type == DecoratorType.Timer:
        return Timer

def EmptyDecorator(node):
    pass

def Negation(node):
    if node.state is Results.SUCCESS:
        node.state = Results.FAIL 
    elif node.state is Results.FAIL:
        node.state = Results.SUCCESS

def UntilFail(node):
    node.func_info += "--UNTIL FAIL"
    if node.state is Results.FAIL:
        node.state = Results.SUCCESS
    else:
        node.state = Results.RUNNING

def UntilSuccess(node):
    node.func_info += "--UNTIL SUCCESS"
    if node.state is Results.SUCCESS:
        node.state = Results.SUCCESS
    else:
        node.state = Results.RUNNING

def Timer(node):
    if node.dargs is None:
        raise Exception("dargs of a Timer can not be None")
    node.func_info += "--TIME ELAPSED = %s s" % (BOARD[TIME])
    if BOARD[TIME] >= node.dargs:
        BOARD[TIME] = 1
    else:
        node.state = Results.RUNNING
        BOARD[TIME] += 1







