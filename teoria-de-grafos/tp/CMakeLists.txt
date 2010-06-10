cmake_minimum_required (VERSION 2.6)
project (TPA)

include(${TPA_SOURCE_DIR}/globalVariables.cmake)

enable_testing()

add_subdirectory (graph)
add_subdirectory (main)
add_subdirectory (test)
