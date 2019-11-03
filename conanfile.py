from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        if self.settings.os == "Android":
            self.requires.add("android_sdl2/0.1.0#f0c8143d56b20e306f788712298bb77778ef536d")
        self.requires.add("cmake_utils/0.1.0#7f17deeced79eecd4a03ba2d327bee3e5e794732")
        self.requires.add("sdl2/2.0.8#e429f599c8c7350ba1edb0e501cfb81c23df0e84")
