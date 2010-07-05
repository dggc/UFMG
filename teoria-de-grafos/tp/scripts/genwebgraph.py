#!/usr/bin/python
#
# Copyright (C) 2007 Saket Sathe
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
# $LastChangedBy: xaeroman $
# $LastChangedDate: 2008-03-24 23:14:05 +0100 (Mon, 24 Mar 2008) $
# $LastChangedRevision: 88 $
# 
#

import getopt, sys
from pygel.RandomGraphs.DirectedPowerLawRandomGraph import *
from pygel.RandomGraphs.UndirectedPowerLawRandomGraph import *

def usage(paramDefaults):
    helpString = """
USAGE: ./genwebgraph.py [options]

        Command line tool for:
            1) Generating an undirected/directed synthetic web graph.

            2) Finding its strongly connected components.

DESCRIPTION

       -t, --threads=NUMBER
               Number of threads to use for the generation. Default: %s

       -o, --output=FILENAME
               File for storing output. Default: %s

       -f, --format=FMT
               Output format. Default: %s. Possible: 'simple' or 'dot' or 'csv'

       -v, --max-vertices=NUMBER
               Maximum number of vertices. Default: %s

       -e, --max-edges=NUMBER
               Maximum number of edges. Default: %s

       -u, --type=[[directed][undirected]]
               Type of the generated graph. Default: %s

       -m, --find-conncomps
               Toggle connected components computation. 

       -c, --file-conncomps=FILENAME
               Write connected components to file. Should be used with --find-conncomps. Default: %s

       -l, --only-largest
               Only find the largest component. Should be used with --find-conncomps. Default: %s

       -s, --no-self-loops
               Disallow self-loops (vertex pointing to itself). 

       -h, --help
               Show this page
        """ % (paramDefaults['threads'], paramDefaults['output'], paramDefaults['format'], paramDefaults['max-vertices'], paramDefaults['max-edges'], paramDefaults['type'], paramDefaults['file-conncomps'], paramDefaults['only-largest'])

    print helpString
    return


if __name__=="__main__":
    paramDefaults = { 'threads' : '1' , 'output' : '/tmp/graph.pyg', 'format': 'simple', 'max-vertices':'100', 'max-edges':'100', 'type':'directed', 'find-conncomps':0 ,'file-conncomps':'/tmp/graph.cc', 'only-largest':0, 'no-self-loops':0}

    
    if len(sys.argv) == 1:
        usage(paramDefaults)
        sys.exit(0)
        
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:o:f:v:e:u:mc:lsh", ["threads=","output=","format=", "max-vertices=","max-edges=", "type=", "find-conncomps", "file-conncomps=", "only-largest","no-self-loops","help"])
    except getopt.GetoptError:
        usage(paramDefaults)
        sys.exit(2)
                      
    config = {}

    for param in paramDefaults:
        config[param] = paramDefaults[param]

    for o, a in opts:
        options = ("-t","--threads")
        if o in options:
           config[options[1][2:]] = a

        options = ("-o","--output")
        if o in options:
           config[options[1][2:]] = a

        options = ("-f","--format")
        if o in options:
           config[options[1][2:]] = a

        options = ("-v","--max-vertices")
        if o in options:
           config[options[1][2:]] = a

        options = ("-e","--max-edges")
        if o in options:
           config[options[1][2:]] = a

        options = ("-u","--type")
        if o in options:
           config[options[1][2:]] = a

        options = ("-m","--find-conncomps")
        if o in options:
           config[options[1][2:]] = 1

        options = ("-c","--file-conncomps")
        if o in options:
           config[options[1][2:]] = a

        options = ("-l","--only-largest")
        if o in options:
           config[options[1][2:]] = 1

        options = ("-s","--no-self-loops")
        if o in options:
           config[options[1][2:]] = 1
           
        options = ("-h","--help")
        if o in options:
            usage(paramDefaults)
            sys.exit(0)


    type = str(config['type'])

    graph = None
    if type == 'directed':
        graph = DirectedPowerLawRandomGraph(int(config['max-vertices']),int(config['max-edges']))
    if type == 'undirected':
        graph = UndirectedPowerLawRandomGraph(int(config['max-vertices']),int(config['max-edges']))

    print "Spawning %s thread(s)..." % (config['threads'])
    noSelfLoops = int(config['no-self-loops'])
    if noSelfLoops == 1: 
        print "Self-loops are not allowed..."
    else:
        print "Self-loops are allowed..."
    graph.generate(int(config['threads']),noSelfLoops)
    graph.populate()
    graph.writeEdges(str(config['output']),str(config['format']))
    print "Output written to file %s" % (str(config['output']))

    findConnComps = config['find-conncomps']
    if findConnComps == 1:
        getLargest = config['only-largest']
        fileName = config['file-conncomps']
        
        allSCC = graph.getSCComponents(getLargest)
        graph.writeCC(fileName, allSCC)
        
        if getLargest == 0:
            print "Connected components written to %s" % (fileName)
        else:
            print "Largest connected component written to %s" % (fileName)
