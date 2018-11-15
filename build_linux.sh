set -e
  
build_dir=build_linux

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan install ..
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --target package -- -j 4
