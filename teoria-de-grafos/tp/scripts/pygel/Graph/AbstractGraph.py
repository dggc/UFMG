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

from pygel.MetaClass.AbstractMethod import *
from pygel.MetaClass.MetaClass import *

class AbstractGraph:
    """ Abstract class for representing a graph

        \ingroup Graph
    """
    __metaclass__ = MetaClass

    ## Abstract method for adding an edge
    addEdge = AbstractMethod('addEdge')

    ## Abstract method for deleting an edge
    deleteEdge = AbstractMethod('deleteEdge')

    ## Abstract method for adding a vertex
    addVertex = AbstractMethod('addVertex')

    ## Abstract method for deleting a vertex
    deleteVertex = AbstractMethod('deleteVertex')

    ## Abstract method for obtaining all edges
    getEdges = AbstractMethod('getEdges')

    ## Abstract method for obtaining all vertices
    getVertices = AbstractMethod('getVertices')
