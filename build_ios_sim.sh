set -e

build_dir=build_ios_sim

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan install .. -s os=iOS -s os.version=8.0
cmake -G Xcode -DCMAKE_TOOLCHAIN_FILE=../cmake/ios.toolchain.cmake -DENABLE_BITCODE=FALSE -DIOS_PLATFORM=SIMULATOR64 ..
cmake --build . --config Release
