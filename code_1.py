import numpy as np
from scipy.stats import bernoulli

set_size=100000

th_pr_A=4/5
th_pr_B=1/2
th_pr_BgivenA=2/5

#simulations by bernoulli r.v.
A_set= bernoulli.rvs(size= sample_size, p = th_pr_A)
B_set= bernoulli.rvs(size= sample_size, p = th_pr_B)
BgivenA_set= bernoulli.rvs(size= sample_size, p = th_pr_BgivenA)

A_ds = np.nonzero(A_set == 1)
B_ds = np.nonzero(B_set == 1)
BgivenA_ds = np.nonzero(BgivenA_set == 1)

num_A= np.size(A_ds)
num_B= np.size(B_ds)
num_BgivenA= np.size(BgivenA_ds)

sim_pr_A=num_A/set_size
sim_pr_B=num_B/set_size
sim_pr_BgivenA=num_BgivenA/set_size

#calculating P(A intersection B):
sim_pr_AB= sim_pr_BgivenA*sim_pr_A
th_pr_AB = th_pr_BgivenA*th_pr_A

#calculating P(AgivenB)
sim_pr_AgivenB= sim_pr_AB/sim_pr_B
th_pr_AgivenB = th_pr_AB/th_pr_B


#calculating P(A union B)
sim_pr_AorB= sim_pr_A + sim_pr_B - sim_pr_AB
th_pr_AorB = th_pr_A+th_pr_B-th_pr_AB

print("P(AB) Calculated Value  = ", sim_pr_AB, " while theoretical value = ", th_pr_AB)
print("P(A/B) Calculated Value  = ", sim_pr_AgivenB, " while theoretical value = ", th_pr_AgivenB)
print("P(A+B)  Calculated Value = ", sim_pr_AorB, " while theoretical value = ", th_pr_AorB)