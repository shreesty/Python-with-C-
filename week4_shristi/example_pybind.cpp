#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <string>
#include <vector>

namespace py = pybind11;

// A simple C++ function to greet
std::string greet(const std::string &name) {
    return "Hello, " + name + "!";
}

// A function to reverse a list of integers
std::vector<int> reverse_list(const std::vector<int> &vec) {
    std::vector<int> result(vec.rbegin(), vec.rend());
    return result;
}

// Expose the functions to Python
PYBIND11_MODULE(example_pybind, m) {
    m.def("greet", &greet, "A function that greets the user");
    m.def("reverse_list", &reverse_list, "A function that reverses a list of integers");
}
