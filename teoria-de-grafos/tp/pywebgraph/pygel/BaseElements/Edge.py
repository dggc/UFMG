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


from AbstractEdge import *

class Edge(AbstractEdge):
    """ Represents graph edge

        \ingroup BaseElements
    """
    
    def __init__(self):
        """ Constructs an emtpy edge
        """
        ## Starting vertex of a edge of type BaseElements::Vertex
        self.startVertex = ''        

        ## Ending vertex of a edge of type BaseElements::Vertex
        self.endVertex = ''

    def __init__(self, startVertex, endVertex):
        """ Constructs a graph edge with given start and end vertices

            @param startVertex start vertex of the edge
            @param endVertex end vertex of the edge
        """
        self.startVertex = startVertex
        self.endVertex = endVertex
       
    def getStartVertex(self):
        """ Get the start vertex

            @return startVertex Start vertex of type BaseElements::Vertex
        """
        return self.startVertex
    
    def getEndVertex(self):
        """ Get the end vertex

            @return endVertex End vertex of type BaseElements::Vertex
        """
        return self.endVertex
    
    def setStartVertex(self, vertex):
        """ Set the start vertex

            @param startVertex Start vertex of type BaseElements::Vertex
        """
        self.startVertex = vertex
        
    def setEndVertex(self, vertex):
        """ Set the end vertex
                
            @param endVertex End vertex of type BaseElements::Vertex
        """
        self.endVertex = vertex
