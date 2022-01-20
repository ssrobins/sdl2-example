from conans import ConanFile

class Conan(ConanFile):
    settings = "os"
    generators = "cmake"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.4.0#41295dd86e5d152269019ea03930766db0c0bddc")
        self.build_requires("cmake_utils/6.0.0#ac1a71244046f44f5484a554918f6a42a1f86d99")

    def requirements(self):
        self.requires("sdl2/2.0.20#45420ef8e58422639bfab3f61e40d75a03091154")
