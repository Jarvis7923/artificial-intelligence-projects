class Conflict:
    """
    This class defines the structure of the conflict set. It includes:
      1. step: the step in which the conflict occurs
      2. index: the index of the conflict cell
      3. value: the value of the conflict cell
    """
    def __init__(self, step, index, value):
        """
        Initialize the conflict cell with given parameters
        """
        self.step = step
        self.index = index
        self.value = value
    
    def __eq__(self, other):
        """
        Override the equal method to make it easier to sort the list of conflict
        """
        return self.step == other.step

    def __hash__(self):
        """
        Override the hash method to make it easier to sort the list of conflict
        """
        return hash(('step',self.step))


def takeConflictKey(conflict):
    """
    take the step of the conflict set when it is sorted
    """
    return conflict.step