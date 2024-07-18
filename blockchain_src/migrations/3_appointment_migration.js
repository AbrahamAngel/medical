const Appointment = artifacts.require("Appointment");

module.exports = function(deployer) {
  deployer.deploy(Appointment);
};
