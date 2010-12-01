import cPickle
import os.path
import re
import logging as l
import csv
import numpy as np

import extract

class SimulationDescription(object):
    ''' Contains the description of the simulation

    it is necessary to reimplement the constructor and the modify_netlist method
    in order to create dinamically the new netlist from the original created with QUCS GUI
    '''
        
    output = None

    def __init__(self, name):
        self.name = name
        self.template_netlist_file = '/home/zonca/.qucs/netlist.txt'

    def modify_netlist(self, template_netlist):
        new_netlist = template_netlist
        return new_netlist
    
    @property
    def template_netlist(self):
        """Read the default netlist from the QUCS folder"""
        
        f = open(self.template_netlist_file, 'r')
        template_netlist = f.read()
        f.close()
        return template_netlist

    def __repr__(self):
        return 'SimulationDescription:%s' % self.name

class Simulation(object):
    """Main class which contains the status of 1 simulation"""

    def __init__(self, simulation_description):
        """Constructor - inizialize simulation, reads config"""
        self.simulation_description = simulation_description

    def __repr__(self):
        return self.simulation_description.name

    def modify_netlist(self):
        """Prepare the netlist input file for the new simulation

        returns the filename"""

        new_netlist = self.simulation_description.modify_netlist(self.template_netlist)

        # writes the netlist file in the netlists folder
        netlists_folder_name = 'netlists'
        if not os.path.isdir(netlists_folder_name):
            os.mkdir(netlists_folder_name)
        filename = os.path.join(netlists_folder_name,'netlist%d.txt' % self.n)
        f = open(filename, 'w')
        f.write(new_netlist)
        f.close()
        self.netlist = filename

    def run(self):
        """Run simulation"""
        self.netlist = self.simulation_description.modify_netlist()
        l.info("Checking netlist: " + self.netlist)
        import os
        try:
            if os.system('qucsator -c -i ' + self.netlist) != 0:
                raise BadNetlistFormatException(self.netlist)
        except BadNetlistFormatException, x:
            import sys
            l.error('File=' + x.netlist_filename) # defined in the exception
            sys.exit()
        l.info("Running QUCS on: " + self.netlist)
        self.out = self.netlist.replace('netlist','output')
        os.system('qucsator -i %s -o %s' % (self.netlist,self.out))

    def extract_data(self):
        """Extracts data from qucsdata file into results"""
        self.results = qucs.load_data(self.out)

    def write_result(self, output_x, output_y, how='csv'):
        """Write results to file. how = csv or pickle """
        folder_name = how 
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)
        filename = os.path.join(folder_name,'out_%s.%s' % (self.simulation_description.name, how))
        l.info('Writing results to %s' % filename)

        x = getattr(self.results, output_x)
        y = getattr(self.results, output_y)

        try:
            matrix = np.hstack((array(x)[:,newaxis],array(y)[:,newaxis]))
        except ValueError:
            print "Dimension mismatch:"
            print "frequency:", freq[:,newaxis].shape
            print "result:", array(result)[:,newaxis].shape
            print "simulation ",self.simulation_description.name
            raise

        if how == 'csv':
            np.savetxt(filename, matrix, delimiter = ',')
        elif how == 'pickle':
            with open(filename, 'wb') as f:
                cPickle.dump(matrix,f,-1)

class BadNetlistFormatException(Exception):
    """Exception raised by qucsator check routine"""
    def __init__(self, netlist_filename):
        Exception.__init__(self)
        self.netlist_filename = netlist_filename
    def __str__(self):
        return "Bad format in file: " + self.netlist_filename
