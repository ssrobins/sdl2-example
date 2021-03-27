from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#a8e9c63ad2763313865f84a027b0509ab6a4208f")
        self.build_requires("cmake_utils/0.3.1#da30d52b2c5db13fc90a22140f704d67c7635319")

    def requirements(self):
        self.requires("sdl2/2.0.14#e219925dea4ac723af26595deffea181936f9b2a")
