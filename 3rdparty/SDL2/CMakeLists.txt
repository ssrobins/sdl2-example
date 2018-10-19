set(library_name SDL2)
set(library_version 2.0.8)
set(library_fullname ${library_name}-${library_version})
set(sdl_library_path ${CMAKE_CURRENT_BINARY_DIR}/${library_fullname} CACHE STRING "" FORCE)

get_archive(
    https://www.libsdl.org/release/${library_fullname}.tar.gz
    ${library_fullname}
)

option(SDL_SHARED "Build a shared version of the library" OFF)

# Copy over an edited version of the SDL2 CMakeLists.txt file with the following changes:
# https://bugzilla.libsdl.org/show_bug.cgi?id=4143
# https://bugzilla.libsdl.org/show_bug.cgi?id=4178
# https://bugzilla.libsdl.org/show_bug.cgi?id=4194
# https://bugzilla.libsdl.org/show_bug.cgi?id=4195
set(cmakelists_sourcepath ${CMAKE_CURRENT_SOURCE_DIR}/CMakeLists-${library_name}.txt)
set(cmakelists_destpath ${sdl_library_path}/CMakeLists.txt)
copy_file(${cmakelists_sourcepath} ${cmakelists_destpath})

add_subdirectory(${sdl_library_path} ${sdl_library_path})
