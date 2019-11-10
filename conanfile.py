from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#db746d43b1b7e728db3b2d280aae273da3922e68")
        self.build_requires.add("cmake_utils/0.1.0#89a9bc6923fea4dabf19de6aa6b7ddcf8667b2ee")

    def requirements(self):
        self.requires.add("sdl2/2.0.8#b67ad1d8b8d22cdecbe36f51a744e4ab84a28cfc")
