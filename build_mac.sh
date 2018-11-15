set -e
  
build_dir=build_mac

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan install ..
cmake -G Xcode ..
cmake --build . --config Release --target package
