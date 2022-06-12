from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        if self.settings.os == "Android":
            self.requires("android_sdl/2.6.2#8e6f2bf8b4252725f2b4d95f2cc3676493382231")
        self.requires("cmake_utils/10.0.0#8e6f2bf8b4252725f2b4d95f2cc3676493382231")
        self.requires("sdl/2.0.22#8e6f2bf8b4252725f2b4d95f2cc3676493382231")
