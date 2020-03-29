add_sdl2_executable(Rectangles)

target_sources(Rectangles PRIVATE
    rectangles.c
)

if(IOS)
    set(icons
        Rectangles.xcassets/AppIcon.appiconset/AppIcon1024x1024~ios-marketing.png
        Rectangles.xcassets/AppIcon.appiconset/AppIcon60x60@2x.png
        Rectangles.xcassets/AppIcon.appiconset/AppIcon76x76@2x~ipad.png
        Rectangles.xcassets/AppIcon.appiconset/AppIcon76x76~ipad.png
        Rectangles.xcassets/AppIcon.appiconset/AppIcon83.5x83.5@2x~ipad.png
    )

    target_sources(Rectangles PRIVATE
        ${icons}
    )

    set_target_properties(Rectangles PROPERTIES
        RESOURCE "${icons}"
    )

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
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

install_executable(Rectangles)
