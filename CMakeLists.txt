cmake_minimum_required(VERSION 3.11.0)

project(Games)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(company dnqpy)

set(version_major 0)
set(version_minor 1)
set(version_patch 0)
if(ANDROID)
    set(version_code 1)
    set(android_min_sdk_version 15)
endif()


set(cmake_file_url https://gitlab.com/ssrobins/cmake-utils/raw/master/global_settings.cmake)
set(cmake_file_path ${CMAKE_BINARY_DIR}/global_settings.cmake)
message(STATUS "Downloading ${cmake_file_url} to ${cmake_file_path}...")
file(DOWNLOAD
    ${cmake_file_url}
    ${cmake_file_path}
    STATUS download_status
)
list(GET download_status 0 download_error_code)
list(GET download_status 1 download_error_msg)
if(NOT ${download_error_code} EQUAL 0)
    message(FATAL_ERROR "Download failed, error code ${download_error_code}: ${download_error_msg}")
endif()
include(${CMAKE_BINARY_DIR}/global_settings.cmake)

if(IOS)
    set(xcode_code_sign_identity "iPhone Developer")
elseif(APPLE)
    set(xcode_code_sign_identity "Developer ID Application")
endif()

if(APPLE)
    set(xcode_dev_team MLPC343Q5F)
    set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.${company}.\${PRODUCT_NAME:identifier}")
endif()

set(CMAKE_INSTALL_PREFIX ${PROJECT_BINARY_DIR}/_install)
set(CPACK_PACKAGE_DIRECTORY ${PROJECT_BINARY_DIR}/_package)

# Allow organizing source files into subdirectories
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
define_property(
    TARGET
    PROPERTY FOLDER
    INHERITED
    BRIEF_DOCS "Set the folder name."
    FULL_DOCS  "Use to organize targets in an IDE."
)

enable_testing()

#add_subdirectory(3rdparty)

# Additional flags to be used everywhere except
# third-party libs
if(MSVC)
    add_compile_options(
        $<$<CONFIG:Release>:/GL> # Whole program optimization
        /sdl # Enable additional security checks
        /WX # Warning as error
    )
else()
    add_compile_options(
        -Werror # Warning as error
    )
endif()

if(CMAKE_SIZEOF_VOID_P EQUAL 8)
    set(bitness 64)
else()
    set(bitness 32)
endif()

if(WIN32)
    set(CPACK_GENERATOR ZIP)
    set(platform Windows)
elseif(APPLE)
    set(CPACK_GENERATOR ZIP)
    set(platform Mac)
else()
    set(CPACK_GENERATOR TGZ)
    set(platform Linux${bitness})
endif()

add_subdirectory(Rectangles)

# Settings for the installation package
set(CPACK_ARCHIVE_COMPONENT_INSTALL ON)
set(CPACK_COMPONENTS_GROUPING IGNORE)
set(CPACK_PACKAGE_VERSION_MAJOR ${version_major})
set(CPACK_PACKAGE_VERSION_MINOR ${version_minor})
set(CPACK_PACKAGE_VERSION_PATCH ${version_patch})
set(CPACK_INCLUDE_TOPLEVEL_DIRECTORY 0)
set(CPACK_PACKAGE_FILE_NAME ${CMAKE_PROJECT_NAME})

include(CPack)
