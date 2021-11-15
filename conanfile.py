from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/1.0.0#33a5929ed7796027107fb57187ae4248e0faf3ce")
        self.build_requires("cmake_utils/2.0.1#bc87acc9a67867fb20e22e3c51eb4c070a9f9758")

    def requirements(self):
        self.requires("sdl2/2.0.16#c89bacace15771b7e37fd41c522d7116c717595e")
