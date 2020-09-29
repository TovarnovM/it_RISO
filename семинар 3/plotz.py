import numpy as np
import matplotlib.pyplot as plt

def plot_termo(res):

    fig = plt.figure()
    host = fig.add_subplot(111)

    par1 = host.twinx()
    par2 = host.twinx()

    host.set_xlim(0, 20)

    plim = (0,300)
    vlim = (0, 1000)
    xlim = (0, 10)

    host.set_ylim(*plim)
    par1.set_ylim(*vlim)
    par2.set_ylim(*xlim)

    n=11
    host.yaxis.set_ticks(np.linspace(*plim, n))
    par1.yaxis.set_ticks(np.linspace(*vlim, n))
    par2.yaxis.set_ticks(np.linspace(*xlim, n))

    host.set_xlabel("Время, мс")
    host.set_ylabel("$p_m$, МПа")
    par1.set_ylabel("$\\upsilon_p$, м/с")
    par2.set_ylabel("$x_p$, м")

    color1 = 'darkorange'
    color2 = 'darkgreen'
    color3 = 'blue'

    p1, = host.plot(res['t']*1e3, res['p_m']/1e6, color=color1, label='$p_m(t)$')
    p2, = par1.plot(res['t']*1e3, res['v_p'], color=color2, label='$\\upsilon_p(t)$')
    p3, = par2.plot(res['t']*1e3, res['x_p'], color=color3, label='$x_p(t)$')

    lns = [p1]
    lns2 = [p2, p3]
    host.legend(handles=lns, loc='upper left')
    par1.legend(handles=lns2, loc='upper right')
    par2.spines['right'].set_position(('outward', 60))      

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    host.grid()
    plt.show()
    
def plot_lagr(res2):
    
    fig = plt.figure()
    host = fig.add_subplot(111)

    par1 = host.twinx()
    par2 = host.twinx()

    host.set_xlim(0, 20)

    plim = (0,300)
    vlim = (0, 1000)
    xlim = (0, 10)

    host.set_ylim(*plim)
    par1.set_ylim(*vlim)
    par2.set_ylim(*xlim)

    n=11
    host.yaxis.set_ticks(np.linspace(*plim, n))
    par1.yaxis.set_ticks(np.linspace(*vlim, n))
    par2.yaxis.set_ticks(np.linspace(*xlim, n))

    host.set_xlabel("Время, мс")
    host.set_ylabel("$p$, МПа")
    par1.set_ylabel("$\\upsilon_p$, м/с")
    par2.set_ylabel("$x_p$, м")

    color1 = 'darkorange' 
    color2 = 'darkgreen' 
    color3 = 'blue' 

    ps_d = np.array([lr['p'][-1] for lr in res2['layers']])
    ps_b = np.array([lr['p'][0] for lr in res2['layers']])
    v_p = np.array([lr['u'][-1] for lr in res2['layers']])
    x_p = np.array([lr['x'][-1] for lr in res2['layers']])
    ts =  np.array([lr['t'] for lr in res2['layers']])

    p1, = host.plot(ts*1e3, ps_d/1e6, color=color1, label='$p_d(t)$')
    p11, = host.plot(ts*1e3, ps_b/1e6, '--', color=color1, label='$p_b(t)$')
    p2, = par1.plot(ts*1e3, v_p, color=color2, label='$\\upsilon_p(t)$')
    p3, = par2.plot(ts*1e3, x_p, color=color3, label='$x_p(t)$')

    lns = [p1, p11]
    lns2 = [p2, p3]
    host.legend(handles=lns, loc='upper left')
    par1.legend(handles=lns2, loc='upper right')

    par2.spines['right'].set_position(('outward', 60))      

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    host.grid()
    plt.show()