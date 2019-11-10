from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires.add("android_sdl2/0.1.0#99ca5d8f13de93355ccabef47eb90c6343d800f7")
        self.build_requires.add("cmake_utils/0.1.0#9efedba7676c460adbfbf3a98e4c51cea7d320db")

    def requirements(self):
        self.requires.add("sdl2/2.0.8#e429f599c8c7350ba1edb0e501cfb81c23df0e84")
