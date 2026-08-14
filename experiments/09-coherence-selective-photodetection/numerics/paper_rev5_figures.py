from pathlib import Path
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['pdf.fonttype'] = 42

OUT=Path('.')

def rates(N,kappa,gamma):
    a=kappa+gamma
    delta=math.sqrt(a*a-4*kappa*gamma/N)
    return (a-delta)/2,(a+delta)/2,delta

def collection(t,N,kappa,gamma,b0):
    rm,rp,delta=rates(N,kappa,gamma)
    A=(rp-kappa*b0)/delta
    B=(kappa*b0-rm)/delta
    return 1-A*math.exp(-rm*t)-B*math.exp(-rp*t)

def gate(N,kappa,gamma,eta):
    f=lambda t: collection(t,N,kappa,gamma,1)-eta
    hi=max(1/(kappa+gamma),1e-15)
    while f(hi)<0: hi*=2
    return brentq(f,0,hi,xtol=1e-12,rtol=1e-11)

def chi_exact(N,k0,g0,alpha,beta,eta):
    k=k0*N**alpha; g=g0*N**beta
    T=gate(N,k,g,eta)
    integ=quad(lambda u:max(collection(u,N,k,g,1/N),0),0,T,epsabs=1e-11,epsrel=1e-9,limit=200)[0]
    return T,N*integ

def save(fig,name):
    fig.savefig(OUT/(name+'.pdf'),bbox_inches='tight')
    fig.savefig(OUT/(name+'.png'),dpi=260,bbox_inches='tight')
    plt.close(fig)

# Fig. 1
fig,ax=plt.subplots(figsize=(8.8,4.9))
ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis('off')
bright_xy=(3.15,3.72); dark_xy=(3.15,1.40); sink_xy=(7.45,3.72)
for xy,w,h in [(bright_xy,2.55,1.02),(dark_xy,2.55,1.02),(sink_xy,1.55,1.02)]:
    ax.add_patch(plt.Rectangle(xy,w,h,fill=False,linewidth=1.55,color='black'))
ax.text(4.425,4.23,'bright counted sector',ha='center',va='center',fontsize=11.0)
ax.text(4.425,1.98,'dark manifold',ha='center',va='center',fontsize=11.0)
ax.text(4.425,1.68,r'$N-1$ orthogonal directions',ha='center',va='center',fontsize=9.2)
ax.text(8.225,4.23,'counted sink',ha='center',va='center',fontsize=11.0)
ax.text(0.25,5.18,r'signal photon prepares $|B\rangle=N^{-1/2}\sum_j|j\rangle$',fontsize=10.8)
ax.annotate('',xy=(3.15,4.23),xytext=(2.42,4.82),arrowprops=dict(arrowstyle='->',lw=1.45,color='black'))
ax.annotate('',xy=(7.45,4.23),xytext=(5.70,4.23),arrowprops=dict(arrowstyle='->',lw=1.75,color='black'))
ax.text(6.58,4.50,r'counted extraction $\kappa_N$',fontsize=10.2,ha='center')
ax.text(0.25,0.62,r'local internal event: one $|j\rangle$',fontsize=10.8)
branch=(2.38,1.02)
ax.plot([branch[0]],[branch[1]],marker='o',markersize=2.8,color='black')
ax.annotate('',xy=(3.15,1.92),xytext=branch,arrowprops=dict(arrowstyle='->',lw=1.45,color='black'))
ax.text(1.40,1.55,r'dark-subspace weight $1-1/N$',fontsize=9.1,ha='center')
ax.annotate('',xy=(3.15,3.88),xytext=branch,arrowprops=dict(arrowstyle='->',lw=1.15,linestyle='--',color='black',connectionstyle='arc3,rad=-0.18'))
ax.text(1.56,2.82,r'direct bright weight $1/N$',fontsize=9.1,ha='center')
ax.annotate('',xy=(3.88,2.42),xytext=(3.88,3.72),arrowprops=dict(arrowstyle='->',lw=1.55,color='black'))
ax.text(3.62,3.10,r'local dephasing $\gamma_N$',fontsize=9.8,ha='right',va='center')
ax.annotate('',xy=(5.00,3.72),xytext=(5.00,2.42),arrowprops=dict(arrowstyle='->',lw=1.25,linestyle='--',color='black'))
ax.text(5.18,3.10,r'effective slow eigenmode $r_{-,N}$',fontsize=9.7,ha='left',va='center')
ax.plot([0.55,9.45],[0.22,0.22],lw=0.75,color='black')
ax.text(5.0,-0.02,r'decision gate: $T_N(\eta)=\inf\{t:C_{S,N}(t)\geq\eta\}$   |   dilute response: $\chi_N=N\int_0^{T_N} C_{\rm loc,N}(u)\,du$',ha='center',va='center',fontsize=9.35)
save(fig,'paper_rev5_fig1_mechanism')

# Fig. 2
k0=10.; g0=1.; Ns=np.unique(np.round(np.logspace(1,4,24)).astype(int))
cases=[
    (r'extraction wins: $\alpha=1,\,\beta=0,\,\eta=.90$',1,0,.90,-1),
    (r'balanced fast: $\alpha=\beta=0,\,\eta=.50$',0,0,.50,0),
    (r'balanced slow: $\alpha=\beta=0,\,\eta=.95$',0,0,.95,2),
    (r'balanced collective slow: $\alpha=\beta=1,\,\eta=.95$',1,1,.95,1),
]
fig,ax=plt.subplots(figsize=(7.5,5.25)); markers=['o','s','^','D']
for m,(lab,a,b,e,sl) in zip(markers,cases):
    vals=[]
    for N in Ns:
        _,ch=chi_exact(int(N),k0,g0,a,b,e); vals.append(ch)
    vals=np.array(vals)
    ax.loglog(Ns,vals,marker=m,ms=4,lw=1.4,label=lab)
    Ng=np.array([Ns[-5],Ns[-1]],float); guide=vals[-1]*(Ng/Ns[-1])**sl
    ax.loglog(Ng,guide,'--',lw=1.0)
    ax.text(Ng[0],guide[0]*1.13,rf'slope ${sl:g}$',fontsize=8.8)
ax.set_xlabel(r'coherently participating states $N$')
ax.set_ylabel(r'dilute internal-event susceptibility $\chi_N(\eta)$')
ax.grid(True,which='both',alpha=.2); ax.legend(frameon=False,fontsize=8.6)
save(fig,'paper_rev5_fig2_scaling')

# Fig. 3
q0=k0/(k0+g0)
fig,ax=plt.subplots(figsize=(7.2,4.75)); ax.set_xlim(-1,1); ax.set_ylim(0,1)
ax.axvline(0,lw=1.4,color='black'); ax.plot([0],[q0],'o',ms=6,color='black')
ax.text(-.5,.70,'dephasing scales faster',ha='center',fontsize=11.5)
ax.text(-.5,.55,r'$\eta_{\rm sc}=0$',ha='center',fontsize=13)
ax.text(-.5,.39,'no fixed positive efficiency\nhas bounded dilute response',ha='center',fontsize=9.8)
ax.text(.5,.70,'extraction scales faster',ha='center',fontsize=11.5)
ax.text(.5,.55,r'$\eta_{\rm sc}=1$',ha='center',fontsize=13)
ax.text(.5,.39,r'every fixed $\eta<1$ can'+'\nhave bounded dilute response',ha='center',fontsize=9.8)
ax.text(0,.965,r'balanced: $\eta_{\rm sc}=q_0=\kappa_0/(\kappa_0+\gamma_0)$',ha='center',va='top',fontsize=10.3)
ax.annotate('',xy=(0,q0+.006),xytext=(0,.91),arrowprops=dict(arrowstyle='->',lw=1.0))
ax.set_xlabel(r'rate-scaling sector $\alpha-\beta$')
ax.set_ylabel(r'bounded-response efficiency supremum $\eta_{\rm sc}$')
ax.set_xticks([-1,0,1],[r'$\alpha<\beta$',r'$\alpha=\beta$',r'$\alpha>\beta$'])
ax.grid(True,axis='y',alpha=.2)
save(fig,'paper_rev5_fig3_ceiling')
