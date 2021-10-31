add_sdl2_executable(Rectangles MACOSX_BUNDLE WIN32)

target_sources(Rectangles PRIVATE
    rectangles.c
)

if(IOS)
    target_assets(Rectangles
        Rectangles.xcassets
    )
endif()

target_include_directories(Rectangles PRIVATE
)

target_link_libraries(Rectangles
    CONAN_PKG::sdl2
)

set_target_properties(Rectangles PROPERTIES
    LINKER_LANGUAGE CXX
)

install_executable(Rectangles)
