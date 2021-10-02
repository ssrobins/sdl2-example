from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#b05721a9fb7f10bd7ae3392924dcf58aa497abb9")
        self.build_requires("cmake_utils/0.3.1#77d5f06b9b20302a5410e41ed45e7bbea7de90a5")

    def requirements(self):
        self.requires("sdl2/2.0.16#558cc0716f686f17d95ee3f68ee18c240a79b20b")
