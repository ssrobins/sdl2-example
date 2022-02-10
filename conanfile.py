from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.0#508b1df8b9b4b37172e71af0c64acb23a413e3c9")
        self.build_requires("cmake_utils/6.0.1#c04990b3e6de61a45c1b7a2845a7aa6daf2abf9d")

    def requirements(self):
        self.requires("sdl2/2.0.20#45420ef8e58422639bfab3f61e40d75a03091154")
