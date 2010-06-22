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
# $LastChangedDate: 2007-07-31 17:42:11 +0200 (Tue, 31 Jul 2007) $
# $LastChangedRevision: 56 $
#
#

import random

from pygel.BaseElements.Vertex import *
from pygel.BaseElements.Edge import *
from pygel.Graph.NumberedEdgeDirectedGraph import *
from pygel.Exceptions.Exceptions import *
from ChooseEdges import *

class DirectedPowerLawRandomGraph(NumberedEdgeDirectedGraph):

    """ Generates a synthetic Web graph or Power Law graph using an RMAT algorithm
        \ingroup RandomGraphs
    """

    def __init__(self, size, noOfEdges):
        """ Constructs an empty graph

            @param size Number of vertices to be considered for generation
            @param noOfEdges Number of edges to generate
        """
        NumberedEdgeDirectedGraph.__init__(self)

        ## Number of vertices to be considered for generation
        self.graphSize = size

        
        ## Number of edges to generate
        self.noOfEdges = noOfEdges

        ## Parameters of the RMAT algorithm. Decide the probability with which quadrants in an adjacency matrix are chosen
        ## \todo Add description about choosing these probabilities


        ## Probability of choosing quadrant A
        self.probA = 0.45

        ## Probability of choosing quadrant B
        self.probB = 0.15

        ## Probability of choosing quadrant C
        self.probC = 0.15

        ## Probability of choosing quadrant D
        self.probD = 0.25

        ## Temporary storage of edges. Maintained for achieving performance
        self.serialEdgeList = []

        ## Debug flag
        self.debug = 0
        
        self.startVertX = 1
        self.endVertX = size

        self.startVertY = 1
        self.endVertY = size

    def setProbs(self, probA, probB, probC, probD):
        """ Sets the probability with which quadrants in an adjacency matrix are chosen

            @param probA Probability of choosing quadrant A
            @param probB Probability of choosing quadrant B
            @param probC Probability of choosing quadrant C
            @param probD Probability of choosing quadrant D
            @throws PackageExceptions::DistError
        """
        if probA + probB + probC + probD != 1:
            raise DistError(ErrorMessages.distAddOne)
        
        self.probA = probA
        self.probB = probB
        self.probC = probC
        self.probD = probD
        return

    def generate(self, noOfThreads, noSelfLoops):
        """ Generates a the graph. Heart of web graph generation algorithm. Each thread gets an equal number of nodes to generate.

            @param noOfThreads Number of threads to spawn for the graph generation. More threads does not correspond to fast generation  
            @param noSelfLoops If true (set to 1) self loops are discarded in the resulting graph.   
        """
        chooserThreads = []
        for i in range(noOfThreads):
            chooser = ChooseEdges(self.noOfEdges/noOfThreads, noSelfLoops,
                                  self.startVertX, self.endVertX, self.startVertY, self.endVertY,
                                  self.probA, self.probB, self.probC, self.probD)
            
            chooserThreads.append(chooser)
            chooser.start()

        for t in chooserThreads:
            t.join()
        
        self.serialEdgeList = ChooseEdges.serialEdgeList

        del chooserThreads
        del ChooseEdges.serialEdgeList
        return

    def populate(self):
        """ Populate graph with edges generated after a call to DirectedPowerLawRandomGraph::generate. You should call this method before you can use any of the non-overridden method in Graph::NumberedEdgeDirectedGraph
        
        """
        serialEdgeList = self.serialEdgeList

        for i in xrange(0,len(serialEdgeList)-1,2):
            newEdge = Edge(Vertex(serialEdgeList[i]), Vertex(serialEdgeList[i+1]))
            self.addEdge(newEdge)

        
    def writeEdges(self, fileName, format):
        """ Write edges to file

            @param fileName File name to store edges
            @param format Format of output file. Can take values: <br>
                          'simple' = simple format <br>
                          'dot' = format compatible with 'dot' command
                          'csv' = comma separated value format
                          
        """
        serialEdgeList = self.serialEdgeList

        if format == 'simple':
            f = open(fileName,'w')
            for i in xrange(0,len(serialEdgeList)-1,2):
                f.write("%s -> %s\n" % (serialEdgeList[i], serialEdgeList[i+1]))
            f.close()
            
        elif format == 'dot':
            f = open(fileName,'w')
            f.write("digraph G { \n")
            for i in xrange(0,len(serialEdgeList)-1,2):
                f.write("%s -> %s\n" % (serialEdgeList[i], serialEdgeList[i+1]))
            f.write("} \n")
            f.close()

        if format == 'csv':
            f = open(fileName,'w')
            for i in xrange(0,len(serialEdgeList)-1,2):
                f.write("%s,%s\n" % (serialEdgeList[i], serialEdgeList[i+1]))
            f.close()


