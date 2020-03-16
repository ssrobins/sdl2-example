from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#5ce8c1a310ba03a40c1b8e3f5059eecfcb287e30")
        self.build_requires("cmake_utils/0.3.1#d093c585be2418d6a664babbec39e71d6b5cd11d")

    def requirements(self):
        self.requires("sdl2/2.0.8#ecad87bc0bf63f851560e29d3b2e0d1881051544")
