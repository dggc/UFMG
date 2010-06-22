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


class WeightedVertex(Vertex):
    """ Represents a weighted vertex

        \ingroup BaseElements
    """
    def __init__(self,vertexNumber,vertexWeight):
        """ Constructs a weighted vertex given a vertex number and vertex weight

            @param vertexNumber vertex number to be assigned to the created vertex
            @param vertexWeight vertex weight to be assigned to the created vertex
        """
        Vertex.__init__(self,vertexNumber)

        ## Vertex weight 
        self.vertexWeight = vertexWeight

    def getWeight(self):
        """ Get vertex weight

            @return vertexWeight Vertex weight of this vertex
        """
        return self.vertexWeight
    
    def setWeight(self,vertexWeight):
        """ Set vertex weight

            @param vertexWeight New vertex weight
        """
        self.vertexWeight = vertexWeight
