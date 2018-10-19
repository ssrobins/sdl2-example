set(component_name ${target_name}_${version_major}.${version_minor}.${version_patch}_${platform})

install(TARGETS ${target_name} DESTINATION ${target_name} COMPONENT ${component_name})

# Stage assets so they are available at runtime in the build directory and install directory
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/assets)
    get_target_property(is_mac_bundle ${target_name} MACOSX_BUNDLE)
    if(APPLE)
        if(CMAKE_GENERATOR STREQUAL Xcode)
            set(config $(CONFIGURATION))
        endif()

        if(${is_mac_bundle})
            if(IOS)
                set(config ${config}$(EFFECTIVE_PLATFORM_NAME))
                set(assets_dest_path ${CMAKE_CURRENT_BINARY_DIR}/${config}/${target_name}.app/assets)
            else()
                set(assets_dest_path ${CMAKE_CURRENT_BINARY_DIR}/${config}/${target_name}.app/Contents/Resources/assets)
            endif()
        else()
            set(assets_dest_path ${CMAKE_CURRENT_BINARY_DIR}/${config}/assets)
        endif()
    elseif(ANDROID)
        set(assets_dest_path ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/assets/assets)
    else()
        if(MSVC)
            set(config $(Configuration))
        endif()
        set(assets_dest_path ${CMAKE_CURRENT_BINARY_DIR}/${config}/assets)

        install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/assets DESTINATION ${target_name} COMPONENT ${component_name})
    endif()

    add_custom_command(
        TARGET ${target_name}
        POST_BUILD
        COMMAND cmake -E copy_directory
            ${CMAKE_CURRENT_SOURCE_DIR}/assets
            ${assets_dest_path}
    )

    # Stage assets so Visual Studio will find them.
    # Not needed if an absolute path is used.
    if(MSVC)
        add_custom_command(
            TARGET ${target_name}
            POST_BUILD
            COMMAND cmake -E copy_directory
                ${CMAKE_CURRENT_SOURCE_DIR}/assets
                ${CMAKE_CURRENT_BINARY_DIR}/assets
        )
    endif()
endif()

# Stage Mac bundle icon
if(APPLE AND NOT IOS)
    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/icon.icns)
        get_target_property(is_mac_bundle ${target_name} MACOSX_BUNDLE)
        if(${is_mac_bundle})
            add_custom_command(
                TARGET ${target_name}
                POST_BUILD
                COMMAND cmake -E copy
                    ${CMAKE_CURRENT_SOURCE_DIR}/icon.icns
                    ${CMAKE_CURRENT_BINARY_DIR}/${config}/${target_name}.app/Contents/Resources/icon.icns
            )
        endif()
    endif()
endif()

if(ANDROID)
    # Stage copy of gradle project for Android build and SDL's Java files
    execute_process(
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${CMAKE_SOURCE_DIR}/Android
            ${CMAKE_CURRENT_BINARY_DIR}/Android
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            ${sdl_library_path}/android-project/app/src/main/java/org/libsdl/app
            ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/java/org/libsdl/app
    )

    if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android)
        execute_process(
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_48x48.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/mipmap-mdpi/ic_launcher.png
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_72x72.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/mipmap-hdpi/ic_launcher.png
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_96x96.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/mipmap-xhdpi/ic_launcher.png
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_144x144.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_192x192.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png
            COMMAND ${CMAKE_COMMAND} -E copy
                ${CMAKE_CURRENT_SOURCE_DIR}/assets_dontship/Android/icon_512x512.png
                ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/ic_launcher-web.png
        )
    endif()

    # Process files so they include target-specific properties
    configure_file (
        ${CMAKE_SOURCE_DIR}/Android/app/src/main/AndroidManifest.xml
        ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/AndroidManifest.xml
    )
    configure_file (
        ${CMAKE_SOURCE_DIR}/Android/app/build.gradle
        ${CMAKE_CURRENT_BINARY_DIR}/Android/app/build.gradle
    )
    configure_file (
        ${CMAKE_SOURCE_DIR}/Android/templates/MainActivity.java
        ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/java/com/${company}/${target_name}/MainActivity.java
    )
    configure_file (
        ${CMAKE_SOURCE_DIR}/Android/app/src/main/res/values/strings.xml
        ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/res/values/strings.xml
    )

    # Copy native library to Android build location
    set (lib_filename ${CMAKE_SHARED_LIBRARY_PREFIX}${target_name}${CMAKE_SHARED_LIBRARY_SUFFIX})
    add_custom_command(
        TARGET ${target_name}
        POST_BUILD
        COMMAND cmake -E copy
            ${CMAKE_CURRENT_BINARY_DIR}/${lib_filename}
            ${CMAKE_CURRENT_BINARY_DIR}/Android/app/src/main/jniLibs/${CMAKE_ANDROID_ARCH_ABI}/${lib_filename}
        COMMAND sh ./gradlew assemble
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/Android
    )
endif()
