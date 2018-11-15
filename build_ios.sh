set -e

build_name=ios

cd $(dirname "$0")
source_dir=${PWD##*/} 
build_dir=$source_dir-build-$build_name

cd ..
mkdir -p $build_dir
cd $build_dir
conan install ../$source_dir -s os=iOS -s arch=armv7 -s os.version=8.0
cmake -G Xcode -DCMAKE_TOOLCHAIN_FILE=../$source_dir/ios.toolchain.cmake -DENABLE_BITCODE=FALSE ../$source_dir
cmake --build . --config Release
