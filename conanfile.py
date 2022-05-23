from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake", "cmake_find_package_multi"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.2#da38ed876673a6da88d73f6dcb0138de5561125b")
        self.build_requires("cmake_utils/7.0.0#9bf47716aeee70a8dcfc8592831a0318eb327a09")

    def requirements(self):
        self.requires("sdl2/2.0.22#9eef18bc748aef7bfc89e085ee925b18e60741c6")
