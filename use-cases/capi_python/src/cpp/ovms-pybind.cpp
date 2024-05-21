#include <pybind11/pybind11.h>
#include "./model_server/src/capi_frontend/server_settings.hpp"
#include "./model_server/src/status.hpp"
#include "./model_server/src/server.hpp"

namespace py = pybind11;

ovms::ServerSettingsImpl ServerSettingsNew(){
    ovms::ServerSettingsImpl serverSettings;
    serverSettings.grpcPort = 9178;
    serverSettings.restPort = 0;
    serverSettings.grpcWorkers = 1;
    serverSettings.grpcBindAddress = "0.0.0.0";
    serverSettings.restBindAddress = "0.0.0.0";
    serverSettings.metricsEnabled = false;
    serverSettings.logLevel = "INFO";
    return serverSettings;
}

// ovms::Status ServerStart(ovms::Server server, ovms::ServerSettingsImpl serverSettings, ovms::ModelsSettingsImpl modelsSettings){
//     // ovms::Status resultsStatus = server.start(&serverSettings, &modelsSettings);
//     // return resultsStatus;
//     return ovms::StatusCode::OK;
// }

PYBIND11_MODULE(ovmspybind, m) {
    // m.doc() = "pybind11 example plugin"; // optional module docstring
    
    py::class_<ovms::ServerSettingsImpl>(m, "ServerSettingsImpl")
        .def(py::init<>()) // <-- bind the default constructor
        .def_readwrite("grpcPort", &ovms::ServerSettingsImpl::grpcPort);
    m.def("ServerSettingsNew", &ServerSettingsNew, "New server settings function");

    py::class_<ovms::ModelsSettingsImpl>(m, "ModelsSettingsImpl")
        .def(py::init<>()) // <-- bind the default constructor
        .def_readwrite("configPath", &ovms::ModelsSettingsImpl::configPath);

    py::enum_<ovms::StatusCode>(m, "StatusCode")
        .value("OK", ovms::StatusCode::OK);

    // py::class_<ovms::Server>(m, "Server");
    // m.def("ServerStart", &ServerStart, "New server function");
    // m.def("ServerIsLive", &ovms::Server::isLive, "Check Server live status");
}