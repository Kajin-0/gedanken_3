import math, numpy as np
H=np.array([-.0032548,0.,-.0056579])
C=np.array([0.,-.0082515,-.00433275])
W=np.linalg.inv(np.eye(3)+np.ones((3,3)))
def coef(a,b):
 q=(b@W@a)/(b@W@b); r=a-q*b
 return math.sqrt(r@W@r)/abs(a[2])
h=coef(H,C); c=coef(C,H)
print('coeff_HgTe',h,'coeff_CdTe',c)
print('condition',np.linalg.cond(np.column_stack((H,C))))
for d in (.01,.02,.05,.10):
 for s in (.01,.02,.05,.10):
  print(d,s,math.ceil((5*s/(h*d))**2),math.ceil((5*s/(c*d))**2))
kT=.08617333262*77
budget=h*.05/5
print('kT_meV',kT,'Eg_full_budget_meV',budget*kT,'Eg_half_budget_meV',.5*budget*kT)
