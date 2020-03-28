from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#1aea09bd255829b7b78634e74c7fd296d99e4582")
        self.build_requires("cmake_utils/0.3.1#b92e3b563e31a4fe0e55849f3bfdb55eb7b06284")

    def requirements(self):
        self.requires("sdl2/2.0.8#ecad87bc0bf63f851560e29d3b2e0d1881051544")
