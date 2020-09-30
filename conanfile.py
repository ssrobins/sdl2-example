from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#33d7832e580dafa05810540f2808f3b070286189")
        self.build_requires("cmake_utils/0.3.1#30236679ffe9804515e8c092a744560a72ffb55a")

    def requirements(self):
        self.requires("sdl2/2.0.8#b16a079e0dd4a2a068a287212aaf9ec0cfaa1fa0")
