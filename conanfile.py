from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.2#da38ed876673a6da88d73f6dcb0138de5561125b")
        self.build_requires("cmake_utils/9.0.0#f0a11f192f7fad4c048ff5ded59027bc043d7cb7")

    def requirements(self):
        self.requires("sdl2/2.0.22#9eef18bc748aef7bfc89e085ee925b18e60741c6")
