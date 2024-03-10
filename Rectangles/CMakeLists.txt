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
    SDL2::SDL2-static
    SDL2::SDL2main
)

set_target_properties(Rectangles PROPERTIES
    LINKER_LANGUAGE CXX
)

if(IOS)
    set_target_properties(Rectangles PROPERTIES
        XCODE_ATTRIBUTE_PROVISIONING_PROFILE_SPECIFIER "Rectangles Development"
    )
endif()

install_executable(Rectangles)
