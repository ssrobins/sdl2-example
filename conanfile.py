from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#5ce8c1a310ba03a40c1b8e3f5059eecfcb287e30")
        self.build_requires("cmake_utils/0.3.1#09e87aa7b71951c0c77bbf861baaaa53c3d55830")

    def requirements(self):
        self.requires("sdl2/2.0.8#51a526f605844c5d5f73275bf3fe1ad121509866")
