cmake_minimum_required(VERSION 3.25)

find_program(DOTNET_EXECUTABLE dotnet REQUIRED)

add_custom_target(HelloWorldCS ALL
    COMMAND ${DOTNET_EXECUTABLE} build -c $<CONFIG> -m "${CMAKE_CURRENT_SOURCE_DIR}/HelloWorldCS.csproj"
        /p:BaseIntermediateOutputPath="${CMAKE_CURRENT_BINARY_DIR}/obj/"
        /p:OutputPath="${CMAKE_CURRENT_BINARY_DIR}/$<CONFIG>/"
    WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    COMMENT "Building HelloWorldCS with dotnet CLI"
    VERBATIM
    USES_TERMINAL
)
