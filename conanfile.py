from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#d299a2e1a9b1b779eb0e2bd7c11d2cf845e5f403")
        self.build_requires("cmake_utils/0.3.1#77d5f06b9b20302a5410e41ed45e7bbea7de90a5")

    def requirements(self):
        self.requires("sdl2/2.0.16#b5081764744dd13a648d8ae2ff0d0abce3d7fe91")
