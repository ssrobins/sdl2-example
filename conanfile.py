from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.1.0#990c9e26dd59ee78d2fe5d1c3e2f1c544afe1dfd")
        self.build_requires("cmake_utils/4.0.0#6f1fbd5e82af9782f3cb28a040dfe34c6e5c990a")

    def requirements(self):
        self.requires("sdl2/2.0.16#9092984606ffc5911f079d363886bb8266518b40")
