@echo off

set build_dir=build_windows

pushd %~dp0
mkdir %build_dir%
pushd %build_dir%

conan install .. -s arch=x86 -s compiler.runtime=MT || goto :error
cmake .. || goto :error
cmake --build . --config Release --target PACKAGE -- /m || goto :error

:error
popd
popd
exit /b %errorlevel%