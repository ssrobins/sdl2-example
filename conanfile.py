from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#1d2ac253f9887def0813161c99f252f08e127f1f")
        self.build_requires("cmake_utils/0.3.1#9ea936d419d454af4927845a23b913923ceaa29a")

    def requirements(self):
        self.requires("sdl2/2.0.8#cfc3fac0c9f98475f888516718b49146cc9dc8ba")
