from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("sdl2/2.0.8@stever/stable")
