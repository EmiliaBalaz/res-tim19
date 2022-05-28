create table LocalDevice(
	DeviceCode varchar(50) NOT NULL , 
	Vreme datetime NOT NULL,
    ActualValue int NOT NULL,
    constraint localdevice_pk primary key (DeviceCode));