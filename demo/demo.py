import sys
import logging as l
import re
import os

sys.path.append('..')
import qucs.simulate

class DemoSimulationDescription(qucs.simulate.SimulationDescription):
    ''' Simple example of SimulationDescription subclassing,

    it is necessary to reimplement the constructor and the modify netlist method
    the modify_netlist method replaces the amplifier input
    output
    '''

    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.template_netlist_file = os.path.join(os.path.expanduser('~'),'.qucs', 'netlist.txt') # path to netlist.txt

    def modify_netlist(self):
        # simple replacement of any low noise amplifier s2p input file with the number defined in the constructor
        self.netlist = re.sub('lownoiseamplifier[0-9]*\.s2p','lownoiseamplifier%d.s2p' % self.n, self.template_netlist)
        return self.netlist

def demo():

    # creating simulation descriptions
    simulation_descriptions = [DemoSimulationDescription('amp0',0), DemoSimulationDescription('amp1',1)]

    # creating simulation objects using descriptions
    simulations = map(qucs.simulate.Simulation,simulation_descriptions)

    # running simulations
    for sim in simulations:
        sim.run()
        sim.extract_data()
        # writing S21 vs freq
        sim.write_result('acfrequency', 's21db')
    return simulations

# if launched as a script
if __name__ == '__main__':
    l.basicConfig(level=l.DEBUG)
    simulations = demo()
    # qucs simulation outputs are saved in simulations[0].results as dictionary

    #plotting
    import matplotlib.pyplot as plt
    plt.figure()
    for sim in simulations:
        plt.plot(sim.results['acfrequency'], sim.results['s21db'],label=str(sim))
    plt.xlabel('Freq[GHz]'); plt.ylabel('S21[dB]'); plt.grid(); plt.legend(loc=0)
    plt.show()
