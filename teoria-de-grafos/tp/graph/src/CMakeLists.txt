include_directories(
    ${GRAPH_INC}
    )

file(GLOB GRAPH_SRC *.cpp)

add_library( ${GRAPH_LIB}
    ${GRAPH_SRC}
    )
