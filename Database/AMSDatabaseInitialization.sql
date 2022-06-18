create table LocalDevice(
	id int NOT NULL AUTO_INCREMENT,
	DeviceCode varchar(50) NOT NULL , 
	Vreme datetime NOT NULL,
    ActualValue int NOT NULL,
    constraint localdevice_pk primary key (id));