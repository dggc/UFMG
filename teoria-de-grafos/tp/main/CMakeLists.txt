include_directories (
    ${GRAPH_INC}
    )
add_executable(${GRAPH_EXE}
    NewGraphMain
    )

target_link_libraries(${GRAPH_EXE} 
    ${GRAPH_LIB}
    )


include_directories (
    ${GRAPH_INC}
    )
add_executable(${RANDOMGRAPH_EXE}
    RandomGraphMain
    )

target_link_libraries(${GRAPH_EXE} 
    ${GRAPH_LIB}
    )

