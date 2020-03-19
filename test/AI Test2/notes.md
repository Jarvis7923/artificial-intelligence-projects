AI Test2 
-------

### Content
Propositional Logic
First Order Logic
#### What is logic

logic can: 
* representing the state of world
* representing rules of operations

by using logic we can:
* make rational desicions
* do inference

#### What is a good representation language
* formal and also can express partial informatiopn
* accommodate inference
  
#### What are the fundamental elements of a formal logic

* Syntax: a set of symbols and ruls used to express knowledge
* Semantics: how the symbols and sentences related to the world
* Inference procedure: describes how to derive new sentences for exsiting sentences

#### What is the semantics for a sentence

its interpretation in the world

#### What is knowledge base

a list of sentence assumed to be true in the world

#### what is a model for a KB or a sentence

the assignment to all the symbols s.t. all the sentences are true

#### What does it mean if p is satisfiable

there exists a model for the sentence

#### what is tautology and contradiction

neither of them provides new information

* tautology: returns true for all the assignments of all the symbel
* contradiction: returns false for all the assignments of all the symbel


#### what is the truth table of p -> q

using Venn diagram:

other compination are T
p: T, q: F --- p -> q: F


#### What is De Morgan's Law

!(p and q) = !p or !q
!(p or q) = !p and !q

#### Contrapositive equivalance

p -> q = !q -> !p

#### What does it mean by KB P entails Q

all models of P are model of Q

P = True -> Q = True

#### how to prove the entailment

Proof by refutaion:

requires:
* KB is in CNF( and of ors)

conjoining the KB with the NEGATION of the query sentence S, called A.

if A has no model , then KB entails S.


#### What is logical inference:

create new sentences that follows the KB

#### what is modus ponens

if p is T, then p -> q makes q is T 

#### what is modus tollens

if !p is T, then p -> q makes !q is T 


#### Logical inference

Forward Chaining:
answer queries using a KB to generate new facts until we find our query is true or we've run out of new facts to generates. 

Backward Chaining:
find the query in the consequnce of rules and unti`l all the facts are known.

#### What algorithm can be used in efficiently cheching satisfiability

DPLL
complete
Depth first for backtracking
requires:
KB in CNF form
improvements
* early possible termination
* pure symbol heuristic
* unit clause heuristic
  

#### Why the Propositional logic are limited
* Hard to identify individuals
* can not directly talk properties and relationships
* pattens and generalizations are not 

#### What else is in the First-Order Logic

* objects: individul
* Properties: distinguish them form other objects
* Relationships: between sets of objects
* Function: subset of relations

* Quantifier: exsistential, universial
* Equality: 

