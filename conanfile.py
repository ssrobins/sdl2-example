from conan import ConanFile

required_conan_version = ">=2.0.0-beta1"

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        if self.settings.os == "Android":
            self.requires("android_sdl/2.7.0@ssrobins")
        self.requires("cmake_utils/10.0.2@ssrobins")
        self.requires("sdl/2.0.22@ssrobins")
