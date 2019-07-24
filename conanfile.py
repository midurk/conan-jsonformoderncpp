from conans import ConanFile, CMake, tools
import os


class JsonForModernCppConan(ConanFile):
    name = "jsonformoderncpp"
    version = "3.6.1"
    settings = "os", "compiler", "arch", "build_type"
    description = "JSON for Modern C++ parser and generator from https://github.com/nlohmann/json"
    license = "MIT"
    url = "https://github.com/midurk/conan-jsonformoderncpp"
    repo_url = "https://github.com/nlohmann/json"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    exports = "arch-indep.diff"

    def source(self):
        tools.get("%s/archive/v%s.zip" % (self.repo_url, self.version))
        tools.patch(base_path="json-%s" % self.version, patch_file="arch-indep.diff")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["JSON_BuildTests"] = False
        cmake.definitions["JSON_MultipleHeaders"] = True
        cmake.configure(source_folder="json-%s" % self.version)
        cmake.install()

    def package(self):
        self.copy("LICENSE.MIT", src="json-%s" % self.version)

    def package_id(self):
        self.info.header_only()
