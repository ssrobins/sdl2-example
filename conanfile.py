from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#b276f95f39b2d5afe404751198b15c400938844d")
        self.build_requires("cmake_utils/0.3.1#2e2e0de4635e8c3a83655a207c63ad34ba1dadd7")

    def requirements(self):
        self.requires("sdl2/2.0.16#e48e0f700a2932b3c19dcc83fac49275cf8d5efc")
