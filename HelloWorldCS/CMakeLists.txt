cmake_minimum_required(VERSION 3.25)

# Use dotnet CLI for building C# projects (works with all generators)
find_program(DOTNET_EXECUTABLE dotnet REQUIRED)

# Create a .csproj file
set(CSPROJ_CONTENT "<?xml version=\"1.0\" encoding=\"utf-8\"?>
<Project Sdk=\"Microsoft.NET.Sdk\">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <EnableDefaultCompileItems>false</EnableDefaultCompileItems>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include=\"${CMAKE_CURRENT_SOURCE_DIR}/Program.cs\" />
  </ItemGroup>
</Project>")

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/HelloWorldCS.csproj" "${CSPROJ_CONTENT}")

# Create a nuget.config to use only nuget.org
set(NUGET_CONFIG "<?xml version=\"1.0\" encoding=\"utf-8\"?>
<configuration>
  <packageSources>
    <clear />
    <add key=\"nuget.org\" value=\"https://api.nuget.org/v3/index.json\" protocolVersion=\"3\" />
  </packageSources>
</configuration>")

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/nuget.config" "${NUGET_CONFIG}")

# Add custom target to build with dotnet
add_custom_target(HelloWorldCS ALL
    COMMAND ${DOTNET_EXECUTABLE} build -c $<CONFIG> "${CMAKE_CURRENT_BINARY_DIR}/HelloWorldCS.csproj"
    WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
    COMMENT "Building HelloWorldCS with dotnet CLI"
    VERBATIM
    USES_TERMINAL
)
