"""
Test script for examine the performance of the genetic algorithm. 

author: shang wang
id: 1277417
email: swang27@tufts.edu

"""


import genetic_algorithm_solver as ga


if __name__ == "__main__":
    sol = ga.solver(n_population=100,
                    p_mutate=0.5,
                    timeout=10,
                    expected_value=44,
                    cull_rate= 0.5, 
                    max_weight=250)
    res = sol.run()


