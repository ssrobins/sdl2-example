set(target_name Rectangles)

add_sdl2_executable(${target_name})

target_sources(${target_name} PRIVATE
    rectangles.c
)

target_include_directories(${target_name} PRIVATE
)

target_link_libraries(${target_name}
    CONAN_PKG::sdl2
)

set_target_properties(${target_name}
    PROPERTIES
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

install_executable(${target_name})
