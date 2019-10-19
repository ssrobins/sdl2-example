from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("ssrobins_engine/0.1.0#bfdd7e61f2ae28bfee82720e4b9e9b39ff8da27d")
