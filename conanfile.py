from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.2#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")
        self.build_requires("cmake_utils/9.0.1#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")

    def requirements(self):
        self.requires("sdl2/2.0.22#e5668aa2be2aa3ef28744dbe2a780c4f7f39a8a8")
