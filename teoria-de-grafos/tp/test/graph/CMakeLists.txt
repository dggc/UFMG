include(${TPA_SOURCE_DIR}/globalVariables.cmake)
include_directories(
    ${GRAPH_INC}
    )

add_executable(graphTest GraphTest)
target_link_libraries(graphTest ${GRAPH_LIB} ${TEST_Boost_LIBS})
set_target_properties(graphTest PROPERTIES COMPILE_FLAGS -DBOOST_TEST_DYN_LINK)
add_test(graphTest ${EXECUTABLE_OUTPUT_PATH}/graphTest)

