add_sdl2_executable(Rectangles)

target_sources(Rectangles PRIVATE
    rectangles.c
)

target_include_directories(Rectangles PRIVATE
)

target_link_libraries(Rectangles
    CONAN_PKG::sdl2
)

set_target_properties(Rectangles
    PROPERTIES
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

install_executable(Rectangles)
