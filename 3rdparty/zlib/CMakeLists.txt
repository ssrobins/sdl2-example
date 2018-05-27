set(library_name zlib)
set(library_version ${zlib_version})
set(library_fullname ${library_name}-${library_version})
set(library_path ${zlib_path})

get_archive(
    https://zlib.net/${library_fullname}.tar.gz
    ${library_fullname}
)

option(BUILD_ZLIB_EXAMPLE "Build zlib example" OFF)
option(BUILD_ZLIB_MINIGZIP "Build zlib gzip example" OFF)

# Copy over an edited CMakeLists.txt file with:
#   -New options BUILD_ZLIB_EXAMPLE and BUILD_ZLIB_MINIGZIP that allow shutting off
#    those example executable builds so I don't have to set MACOSX_BUNDLE,
#    XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY, and XCODE_ATTRIBUTE_DEVELOPMENT_TEAM to get
#    iOS builds to work
#   -MACOSX_RPATH set to ON to avoid CMake configure warning
# Submitted these changes to zlib@gzip.org
set(cmakelists_sourcepath ${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists-${library_name}.txt)
set(cmakelists_destpath ${library_path}/CMakeLists.txt)
copy_file(${cmakelists_sourcepath} ${cmakelists_destpath})

add_subdirectory(${library_path} ${library_path})
