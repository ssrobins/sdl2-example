from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("sdl2/2.0.8#ece35a6c4011a59b0240d62bccb7a469ac47d6b9")
