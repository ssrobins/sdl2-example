set -e

build_dir=build_android-v7a

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

export android_min_sdk_version=16

conan install --update .. -s os=Android -s os.api_level=$android_min_sdk_version -s arch=armv7 -s compiler=clang -s compiler.version=8 -s compiler.libcxx=libc++

cmake -DANDROID_PLATFORM=android-$android_min_sdk_version -DANDROID_ABI=armeabi-v7a -DANDROID_TOOLCHAIN=clang -DANDROID_STL=c++_static -DCMAKE_TOOLCHAIN_FILE=$ANDROID_HOME/android-ndk-${android_ndk_version}/build/cmake/android.toolchain.cmake -DCMAKE_BUILD_TYPE=Release ..

cmake --build . --target package -- -j 4
