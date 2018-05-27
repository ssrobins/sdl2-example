target_link_libraries(${target_name}
    gtest
    gtest_main
)

if(NOT ANDROID AND NOT IOS)
    add_test(NAME ${target_name} COMMAND ${target_name})

    # Run unit tests after the build
    add_custom_command(
        TARGET ${target_name}
        POST_BUILD
        COMMAND ctest -C $<CONFIGURATION> --output-on-failure
    )
endif()
