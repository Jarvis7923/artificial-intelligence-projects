AI HW4 README
------------
Shang Wang

### Dependencies

OS: Window 10
python version 3.6.9
required package: `time`, `numpy`

### How to Run

```
$ python3 test.py
```

### Expected Outputs

The results:

```
 >> total generations = 6 
 >> time elapesd = 0.05 (sec)

The expected importance value is 44
Find the solution!

items in backpack:
     #1,  #2,  #5,  #6,  #7,  #8,  #10,
 total weight: 250
 total value: 44
```

or

```
 >> total generations = 11 
 >> time elapesd = 0.37 (sec)

The expected importance value is 44
Find the solution!

items in backpack:
     #1,  #2,  #3,  #6,  #8,  #10,  #11,
 total weight: 250
 total value: 44
```

or 
```
 >> total generations = 624 
 >> time elapesd = 10.01 (sec)

The expected importance value is 45
Do not find the solution!
The suboptimal solution is

items in backpack:
     #1,  #2,  #5,  #6,  #7,  #8,  #10,
 total weight: 250
 total value: 44
```

### File list

* `genetic_algorithm_solver.py`: the implementation of the genetic algorithm solver for the knapsack problem
* `knapsack_problem.py`: defined the backpack object as well as the item object in the knapsack problem
* `test.py`: test script

### Concepts in the Gentic Algorithm

#### Define as a GA problem

The goal is to fill the backpack to make it as valuable as possible without exceeding the maximum weight (250). And the states could be a set of bools, and each bool indicates the item is in the bag or not. The goal could be interpreted as finding the local maxima in the 12-Dimensional binary space. And the objective function is the fitness function, the constraint fucntion is the sum of the weight of the items in the backpack. The problem could be solved by the Genetic Algorithm. 

#### The Genome

The chromosome in this case is: `[ item #1, item #2,  ...,  item #12 ]`.
Therefore the size of the genome is `12`. Each gene could be either true or false, indicating if the item is going to be in the backpack or not.  

Each individual is a tuple of the importance value and the its genome.  
A population is a list of individuals.

#### Fringe operations
##### Mutation

the mutation mechanism will change the value of a single gene at a random position in the chromosome. 
eg. `[1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0] => [1, 1, 1, 0, 0, 1, 0, 1, *1, 1, 1, 0]`
        
##### Crossover(Reproduce)

it will reproduce one new individual from two parent individuals. Part of the gene from both parents will form the genome of the child. In this implemetation, the gene of the child individual is split into two parts from a random position. The first half comes from the mother individual and the second is from the father. 

eg. `[ 1, 1, 1 , ..., 1 ] + [ 0, 0, 0,...,0 ] => [ 1,1 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]`


#### Culling function

The culling process will delete the some rate of the less fit population and let the rest evolute. The culling rate can be any number within (0, 1). 

