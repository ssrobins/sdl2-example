cmake_minimum_required(VERSION 3.11.0)

project(Games)

set(company dnqpy)

set(version_major 0)
set(version_minor 1)
set(version_patch 0)
if(ANDROID)
    set(version_code 1)
    set(android_min_sdk_version 15)
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(IOS)
    set(xcode_code_sign_identity "iPhone Developer")
elseif(APPLE)
    set(xcode_code_sign_identity "Developer ID Application")
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.9" CACHE STRING "Minimum OS X deployment version" FORCE)
endif()

if(APPLE)
    set(xcode_dev_team MLPC343Q5F)
    set(MACOSX_BUNDLE_GUI_IDENTIFIER "com.${company}.\${PRODUCT_NAME:identifier}")
endif()

if(MSVC)
    add_compile_options(
        $<$<CONFIG:Release>:/Gy> # Enable function-level linking
        /MP # Multi-processor compilation
        $<$<CONFIG:>:/MT> #---------|
        $<$<CONFIG:Debug>:/MTd> #---|-- Statically link the runtime libraries
        $<$<CONFIG:Release>:/MT> #--|
        $<$<CONFIG:Release>:/Oi> # Generate intrinsic functions
        /permissive- # Standard C++ conformance
        $<$<CONFIG:Debug>:/ZI> # Produces a program database (PDB) that supports edit and continue
        $<$<CONFIG:Release>:/Zi> # Produces a program database (PDB)
    )
    
    set(linker_flags_debug
        /SAFESEH:NO # Don't produce an image with a table of safe exceptions handlers
    )
    foreach(flag ${linker_flags_debug})
        set(CMAKE_EXE_LINKER_FLAGS_DEBUG "${CMAKE_EXE_LINKER_FLAGS_DEBUG} ${flag}")
        set(CMAKE_MODULE_LINKER_FLAGS_DEBUG "${CMAKE_MODULE_LINKER_FLAGS_DEBUG} ${flag}")
        set(CMAKE_SHARED_LINKER_FLAGS_DEBUG "${CMAKE_SHARED_LINKER_FLAGS_DEBUG} ${flag}")
    endforeach()
    
    set(linker_flags_release
        /DEBUG # Generate debug information
        /LTCG:incremental # Link-time code generation
        /OPT:ICF # Perform identical COMDAT folding
        /OPT:REF # Eliminates functions and/or data that are never referenced
    )
    foreach(flag ${linker_flags_release})
        set(CMAKE_EXE_LINKER_FLAGS_RELEASE "${CMAKE_EXE_LINKER_FLAGS_RELEASE} ${flag}")
        set(CMAKE_MODULE_LINKER_FLAGS_RELEASE "${CMAKE_MODULE_LINKER_FLAGS_RELEASE} ${flag}")
        set(CMAKE_SHARED_LINKER_FLAGS_RELEASE "${CMAKE_SHARED_LINKER_FLAGS_RELEASE} ${flag}")
    endforeach()
elseif("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU")
    set(linker_flags_gcc
        -static-libgcc
        -static-libstdc++
    )
    foreach(flag ${linker_flags_gcc})
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${flag}")
        set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} ${flag}")
        set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${flag}")
    endforeach()
elseif(IOS)
    set(linker_flags_ios
        "${XCODE_IOS_PLATFORM_VERSION_FLAGS}"
    )
    foreach(flag ${linker_flags_ios})
        set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${flag}")
        set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} ${flag}")
        set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} ${flag}")
    endforeach()
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

add_subdirectory(3rdparty)

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
