add_sdl_executable(Rectangles MACOSX_BUNDLE WIN32)

target_sources(Rectangles PRIVATE
    rectangles.c
)

if(APPLE)
    target_assets(Rectangles
        Rectangles.xcassets
    )
endif()

target_include_directories(Rectangles PRIVATE
)

target_link_libraries(Rectangles
    sdl::sdl
)

set_target_properties(Rectangles PROPERTIES
    LINKER_LANGUAGE CXX
)

install_executable(Rectangles)
