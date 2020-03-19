"""
defined the backpack object as well as the item object in the knapsack problem

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""

from typing import List
States = List[bool]


class backpack:
    """
    The backpack could contain items from number 1 to 12, each item has a weight and an importance value. The state of the backpack is which items to put into the backpack so that the total weight of if do not exceed a maximum weight it can bear.   
    
    the states of the backpack is a list of 12 booleans which indicates which items are going to in the bag or not.
    
    [#1:bool, #2:bool, ... , #12:bool] 

    Public Methods
    ------
        total weight: calculate the total weight according to the state 
        total value: calculate the total value according to the state 

    """

    def __init__(self,
                 max_weight: int,
                 ) -> None:
        """

        """
        self._init_items()
        self.max_weight = max_weight
        self.n_items = len(self._items)

    def _init_items(self) -> None:
        """
        initialize each of the items in the knapsack problem
        """
        self._items = {
            0: _item(20, 6),
            1: _item(30, 5),
            2: _item(60, 8),
            3: _item(90, 7),
            4: _item(50, 6),
            5: _item(70, 9),
            6: _item(30, 4),
            7: _item(30, 5),
            8: _item(70, 4),
            9: _item(20, 9),
            10: _item(20, 2),
            11: _item(60, 1)
        }

    def total_weight(self, s: States) -> int:
        """
        get the total weight of a certain state
        
        Arguments:
        -----
            s: the state of the knapsack problem

        Returns:
        -----
            the total weight of the current state 

        """
        sum = 0
        for i in range(len(s)):
            if s[i]:
                sum += self._items[i].weight
        return sum

    def total_value(self, s: States) -> int:
        """
        get the total importance value of a certain state

        Arguments:
        -----
            s: the state of the knapsack problem

        Returns:
        -----
            the total importance value of the current state 

        """
        sum = 0
        for i in range(len(s)):
            if s[i]:
                sum += self._items[i].value
        return sum


class _item:
    """
    defined a item object.

    Public Property
    ------
        weight：the weight of the item
        value: the importance value of the item
    """

    def __init__(self, w: int, v: int) -> None:
        self.weight = w
        self.value = v


