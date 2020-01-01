from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#debda07d9c722b256dc83beccc487d30fffbd274")
        self.build_requires.add("cmake_utils/0.3.1#95dea75496ef60374382c194489e6524e9503eb4")

    def requirements(self):
        self.requires.add("sdl2/2.0.8#0ac39a5179e1f92a0af645ee15c70760af8cf590")
