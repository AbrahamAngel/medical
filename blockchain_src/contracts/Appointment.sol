// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

pragma experimental ABIEncoderV2;

contract Appointment {
    struct AppointmentDetails {
        string patientName;
        string doctorName;
        uint appointmentDate;
    }

    mapping(address => AppointmentDetails[]) public appointments;

    function createAppointment(
        string memory _patientName,
        string memory _doctorName,
        uint _appointmentDate
    ) public {
        appointments[msg.sender].push(AppointmentDetails(_patientName, _doctorName, _appointmentDate));
    }

    function getAppointments() public view returns (AppointmentDetails[] memory) {
        return appointments[msg.sender];
    }
}
