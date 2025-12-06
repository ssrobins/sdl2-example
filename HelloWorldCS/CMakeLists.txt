cmake_minimum_required(VERSION 3.25)

enable_language(CSharp)

add_executable(HelloWorldCS Program.cs)

set_target_properties(HelloWorldCS PROPERTIES
    VS_DOTNET_TARGET_FRAMEWORK_VERSION "v4.7.2"
    VS_DOTNET_REFERENCES "System"
    DOTNET_TARGET_FRAMEWORK "net6.0"
)
