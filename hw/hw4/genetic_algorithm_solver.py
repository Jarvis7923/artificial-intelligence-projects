"""
The genetic algorithm solver for the knapsack problem. 

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""

import numpy as np
import time

from knapsack_problem import *

# Type annotations
from typing import List, Tuple, Callable

Individual = Tuple[int, States]
Population = List[Individual]


class solver:
    """
    The chromosome in this case is:
        [#1 #2 ... #12].
    Therefor the size of the genome is 12. Each gene could be either true or false, indicating if the item is going to be in the backpack or not.  

    Each individual is a tuple of the importance value and the its genome.  
    A population is a list of individuals.

    Arguments
    ------
        n population: the number of the individuals in a population
        p mutate: the propability of the mutation
        timeout: the maximum time spent on solving the problem by the solver
        expected value: the acceptable importance value for the knapsack problem
        cull rate: the rate of disposed individual in the total population
        max weight: the maximum weight of the backpack 

    """

    def __init__(self,
                 n_population: int = 200,
                 p_mutate: float = 0.1,
                 timeout: int = 5,
                 expected_value: int = 44,
                 cull_rate: float = 0.5,
                 max_weight: int = 250
                 ) -> None:
        self._np = n_population
        self._p_mutate = p_mutate
        self._timeout = timeout
        self._expected_value = expected_value
        self._cull_rate = cull_rate

        self._t0 = time.time()
        self._bp = backpack(max_weight)

    def run(self,
            p: Population = None,
            fn: Callable[[States], int] = None
            ) -> Individual:
        """ 
        run the solving process 

        Arguments:
            p: the initial population
            fn: the fitness function name which takes the states as argument and returns a fitness value 
        Returns:
        -----
            The best individual according to the fiteness function
        
        """
        if fn is None:
            fn = self._fitness_fn
        if p is None:
            p = self._init_popluation(fn)
        return self._genetic_algorithm(p, fn)

    def _genetic_algorithm(self,
                           p: Population,
                           fn: Callable[[States], int]
                           ) -> Individual:
        """
        the implementation of the genetic algorithm given a initial population and a fitness function

        Arguments:
        -----
            p: the initial population
            fn: the fitness function

        Returns:
        -----
            The best individual
        
        """
        gen = 0
        while not(self._check_solution(p) or self._t_elpased > self._timeout):
            new_p = []
            p = self._cull(p)
            for i in range(self._np):
                c = self._reproduce(self._random_selection(p), fn)
                if np.random.random() < self._p_mutate:
                    c = self._mutate(c, fn)
                new_p.append(c)
            p = sorted(new_p, reverse=True)
            gen += 1
            print("\r\33[95m >> total generations = %s \33[0m" % (gen), end="")
        print("\n\33[95m >> time elapesd = %.2f (sec)\33[0m" % (self._t_elpased))
        self.show_result(p[0])
        return p[0]

    @property
    def _t_elpased(self) -> float:
        """
        time spent in the solving process

        Returns:
        -----
            time elapsed
        """
        return time.time() - self._t0

    def _init_popluation(self,
                         fn: Callable[[States], int],
                         ) -> Population:
        """
        randomly initialize a population with `self._np` individuals

        Arguments:
        ------
            fn: the fitness function

        Returns:
        ------
            A random population with size `self._np`
        """
        p = []
        for ele in range(self._np):
            s = [np.random.randint(0, 1) for i in range(self._bp.n_items)]
            p.append((fn(s), s))
        return p

    def _reproduce(self,
                   parents: Tuple[Individual],
                   fn: Callable[[States], int],
                   ) -> Tuple[int, List[bool]]:
        """
        reproduce a new individual from two parent individuals.

        Arguments
        ------
            parents: a tuple of two parent individuals
            fn : the fitness function

        Returns
        -----
            a child individual

        """
        (x, y) = parents
        n = np.random.randint(len(x[1]))
        s = x[1][:n] + y[1][n:]
        return (fn(s), s)

    def _mutate(self,
                c: Individual,
                fn: Callable[[States], int],
                ) -> Individual:
        """
        the mutation mechanism, it reverse the value of a gene at a random position
        
        Arguments
        ------
            c: the individual before mutation
            fn : the fitness function

        Returns
        -----
            a individual after mutation
        
        """
        n = np.random.randint(len(c[1]))
        c[1][n] = int(not c[1][n])
        return (fn(c[1]), c[1])

    def _random_selection(self,
                          p: Population
                          ) -> Tuple[Individual]:
        """
        randomly select two parent individuals to mate

        Arguments
        ------
            p: the population
            fn : the fitness function

        Returns
        -----
            a tuple of two parent individuals
        
        """
        l = np.array([ele[0] for ele in p])
        s = np.sum(l)
        i, j = np.random.choice(len(l), 2, replace=False) if s == 0 else np.random.choice(
            len(l), 2, replace=False, p=l/s)
        return p[i], p[j]

    def _fitness_fn(self,
                    s: States
                    ) -> int:
        """
        a possible fitness function, it returns the total importance value of the current state of the backpack if the total weight did not exceed the max weight. It returns 0 if the total weight busts.

        Arguments:
        ------
            s: states

        Returns
        ----
            the fitness value
        
        """
        return 0 if self._bp.total_weight(s) > self._bp.max_weight else self._bp.total_value(s)

    def _check_solution(self,
                        p: Population
                        ) -> bool:
        """
        check if the individual with the largest fitness value in the population satisfied the expected fitness value
        
        Arguments:
        ------
            p: Population

        Returns
        ----
            bool flag
        
        """
        return p[0][0] >= self._expected_value

    def _cull(self,
              p: Population
              ) -> Population:
        """
        cull a certain percentage of the population with lower fitness value.
        
        Arguments:
        ------
            p: Population

        Returns
        ----
            Population after culling
            
        """
        return p[:int(len(p)*(1-self._cull_rate))]

    def show_result(self, i):
        v, s = i
        n = "\nThe expected importance value is %s"%self._expected_value
        n += "\nFind the solution!\n" if self._check_solution([i]) else "\nDo not find the solution!\nThe suboptimal solution is\n"
        n += "\nitems in backpack: \n    "
        for ele in range(len(s)):
            if s[ele]:
                n += " #%s, "%(ele+1)
        n += "\n total weight: %s"%self._bp.total_weight(s)
        n += "\n total value: %s\n"%v
        print(n)