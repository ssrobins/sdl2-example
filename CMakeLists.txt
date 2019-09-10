cmake_minimum_required(VERSION 3.14)

project(Rectangles VERSION 0.1.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS NO_OUTPUT_DIRS)

include(${CONAN_SSROBINS_ENGINE_ROOT}/cmake/global_settings.cmake)

# Helper functions
include(${CONAN_SSROBINS_ENGINE_ROOT}/cmake/add_executable_custom.cmake)
include(${CONAN_SSROBINS_ENGINE_ROOT}/cmake/add_sdl2_executable.cmake)
include(${CONAN_SSROBINS_ENGINE_ROOT}/cmake/install_executable.cmake)

enable_testing()

add_subdirectory(Rectangles)

set(CPACK_PACKAGE_FILE_NAME ${CMAKE_PROJECT_NAME}_${PROJECT_VERSION}_${platform})
include(CPack)
