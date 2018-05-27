if(ANDROID)
    add_library(${target_name} SHARED)
else()
    add_executable(${target_name})
endif()

if(IOS)
    if(${ENABLE_BITCODE})
        set(xcode_bitcode YES)
    else()
        set(xcode_bitcode NO)
    endif()

    set_target_properties(${target_name}
        PROPERTIES
        MACOSX_BUNDLE TRUE
        XCODE_ATTRIBUTE_ENABLE_BITCODE "${xcode_bitcode}"
        XCODE_ATTRIBUTE_IPHONEOS_DEPLOYMENT_TARGET "${IOS_DEPLOYMENT_TARGET}"
        XCODE_ATTRIBUTE_CODE_SIGN_IDENTITY "${xcode_code_sign_identity}"
        XCODE_ATTRIBUTE_DEVELOPMENT_TEAM "${xcode_dev_team}"
    )
endif()
