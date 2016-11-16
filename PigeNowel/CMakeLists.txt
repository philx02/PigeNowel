SET(this_target PigeNowel)


INCLUDE_DIRECTORIES(
  ${Boost_INCLUDE_DIRS}
)

SET(${this_target}_HEADER_FILES
  SendEmail.h
)

SET( ${this_target}_SOURCE_FILES
  main.cpp
) 
 
LIST(APPEND ${this_target}_SOURCE_FILES ${${this_target}_HEADER_FILES})

add_executable(${this_target} ${${this_target}_SOURCE_FILES})
target_link_libraries(${this_target} ${Boost_LIBRARIES})
IF(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
target_link_libraries(${this_target} pthread)
target_link_libraries(${this_target} dl)
ENDIF()
