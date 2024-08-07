from conan import ConanFile

required_conan_version = ">=2.0.4"

class Conan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"
    default_options = {
        "sdl/*:alsa": False,
        "sdl/*:arts": False,
        "sdl/*:directfb": False,
        "sdl/*:directx": False,
        "sdl/*:esd": False,
        "sdl/*:iconv": False,
        "sdl/*:jack": False,
        "sdl/*:libunwind": False,
        "sdl/*:nas": False,
        "sdl/*:opengl": False,
        "sdl/*:opengles": False,
        "sdl/*:pulse": False,
        "sdl/*:sndio": False,
        "sdl/*:video_rpi": False,
        "sdl/*:vulkan": False,
        "sdl/*:wayland": False,
        "sdl/*:x11": False,
        "sdl/*:xcursor": False,
        "sdl/*:xinerama": False,
        "sdl/*:xinput": False,
        "sdl/*:xrandr": False,
        "sdl/*:xscrnsaver": False,
        "sdl/*:xshape": False,
        "sdl/*:xvm": False
    }

    def config_options(self):
        self.options["sdl/*"].iconv = self.settings.os == "iOS"
        self.options["sdl/*"].opengl = self.settings.os != "Android"
        self.options["sdl/*"].opengles = self.settings.os == "Android"
        self.options["sdl/*"].x11 = self.settings.os == "Linux"
        self.options["sdl/*"].xinput = self.settings.os == "Linux"

    def requirements(self):
        self.requires("sdl/2.30.4")
