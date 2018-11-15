set -e

build_dir=build_android

cd $(dirname "$0")
mkdir -p $build_dir
cd $build_dir

conan install .. -s os=Android -s os.api_level=${android_sdk_version} -s arch=armv7 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++11
cmake -DCMAKE_SYSTEM_NAME=Android -DCMAKE_SYSTEM_VERSION=${android_sdk_version} -DCMAKE_ANDROID_ARCH_ABI=armeabi-v7a -DCMAKE_ANDROID_NDK=$ANDROID_HOME/android-ndk-${android_ndk_version} -DCMAKE_ANDROID_NDK_TOOLCHAIN_VERSION=clang -DCMAKE_ANDROID_STL_TYPE=c++_static -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --config Release
