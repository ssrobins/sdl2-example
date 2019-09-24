from conans import ConanFile

class Conan(ConanFile):

    settings = "os"
    generators = "cmake"

    def requirements(self):
        self.requires.add("ssrobins_engine/0.1.0#b89fc804e84394548b432a2912fd2d567f4ac2e8")
