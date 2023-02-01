#include "BayesElo/CResultSet.h"
#include "BayesElo/CEloRatingCUI.h"
#include <sstream>
#include <pybind11/pybind11.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(bayeselo, m) {
  py::class_<CResultSet>(m, "ResultSet")
      .def(py::init<>(), "Result Set")
      .def("append", &CResultSet::Append, "append result", py::arg("white"),
           py::arg("black"), py::arg("result"));
  py::class_<CEloRatingCUI>(m, "EloRating")
      .def(py::init<const CResultSet&, const std::vector<std::string>&>(),
           "elo rating", py::arg("result_set"), py::arg("name_list"))
      .def("mm", &CEloRatingCUI::MM, "", py::arg("theta_w") = 0,
           py::arg("theta_d") = 0)
      .def("exact_dist", &CEloRatingCUI::ExactDist, "", py::arg("player") = -1)
      .def("offset", &CEloRatingCUI::Offset, "", py::arg("offset"))
      .def("__repr__",
           [](CEloRatingCUI& a) {
             std::ostringstream oss;
             a.Ratings(oss);
             return oss.str();
           })
      .def("__str__", [](CEloRatingCUI& a) {
        std::ostringstream oss;
        a.Ratings(oss);
        return oss.str();
      });
#ifdef VERSION_INFO
  m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
  m.attr("__version__") = "dev";
#endif
}


