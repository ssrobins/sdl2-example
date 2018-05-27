set(target_name Rectangles)

include(${CMAKE_SOURCE_DIR}/add_executable.cmake)

target_sources(${target_name} PRIVATE
    rectangles.c
)

target_include_directories(${target_name} PRIVATE
)

target_link_libraries(${target_name}
    SDL2-static
)

set_target_properties(${target_name}
    PROPERTIES
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

include(${CMAKE_SOURCE_DIR}/copy_files_to_binary_dir.cmake)
