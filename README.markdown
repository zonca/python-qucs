Python package for automating QUCS simulations
==============================================

_License GPL_

Example usage of this package in my article:
[Modeling the frequency response of microwave radiometers with QUCS](http://arxiv.org/abs/1011.6363)

Introduction
------------

It was designed to easily iterate between testing a circuit on the QUCS GUI and running batch simulations,
so that a system can be debugged interactively at several development stages. 

The _simulate_ module parses the netlist produced interactively by the QUCS GUI and runs user defined regular expressions to create and save to disk the target set of netlists, then runs qucsator on each of them. The _extract_ and _plot_ modules allow then to read the custom QUCS file format, manipulate and plot the results.

Usage
-----

The easiest way is to run the demo:

1. copy pythonqucstest_prj in your .qucs folder
2. open QUCS GUI and run the pythonqucstest schematic in order to create the netlist
3. check that QUCS created the netlist text file, usually in .qucs/netlist.txt
4. run python demo.py in the demo folder
5. simulations for 2 netlists with 2 different amplifiers are automatically run, results are plotted and written as csv files under the csv folder
6. netlists and raw output files are written in the subfolders netlists and outputs

Citing
------

If you use python-qucs for research, please cite my work in your publication:
[http://arxiv.org/abs/1011.6363](http://arxiv.org/abs/1011.6363)

* [python-qucs homepage](http://andreazonca.com/software/python-qucs)
* [python-qucs on on Github](https://github.com/zonca/python-qucs)
* [QUCS](http://qucs.sf.net)
