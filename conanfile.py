from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#b185e9d8c14eef5fcbce6e9fb0468c944149a4c5")
        self.build_requires("cmake_utils/0.3.1#cc144db607f04d12c0b18303a7c7d37386ce0783")

    def requirements(self):
        self.requires("sdl2/2.0.8#f45c74e900f09457e388645638c72802bd4cd081")
