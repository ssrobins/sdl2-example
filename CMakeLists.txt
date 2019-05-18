cmake_minimum_required(VERSION 3.14)

project(Rectangles)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

include(cmake/global_settings.cmake)

# Helper functions
include(cmake/add_executable_custom.cmake)
include(cmake/add_sdl2_executable.cmake)
include(cmake/install_executable.cmake)

enable_testing()

add_subdirectory(Rectangles)

include(CPack)
