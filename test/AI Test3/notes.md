AI test3
-----

### Probability theory

what is the Decision theory:
* probability theory: agent's beliefs 
* utility theory: agent's desires
* defining the best action that maximize the expected utility

What can be tackled by the probability theory
* Laziness: failure to enumerate all the expectations, and the qualifications of an anction, etc
* Theoretical ignorance: the model is too complex to build
* practical ignorance: it's impossible to find all the relevant facts or initial conditions  

What are the features of the Bayesian or Subjective probability?
* it relates the pobability of a proposition to one's knowledge
* probablities assert a belief but not a fact
* probability of a proposition changes with new evidence or knowledge

What is the probability of a random variable:


what is the prior:
* Each of the variable's value has an probability called the prior that corresponds to the belief before the arrival of any evidence.

what is the probabilistic distribution:
* a table of values of the random variable and its probability

What is the atomic event in probability theory:
* a completely specification of the values of the random variables of interest, a point in the joint distribution.

The set of all the atomic event has two properties:
* mutually exhaustive
* mutually exclusive

what is a joint distribution over a set of random variables:
* a table that specified the probability of each of the atomic event or the probability of each of the assignments of variables happens at the same time

what is a probabilistics model: 
* a joint distribution over a set of random variables


What is a marginal distrubution:
* a sub-table of joint distribution that some of the variables are eliminated

What is a conditional probability:
* the likelihood that one event a will occur if b occurs

Conditional product rule:

Bayes's rule:

some thing to be notices:
* tests and events are seperate things
* tests are always flawed(false positive and false negative)
* tests give us the test probability, but not the real probability
* false positive skew results for rare event




What is probabilistic inference:
* it computes the a desired probability from other known probabilites
* it starts with conditionbal probabilities that represent some belief given evidence
* probabilities is updated with new evidences


what types of variables could be used in a conditional query:
* given a probabilistic model:
  * evidence variables in the query conditioned upon
  * query variables
  * hidden variables

chain rule


Whats the sensitivity and what is the specificity:
* sensitivity: actual positive that are correctly identified by the test
* actual negative that are correctly identified by the test 



What is baysian networks
* it's called belief networks or more formally graphical models as well
* it's a simplified model of how some portion of the world work
* better for describe joint probabilities
* using local conditional probabilities among random variables to calculate the complex joint dist
* local interactions will chain together to give the global, indirect interations

What is a node in Baysian networks
* random variable with its domain
* usually one node per random variable
* can be assigned(observed) or unassigned(unobserved)

What do the arcs do in the bayesian networks: 
* nodes without arcs are the independent variables
* arcs encodes the conditional probability
* a directed, acyclic graph that encodes conditional independence

Features of bayesian networks:
* not have to be causual. 
* if a bayesian network do reflect a true causal relationship, and they tend to by more intuitive and with simpler topology

Three query in the baysian networks:
* joint probability query
* conditianal probability query
* conditioanl independence query

D-seperation algorithm:
* tail-to-tail: 
* head-to-tail:
* head-to-head:

path blocked:



what is a Markov model:
* bayesian network with assumptions:
  * future is always independent from the past, given the present
  * Fisrt-order Markov property: each time step only depends on the previous step
  * value of variable at a given time is called state

What are the primary components of a markov model:
* initial prior
* transitional probability: how dynamics of the system evolves over time

The stationary assumption states

What are Hidden Markov models:
* state a underlying hidden state conditioanlly independent to some ovserved evidence
* Emission cpt is an additional definition to the regular markove model
* Evidence variables are not independent because correlate via the hidden state

Naiive Bayes model for classification:
because the assumption:
* the conditional independence between evidence variables given the class 

Naiive bayes model: 
* a prior 
* the class conditional distribution P(Oi|C)

most important applications in performing inference in temporal model:
* filtering 
* prediction
* smoothing
* most likely explanation


