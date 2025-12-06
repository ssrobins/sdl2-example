cmake_minimum_required(VERSION 3.25)

# Define source files once
set(CSHARP_SOURCES
    Program.cs
)

if(CMAKE_GENERATOR MATCHES "Visual Studio")
    # Use native C# support for Visual Studio generators
    enable_language(CSharp)

    add_executable(HelloWorldCS ${CSHARP_SOURCES})

    set_target_properties(HelloWorldCS PROPERTIES
        VS_DOTNET_TARGET_FRAMEWORK_VERSION "v4.7.2"
        VS_DOTNET_REFERENCES "System"
        DOTNET_TARGET_FRAMEWORK "net8.0"
    )
else()
    # Use dotnet CLI for other generators (Ninja, etc.)
    # Search for dotnet executable
    find_program(DOTNET_EXECUTABLE dotnet)

    # If not found in PATH, try to find it via Visual Studio
    if(NOT DOTNET_EXECUTABLE AND WIN32)
        find_program(VSWHERE_EXECUTABLE
            NAMES vswhere
            PATHS "$ENV{ProgramFiles\(x86\)}/Microsoft Visual Studio/Installer"
        )

        if(VSWHERE_EXECUTABLE)
            execute_process(
                COMMAND ${VSWHERE_EXECUTABLE} -latest -requires Microsoft.Component.MSBuild -property installationPath
                OUTPUT_VARIABLE VS_INSTALLATION_PATH
                OUTPUT_STRIP_TRAILING_WHITESPACE
            )

            if(VS_INSTALLATION_PATH)
                # Try to find dotnet in Common7/IDE/CommonExtensions/Microsoft/DotNet/SDK
                find_program(DOTNET_EXECUTABLE
                    NAMES dotnet
                    PATHS "${VS_INSTALLATION_PATH}/Common7/IDE/CommonExtensions/Microsoft/DotNet/SDK"
                    NO_DEFAULT_PATH
                )
            endif()
        endif()

        # Also check Program Files for standalone .NET SDK
        if(NOT DOTNET_EXECUTABLE)
            find_program(DOTNET_EXECUTABLE
                NAMES dotnet
                PATHS "$ENV{ProgramFiles}/dotnet" "$ENV{ProgramFiles\(x86\)}/dotnet"
                NO_DEFAULT_PATH
            )
        endif()
    endif()

    if(NOT DOTNET_EXECUTABLE)
        message(FATAL_ERROR "Could not find dotnet executable. Please install .NET SDK or ensure it's in your PATH.")
    endif()

    message(STATUS "Found dotnet: ${DOTNET_EXECUTABLE}")

    add_custom_target(HelloWorldCS ALL
        COMMAND ${DOTNET_EXECUTABLE} build -c $<CONFIG> -m "${CMAKE_CURRENT_SOURCE_DIR}/HelloWorldCS.csproj"
            /p:BaseIntermediateOutputPath="${CMAKE_CURRENT_BINARY_DIR}/obj/"
            /p:OutputPath="${CMAKE_CURRENT_BINARY_DIR}/$<CONFIG>/"
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
        COMMENT "Building HelloWorldCS with dotnet CLI"
        VERBATIM
        USES_TERMINAL
    )
endif()
