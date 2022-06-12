from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        if self.settings.os == "Android":
            self.requires("android_sdl/2.6.2#94f9b35ee28227c1985125702817819f15e76186")
        self.requires("cmake_utils/10.0.1#94f9b35ee28227c1985125702817819f15e76186")
        self.requires("sdl/2.0.22#94f9b35ee28227c1985125702817819f15e76186")
