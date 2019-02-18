set -e

build_dir=build_ios

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan install .. -s os=iOS -s arch=armv7 -s os.version=8.0
cmake -G Xcode -DCMAKE_TOOLCHAIN_FILE=../cmake/ios.toolchain.cmake -DIOS_ARCH="armv7 arm64" -DENABLE_BITCODE=FALSE ..
cmake --build . --config Release
