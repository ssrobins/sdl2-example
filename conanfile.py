from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.3.0#9517496737c184f98924eec823064964c8123474")
        self.build_requires("cmake_utils/5.1.0#2c0d8f9dda3cac137976849bb3851fd6c4999de0")

    def requirements(self):
        self.requires("sdl2/2.0.18#f9abc4b1f200e751c41e1aab3026eeb7370b0d46")
