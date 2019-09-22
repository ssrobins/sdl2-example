from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("ssrobins_engine/0.1.0#d3e7ff5bda36e861325826ea6a224a496d0308e2")
