
AI HW2 README
------------
Shang Wang;  

### Dependencies

python version 3.6.9
required package: time, numpy

### How to Run

```
$ python3 test.py
```

### Expected Outputs

```
...
=========start!=========

---------------
`A*` Algorithm
---------------
heuristic function: GAP_DIST
cost function: UNIFORM_STEP_COST
progress: 50
  >> solution:
     state:     5  7  4  1  2  6  3
     |-action                 ^
     state:     5  7  4  1  2  3  6
     |-action        ^
     state:     5  7  6  3  2  1  4
     |-action     ^
     state:     5  4  1  2  3  6  7
     |-action  ^
     state:     7  6  3  2  1  4  5
     |-action        ^
     state:     7  6  5  4  1  2  3
     |-action              ^
     state:     7  6  5  4  3  2  1
  >> total iteration: 75
  >> backward cost: 6
  >> number of nodes in frontier: 284
  >> time elapsed(s): 0.08477377891540527
---------------
`UCS` Algorithm
---------------
heuristic function: NONE
cost function: UNIFORM_STEP_COST
progress: 5500
  >> solution:
     state:     5  7  4  1  2  6  3
     |-action                 ^
     state:     5  7  4  1  2  3  6
     |-action        ^
     state:     5  7  6  3  2  1  4
     |-action     ^
     state:     5  4  1  2  3  6  7
     |-action  ^
     state:     7  6  3  2  1  4  5
     |-action        ^
     state:     7  6  5  4  1  2  3
     |-action              ^
     state:     7  6  5  4  3  2  1
  >> total iteration: 5512
  >> backward cost: 6
  >> number of nodes in frontier: 3934
  >> time elapsed(s): 27.857924222946167
...

```

### File list

* `Astar_algorithm.py`: implementation of `A*` algorithm, definition of nodes, frontier, cost, and heuristic function 
* `Settings.py`: contains a dict of public variables named `SETTINGS`, and types cost/heuristic functions
* `test.py`: test file, user could overwrite the config in `SETTINGS` to test the performance of different combination of cost/heuristic function and different initial state

### Ideas of the regular problem and bonus problem

`A*` is a more integrated algorithm compared with Greedy best-first search and Uniform cost search(`UCS`) since it takes advantage of both real cost and heuristic cost(backward cost and forward cost). 
`UCS` is more like the degrade version of `A*`.
Therefore, the easiest way to implement a `UCS` is to simply set the heuristic value in `A*` to be 0 every time. 

### Notes about the runtime

If the number of pancakes are bigger than 8, `UCS` will take a significant long time to get the solution. The default test array is modified into a rather easy case in terms of the runtime, just to demonstrate the difference of performance between `A*` and `UCS`. 

### Heuristic function

There are 3 heuristic functions in the code:

* gap heuristc: The gap heuristic in the reference, which is the fastest way in our experiments. According to the reference, to gurentee the admissibility of `A*` while using gap heuristic, the cost of each flip must be bigger than 1.
* euclidean distance: the euclidean distance of current state and the goal state, which takes rather long exploration in our searching algorithm. Sometimes it might jeopardize the performance. The optimality and completeness are not guarenteed by any proof, so this hueristic function is just used for comparison.
* empty heuristic: returns 0 at any state. It cooresponds to the uniform cost search.


### Cost function

There are two cost function or backward cost types in the code:

* uniform step cost: each flip has an identical cost 1 
* step plus flip number cost: the cost considered the number of pancakes to flip at each step. Numerically, cost = 1 + num of fliped pancakes/(total number of pancakes * 5). 

In the case of using gap heuristic, the step cost better be as small as possible but it still need to be greater than 1 to ensure the admissibility.

### Key code explaination

#### A* implementation

```python
front = frontier(node(init_state)) # put the first node into the frontier
iter = 0
while (True):
    # if the frontier has no zero element, return fail
    if front.length == 0: 
        end = time.time()
        return (False, iter, None, 0, end-start)
    n = front.top_node # extract the node with lowest cost
    if n.state == SETTINGS[GOAL]: 
        end = time.time()
        return (n.backtrack(), iter, n.total_cost, front.length, end-start) # goal test
    for i in range(len(n.state)-1):
        front.add(node(state=flip(n.state, i), parent=n, action=i))
    iter += 1

```

#### Node class

Each node of the search tree is implemented as a node object, which will read the configuration in `SETTINGS` and choose the cost, heuristc function accordingly. Parameter `action` means the action we take to reach the current node from its parent. eg. to reach the child node [1,2,4,3] from parent [1,2,3,4], we need to flip the pancakes above(contains) the index `2`(starts at 0), this action `2` will be stored in the child node.  

There is also a public method in node class called `backtrack`, it can recursively get the parent states and action unless it reacheed the root node of the search tree.

#### Frontier class

A frontier object record the frontier of the search tree as a list of node object. Each time user do `add(node)`, the adding process will automatically check if `node` has been visited. If so, it will drop the node with higher backward cost in the frontier.  

There is also a public property called `top_node`. While the property is called, the frontier will hunt down the node with the smallest backward cost.