from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#85f60caeb1c67dda9309809530c85f60a781b916")
        self.build_requires("cmake_utils/0.3.1#bddead915084dbfac2b4114574fae5ae8545e540")

    def requirements(self):
        self.requires("sdl2/2.0.8#1191d9c2866846bb19e3975626bc3051e00ff23e")
