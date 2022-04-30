from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.2#da38ed876673a6da88d73f6dcb0138de5561125b")
        self.build_requires("cmake_utils/6.1.0#9ced9bcfd95178b35d2ec5955b725a5652dbda26")

    def requirements(self):
        self.requires("sdl2/2.0.22#818215441000572b96461f775dce5f47cdf15761")
