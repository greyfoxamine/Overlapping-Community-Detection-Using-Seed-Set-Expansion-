#README#

##Info##
This is an efficient C code to compute the similarity between two -possibly overlapping- community structures.  
More generally it evaluates the similarity between two sets of sets.

Given two sets of communities C1 and C2, for each community c1 in C1, the maximum of its similarity to any community in the second set is computed. That is, the program computes $\max_{c2 \in C2}(sim(c1,c2))$. It then computes the average of these maximum similarity scores that is $\frac{1}{|C1|} \sum_{c1 \in C1} \max_{c2\in C2} sim(c1,c2)$.  
It then do reverse, that is compute $\frac{1}{|C2|} \sum_{c2 \in C2} \max_{c1\in C1} sim(c1,c2)$ and then returns the harmonic mean between these two quantities.  
The similarity score used is the f1-score such as described in [1]. See [2] for more details.

##To compile##

gcc f1max.c -o f1max -O3  

##To execute##

type "./f1max coms1.txt coms2.txt"

coms1.txt and coms2.txt contain the list of all communities in each set.  
One community on eanch line:  
i0 i1 i2 ... in  
where:  
i0 i1 i2 ... in is the list of the nodes in the community.

type "./f1max coms2.txt coms1.txt" to do reverse, you can then compute the average or harmonic mean of both values to evaluate how both sets are similar.

Or type "bash test.sh coms1.txt coms2.txt" if you directly want to have all four values.

##References##

[1] J. Yang and J. Leskovec. Overlapping community detection at scale: a nonnegative matrix factorization approach. WSDM2013.  
[2] Danisch M., Guillaume J.-L., Le Grand B. (2015). Déplier la structure communautaire d’un réseau en mesurant la proximité aux représentants de communauté. (in French)

##Initial contributors##

Maximilien Danisch  
Technical consultant: Noe Gaumont and Raphael Tackx  
July 2015  
http://bit.ly/maxdan94  
maximilien.danisch@telecom-paristech.fr
