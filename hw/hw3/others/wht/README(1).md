Read me before you test
---

Author : Ruoxi Ren

Email : Ruoxi.Ren@tufts.edu

# File list
* `Nodes.py`
    * It defines the class of the tree node.
    * Inside the class there is a `Run` function which is called when needed.
* `Define.py`
    * It defines the return type of the `Run` function which includes failure, success and running.
    * It defines the type of the tree node which includes composite, condition and task.
* `TaskFunctions.py`
    * It defines the functions of the task node which is shown in the tree.
    * Every task node should return success or failure.
* `CompositeFunctions.py`
    * It defines the functions of the composite node which is shown in the tree.
    * Every composite node should return success, failure or running.
* `ConditionFunctions.py`
    * It defines the functions of the condition node which is shown in the tree.
    * Every condition node should return success or failure.
* `DecoratorFunctions.py`
    * It defines the functions of the decorator node which is shown in the tree.
    * * Every decorator node should return success, failure or running.
* `PrintFunctions.py`
    * It defines the function of printing the relative information of the task.
* `Blackboard.py`
    * It defines the blackboard object which contains the battery level, spot, general, dusty spot and home path.
    * It defines the tick which are assigned to zero at the beginning.
    * It defines the common test cases that may be useful in test.
    * It defines the test case which accepts users' input as blackboard elements.
* `BehaviorTree.py`
    * It defines the structure of the tree.
* `Main.py`
    * It defines the test case and the main running loop of the simulation.

# Assumptions made in the implementation
* It is supposed that the simulation of the behavior tree should run forever until the outside interruption or exceptions.
* It is supposed that all the tree node should return either success, failure or running.
* It is supposed that there should be two kinds of nodes:
    * Nodes without decorator, which is defined in `Nodes.py` as `Node`.
    * Nodes with decorator, which is defined in `Nodes.py` as `NodeWithDecorator`.
    * It is supposed that the decorator should be a characteristic of a node, not a single node. It must be defined along with other types of node (composite, task or condition). So a node with a decorator should be defined as `NodeWithDecorator`.
* It is supposed that all the task nodes, if no blackboard element is changed or the blackboard element is valid, return success; otherwise failure is returned.
* It is supposed that the `Until Fail` decorator in the graph should be actually a `Until Succeed` decorator. The professor told me I could do that. It means that when the composite node returns success, then success is returned; otherwise running is returned.
    * In order to restore the actual situation as much as possible, some modification is made on the behavior tree.
    * Logically, if the decorator is `Until Fail` and every child task returns success when completes, the `DONE GENERAL` task would never be executed.
* It is supposed that 1% of battery should be consumed in every loop.
* It is supposed that the node with `Timer` decorator will refer to a timer as `Tick` element in the blackboard and receive a input of the execution time as `Clock`. The `Tick` element would be reset to zero if the task had been executed for enough times which is defined by `Clock`.
* It is supposed that `DOCK` task change the battery level to 100% and change the `Tick` to 0. It means that when it gets charged, the old timer is no longer in use, so all the task has to start over again.
* It is supposed that except the task nodes, the condition nodes and the priority node, no information about the composite nodes should be printed out.
* It is supposed that the print information should be in one of the formats below:
    * `[Task or Condition Node] Relative Blackboard value Information`
        * Example: `[BATTERY < 30%] BatteryLevel : 50`
    * `(Return State) Task or Condition Node`
        * Example: `(Running) CLEAN SPOT`
    * `(Return State){Number of Time already spent} Task or Condition Node`
        * Example: `(Success){4 s} CLEAN SPOT`
        * This should print the state of the task without taking the decorator into account.
        * The state of the task after this loop should be accessible via the information print in the format `(Return State) Task or Condition Node`


# Test
## Development environment
* Language: Python 3.6.4 64-bit
* Text editor:Visual Studio Code
* Operating System: macOS Mojave 10.14
## How to test
* Run `Main.py`
    * Command: `python3 Main.py`
* Test cases 
    * The default test case is self-defined in which user must input the value for battery level (integer), spot (boolean), general (boolean), dusty spot (boolean) and home path (string).
    * Users can change the test cases in `Main.py`. Some available test cases are listed below:
        * `TestCase.SpotCleaning`
            * battery level = 70
            * spot = true
            * general = false
            * dusty spot = false
            * home path = "Go to find the home path"
        * `TestCase.GeneralCleaning`
            * battery level = 70
            * spot = false
            * general = true
            * dusty spot = false
            * home path = "Go to find the home path"
        * `TestCase.DustySpotCleaning`
            * battery level = 70
            * spot = false
            * general = true
            * dusty spot = true
            * home path = "Go to find the home path"
        * `TestCase.Charging`
            * battery level = 20
            * spot = false
            * general = false
            * dusty spot = false
            * home path = "Go to find the home path"
        * `TestCase.DoNothing`
            * battery level = 50
            * spot = false
            * general = false
            * dusty spot = false
            * home path = "Go to find the home path"
        * `TestCase.SelfDefine`
            * All the elements are defined by users
## Example for the output information
* Settings:
    * battery level = 75
    * spot = false
    * general = true
    * dusty spot = false
    * home path = "Go to the right corner"
* Output Information
```
Pleas input the value for Battery (an integer from 1 to 100):75
Please input the value for Spot (true or false):false
Please input the value for General (true or false):true
Please input the value for Dusty Spot (true or false):false
Please input the value for Home Path:Go to the right corner

-------------------------  This is the test settings  -------------------------
                           Battery Level  : 75
                           Spot           : False
                           General        : True
                           Dusty Spot     : False
                           Home Path      : Go to the right corner
-------------------------------------------------------------------------------

......  Begin to simulate
------------------- 1 Tick -------------------
[BATTERY < 30%] BatteryLevel : 75
(Failure) BATTERY < 30%
(Failure) SPOT
(Success) GENERAL
[Battery >= 30%] BatteryLevel : 75
(Success) Battery >= 30%
(Failure) DUSTY SPOT
(Success) CLEAN
[DONE GENERAL] I have finished general cleaning!
(Success) DONE GENERAL
(Success) PRIORITY ROOT
------------------- 2 Tick -------------------
[BATTERY < 30%] BatteryLevel : 74
(Failure) BATTERY < 30%
(Failure) SPOT
(Failure) GENERAL
Zzzzz...
(Success) DO NOTHING
(Success) PRIORITY ROOT
------------------- 3 Tick -------------------
[BATTERY < 30%] BatteryLevel : 73
(Failure) BATTERY < 30%
(Failure) SPOT
(Failure) GENERAL
Zzzzz...
(Success) DO NOTHING
(Success) PRIORITY ROOT
Terminated: 15
```