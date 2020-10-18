from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/0.1.0#080a2227eb3904d6c6df6bd90ff689d1cf12736e")
        self.build_requires("cmake_utils/0.3.1#cc144db607f04d12c0b18303a7c7d37386ce0783")

    def requirements(self):
        self.requires("sdl2/2.0.8#7aeaa31616b717a1fd7799edc88e95c8c03e3af1")
