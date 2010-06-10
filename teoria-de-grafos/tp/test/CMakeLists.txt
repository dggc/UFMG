include(${TPA_SOURCE_DIR}/globalVariables.cmake)

set (Boost_FIND_REQUIRED TRUE)
set (Boost_FIND_QUIETLY TRUE)
set (Boost_USE_MULTITHREADED TRUE)
set (Boost_USE_STATIC_LIBS FALSE)
set (BOOST_COMPONENTS program_options unit_test_framework prg_exec_monitor )
find_package(Boost COMPONENTS ${BOOST_COMPONENTS} )
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${Boost_LIBRARY_DIRS})
set (TEST_Boost_LIBS ${Boost_PROGRAM_OPTIONS_LIBRARY} 
${Boost_PRG_EXEC_MONITOR_LIBRARY} ${Boost_UNIT_TEST_FRAMEWORK_LIBRARY} )

add_subdirectory(graph)

