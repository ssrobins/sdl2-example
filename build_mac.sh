set -e
  
build_dir=build_mac

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

config=Release

conan install --update ..

cmake -G Xcode ..

cmake --build . --config $config

ctest -C $config --output-on-failure

cpack
