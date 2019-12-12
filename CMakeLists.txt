cmake_minimum_required(VERSION 3.16)

project(Rectangles VERSION 0.1.11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

include(${CONAN_CMAKE_UTILS_ROOT}/global_settings.cmake)

# Helper functions
include(${CONAN_CMAKE_UTILS_ROOT}/add_executable_custom.cmake)
include(${CONAN_CMAKE_UTILS_ROOT}/add_sdl2_executable.cmake)
include(${CONAN_CMAKE_UTILS_ROOT}/install_executable.cmake)
include(${CONAN_CMAKE_UTILS_ROOT}/target_assets.cmake)

enable_testing()

add_subdirectory(Rectangles)

set(CPACK_PACKAGE_FILE_NAME ${CMAKE_PROJECT_NAME}_${PROJECT_VERSION}_${platform})
include(CPack)
