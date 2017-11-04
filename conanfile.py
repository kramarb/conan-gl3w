from conans import ConanFile, CMake, tools
#import os


class Gl3wConan(ConanFile):
    name = "gl3w"
    version = "latest"
    license = "Unlicense"
    url = "https://github.com/thoughton/conan-gl3w"
    description = "Simple OpenGL core profile loading."

    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "UNLICENSE"

    def source(self):
        tools.download("https://github.com/skaslev/gl3w/raw/master/gl3w_gen.py", "gl3w_downloader/gl3w_gen.py")
        self.run("python gl3w_downloader/gl3w_gen.py --root gl3w")

    def build(self):
        cmake = CMake(self)
        self.run('cmake . %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="gl3w/include", keep_path=True)
        self.copy("*gl3w.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gl3w"]
