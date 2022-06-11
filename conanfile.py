from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def requirements(self):
        if self.settings.os == "Android":
            self.requires("android_sdl2/2.6.2#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
        self.requires("cmake_utils/9.0.1#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
        self.requires("sdl2/2.0.22#16c0041381708e6564b0a9a8ba11b0b0bd067fa2")
