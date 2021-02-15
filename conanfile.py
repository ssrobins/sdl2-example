from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#ed934365b888c490f9dca54779d85a6e3cc3cc52")
        self.build_requires("cmake_utils/0.3.1#e474aafdec36cf92d97e781b844f390f3170f29f")

    def requirements(self):
        self.requires("sdl2/2.0.14#f467b416e317c6dae86ecfd38fbf5c2ab2072a2c")
