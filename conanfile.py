from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#732c8c9ca19314c41111a1ea1a339bb1ed6cfdea")
        self.build_requires("cmake_utils/0.3.1#b92e3b563e31a4fe0e55849f3bfdb55eb7b06284")

    def requirements(self):
        self.requires("sdl2/2.0.8#cfc3fac0c9f98475f888516718b49146cc9dc8ba")
