from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#debda07d9c722b256dc83beccc487d30fffbd274")
        self.build_requires.add("cmake_utils/0.2.0#9bd58176d9770733cb8d216a9b35017ae0ee6689")

    def requirements(self):
        self.requires.add("sdl2/2.0.8#b67ad1d8b8d22cdecbe36f51a744e4ab84a28cfc")
