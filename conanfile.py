from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/1.0.0#33a5929ed7796027107fb57187ae4248e0faf3ce")
        self.build_requires("cmake_utils/1.0.0#926ac6b58f4f500187b0a004491f5d0f7ebe0ed4")

    def requirements(self):
        self.requires("sdl2/2.0.16#2eaf773d352c3a11898ebb3738ebe49f9990405d")
