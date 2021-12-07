from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.1.0#4631baf96c5937b22753e9ac1146265ca3b32aff")
        self.build_requires("cmake_utils/5.0.0#1ecfed8c68a43ea17d321701cc8a91df21d06453")

    def requirements(self):
        self.requires("sdl2/2.0.18#f9abc4b1f200e751c41e1aab3026eeb7370b0d46")
