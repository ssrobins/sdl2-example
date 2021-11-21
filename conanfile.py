from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/1.0.0#33a5929ed7796027107fb57187ae4248e0faf3ce")
        self.build_requires("cmake_utils/3.0.0#4e7b4d9bfca394477325cdfc8eacce8b1c82583e")

    def requirements(self):
        self.requires("sdl2/2.0.16#9092984606ffc5911f079d363886bb8266518b40")
