from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("sdl2/2.0.8#69c21e066605654a91aa48560889ada1b5e3913a")
