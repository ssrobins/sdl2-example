from conans import ConanFile

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def build_requirements(self):
        if self.settings.os == "Android":
            self.build_requires("android_sdl2/2.6.2#da38ed876673a6da88d73f6dcb0138de5561125b")
        self.build_requires("cmake_utils/9.0.1#7f745054c87ea0007a89813a4d2c30c4c95e24b2")

    def requirements(self):
        self.requires("sdl2/2.0.22#a0ed6f0eeebba28be4a84af1ad62a427da28a922")
