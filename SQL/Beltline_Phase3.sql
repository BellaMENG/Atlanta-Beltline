-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: Beltline
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Administrator`
--

DROP TABLE IF EXISTS `Administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Administrator` (
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`),
  CONSTRAINT `administrator_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Administrator`
--

LOCK TABLES `Administrator` WRITE;
/*!40000 ALTER TABLE `Administrator` DISABLE KEYS */;
INSERT INTO `Administrator` VALUES ('james.smith');
/*!40000 ALTER TABLE `Administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Assign_To`
--

DROP TABLE IF EXISTS `Assign_To`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Assign_To` (
  `Username` varchar(20) NOT NULL,
  `EventName` varchar(50) NOT NULL,
  `StartDate` date NOT NULL,
  `SiteName` varchar(50) NOT NULL,
  PRIMARY KEY (`Username`,`EventName`,`StartDate`,`SiteName`),
  KEY `SiteName` (`SiteName`,`EventName`,`StartDate`),
  CONSTRAINT `assign_to_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `assign_to_ibfk_2` FOREIGN KEY (`SiteName`, `EventName`, `StartDate`) REFERENCES `event` (`sitename`, `name`, `startdate`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assign_To`
--

LOCK TABLES `Assign_To` WRITE;
/*!40000 ALTER TABLE `Assign_To` DISABLE KEYS */;
INSERT INTO `Assign_To` VALUES ('staff1','Official Atlanta BeltLine Bike Tour','2019-02-09','Atlanta BeltLine Center'),('michael.smith','Eastside Trail','2019-02-13','Historic Fourth Ward Park'),('michael.smith','Bus Tour','2019-02-01','Inman Park'),('staff2','Bus Tour','2019-02-01','Inman Park'),('michael.smith','Bus Tour','2019-02-08','Inman Park'),('robert.smith','Bus Tour','2019-02-08','Inman Park'),('robert.smith','Eastside Trail','2019-02-04','Inman Park'),('staff2','Eastside Trail','2019-02-04','Inman Park'),('staff1','Eastside Trail','2019-03-01','Inman Park'),('robert.smith','Private Bus Tour','2019-02-01','Inman Park'),('michael.smith','Eastside Trail','2019-02-04','Piedmont Park'),('staff1','Eastside Trail','2019-02-04','Piedmont Park'),('staff1','Westside Trail','2019-02-18','Westview Cemetery'),('staff3','Westside Trail','2019-02-18','Westview Cemetery');
/*!40000 ALTER TABLE `Assign_To` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Connect`
--

DROP TABLE IF EXISTS `Connect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Connect` (
  `Name` varchar(50) NOT NULL,
  `Route` varchar(20) NOT NULL,
  `TransportType` varchar(20) NOT NULL,
  PRIMARY KEY (`Name`,`Route`,`TransportType`),
  KEY `Route` (`Route`,`TransportType`),
  CONSTRAINT `connect_ibfk_1` FOREIGN KEY (`Name`) REFERENCES `site` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `connect_ibfk_2` FOREIGN KEY (`Route`, `TransportType`) REFERENCES `transit` (`route`, `transporttype`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Connect`
--

LOCK TABLES `Connect` WRITE;
/*!40000 ALTER TABLE `Connect` DISABLE KEYS */;
INSERT INTO `Connect` VALUES ('Historic Fourth Ward Park','152','Bus'),('Inman Park','152','Bus'),('Piedmont Park','152','Bus'),('Historic Fourth Ward Park','Blue','MARTA'),('Inman Park','Blue','MARTA'),('Piedmont Park','Blue','MARTA'),('Westview Cemetery','Blue','MARTA'),('Historic Fourth Ward Park','Relay','Bike'),('Piedmont Park','Relay','Bike');
/*!40000 ALTER TABLE `Connect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Emails`
--

DROP TABLE IF EXISTS `Emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Emails` (
  `Username` varchar(20) NOT NULL,
  `Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Username`,`Email`),
  CONSTRAINT `emails_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Emails`
--

LOCK TABLES `Emails` WRITE;
/*!40000 ALTER TABLE `Emails` DISABLE KEYS */;
INSERT INTO `Emails` VALUES ('david.smith','dsmith@outlook.com'),('james.smith','jsmith@gatech.edu'),('james.smith','jsmith@gmail.com'),('james.smith','jsmith@hotmail.com'),('james.smith','jsmith@outlook.com'),('manager1','m1@beltline.com'),('manager2','m2@beltline.com'),('manager3','m3@beltline.com'),('manager4','m4@beltline.com'),('manager5','m5@beltline.com'),('maria.garcia','mgarcia@gatech.edu'),('maria.garcia','mgarcia@yahoo.com'),('maria.hernandez','mh@gatech.edu'),('maria.hernandez','mh123@gmail.com'),('maria.rodriguez','mrodriguez@gmail.com'),('mary.smith','mary@outlook.com'),('michael.smith','msmith@gmail.com'),('robert.smith','rsmith@hotmail.com'),('staff1','s1@beltline.com'),('staff2','s2@beltline.com'),('staff3','s3@beltline.com'),('user1','u1@beltline.com'),('visitor1','v1@beltline.com');
/*!40000 ALTER TABLE `Emails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Employee` (
  `Username` varchar(20) NOT NULL,
  `EmployeeID` char(9) NOT NULL,
  `Phone` varchar(12) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `State` char(2) DEFAULT NULL,
  `Zipcode` char(5) DEFAULT NULL,
  PRIMARY KEY (`Username`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES ('david.smith','5','5124776435','350 Ferst Drive','Atlanta','GA','30332'),('james.smith','1','4043721234','123 East Main Street','Rochester','NY','14604'),('manager1','6','8045126767','123 East Main Street','Rochester','NY','14604'),('manager2','7','9876543210','123 East Main Street','Rochester','NY','14604'),('manager3','8','5432167890','350 Ferst Drive','Atlanta','GA','30332'),('manager4','9','8053467565','123 East Main Street','Columbus','OH','43215'),('manager5','10','8031446782','801 Atlantic Drive','Atlanta','GA','30332'),('maria.garcia','4','7890123456','123 East Main Street','Richland','PA','17987'),('michael.smith','2','4043726789','350 Ferst Drive','Atlanta','GA','30332'),('robert.smith','3','1234567890','123 East Main Street','Columbus','OH','43215'),('staff1','11','8024456765','266 Ferst Drive Northwest','Atlanta','GA','30332'),('staff2','12','8888888888','266 Ferst Drive Northwest','Atlanta','GA','30332'),('staff3','13','3333333333','801 Atlantic Drive','Atlanta','GA','30332');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Event` (
  `Name` varchar(50) NOT NULL,
  `StartDate` date NOT NULL,
  `SiteName` varchar(50) NOT NULL,
  `EndDate` date DEFAULT NULL,
  `Price` decimal(6,2) DEFAULT NULL,
  `Capacity` int(11) DEFAULT NULL,
  `MinStaffReq` int(11) DEFAULT NULL,
  `Description` text,
  PRIMARY KEY (`SiteName`,`Name`,`StartDate`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`SiteName`) REFERENCES `site` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES ('Official Atlanta Beltline Bike Tour','2019-02-09','Atlanta Beltline Center','2019-02-14',5.00,5,1,'These tours will include rest stops highlighting assets and points of interest along the Atlanta BeltLine. Staff will lead the rides, and each group will have a ride sweep to help with any unexpected mechanical difficulties.'),('Eastside Trail','2019-02-13','Historic Fourth Ward Park','2019-02-14',0.00,99999,1,'A combination of multi-use trail and linear greenspace, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/'),('Arboretum Walking Tour','2010-02-08','Inman Park','2019-02-11',5.00,5,1,'Official Atlanta BeltLine Arboretum Walking Tours provide an up-close view of the Westside Trail and the Atlanta BeltLine Arboretum led by Trees Atlanta Docents. The one and a half hour tours step off at at 10am (Oct thru May), and 9am (June thru September). Departure for all tours is from Rose Circle Park near Brown Middle School. More details at: https://beltline.org/visit/atlanta-beltline-tours/#arboretum-walking'),('Bus Tour','2019-02-01','Inman Park','2019-02-02',25.00,6,2,'The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations – Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources'),('Bus Tour','2019-02-08','Inman Park','2019-02-10',25.00,6,2,'The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations – Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources'),('Eastside Trail','2019-02-04','Inman Park','2019-02-05',0.00,99999,1,'A combination of multi-use trail and linear greenspace, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/'),('Eastside Trail','2019-03-01','Inman Park','2019-03-02',0.00,99999,1,'A combination of multi-use trail and linear greenspace, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/'),('Private Bus Tour','2019-02-01','Inman Park','2019-02-02',40.00,4,1,'Private tours are available most days, pending bus and tour guide availability. Private tours can accommodate up to 4 guests per tour, and are subject to a tour fee (nonprofit rates are available). As a nonprofit organization with limited resources, we are unable to offer free private tours. We thank you for your support and your understanding as we try to provide as many private group tours as possible. The Atlanta BeltLine Partnership’s tour program operates with a natural gas-powered, ADA accessible tour bus funded through contributions from 10th & Monroe, LLC, SunTrust Bank Trusteed Foundations – Florence C. and Harry L. English Memorial Fund and Thomas Guy Woolford Charitable Trust, and AGL Resources'),('Eastside Trail','2019-02-04','Piedmont Park','2019-02-05',0.00,99999,1,'A combination of multi-use trail and linear greenspace, the Eastside Trail was the first finished section of the Atlanta BeltLine trail in the old rail corridor. The Eastside Trail, which was funded by a combination of public and private philanthropic sources, runs from the tip of Piedmont Park to Reynoldstown. More details at https://beltline.org/explore-atlanta-beltline-trails/eastside-trail/'),('Westside Trail','2019-02-18','Westview Cemetery','2019-02-21',0.00,99999,1,'The Westside Trail is a free amenity that offers a bicycle and pedestrian-safe corridor with a 14-foot-wide multi-use trail surrounded by mature trees and grasses thanks to Trees Atlanta’s Arboretum. With 16 points of entry, 14 of which will be ADA-accessible with ramp and stair systems, the trail provides numerous access points for people of all abilities. More details at: https://beltline.org/explore-atlanta-beltline-trails/westside-trail/');
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manager`
--

DROP TABLE IF EXISTS `Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Manager` (
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`),
  CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manager`
--

LOCK TABLES `Manager` WRITE;
/*!40000 ALTER TABLE `Manager` DISABLE KEYS */;
INSERT INTO `Manager` VALUES ('david.smith'),('manager1'),('manager2'),('manager3'),('manager4'),('manager5'),('maria.garcia');
/*!40000 ALTER TABLE `Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Site`
--

DROP TABLE IF EXISTS `Site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Site` (
  `Name` varchar(50) NOT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Zipcode` char(5) DEFAULT NULL,
  `OpenEveryday` varchar(3) DEFAULT NULL,
  `Manager` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Name`),
  KEY `Manager` (`Manager`),
  CONSTRAINT `site_ibfk_1` FOREIGN KEY (`Manager`) REFERENCES `manager` (`username`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Site`
--

LOCK TABLES `Site` WRITE;
/*!40000 ALTER TABLE `Site` DISABLE KEYS */;
INSERT INTO `Site` VALUES ('Atlanta Beltline Center','112 Krog Street Northeast','30307','No','manager3'),('Historic Fourth Ward Park','680 Dallas Street Northeast','30308','Yes','manager4'),('Inman Park','','30307','Yes','david.smith'),('Piedmont Park','400 Park Drive Northeast','30306','Yes','manager2'),('Westview Cemetery','1680 Westview Drive Southwest','30310','No','manager5');
/*!40000 ALTER TABLE `Site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Staff` (
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
INSERT INTO `Staff` VALUES ('michael.smith'),('robert.smith'),('staff1'),('staff2'),('staff3');
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Take`
--

DROP TABLE IF EXISTS `Take`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Take` (
  `Username` varchar(20) NOT NULL,
  `TransportType` varchar(20) NOT NULL,
  `Route` varchar(20) NOT NULL,
  `TransitDate` date NOT NULL,
  PRIMARY KEY (`Username`,`Route`,`TransportType`,`TransitDate`),
  KEY `Route` (`Route`,`TransportType`),
  CONSTRAINT `take_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `take_ibfk_2` FOREIGN KEY (`Route`, `TransportType`) REFERENCES `transit` (`route`, `transporttype`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Take`
--

LOCK TABLES `Take` WRITE;
/*!40000 ALTER TABLE `Take` DISABLE KEYS */;
INSERT INTO `Take` VALUES ('manager2','Bus','152','2019-03-20'),('maria.hernandez','Bus','152','2019-03-20'),('maria.hernandez','Bus','152','2019-03-22'),('manager2','MARTA','Blue','2019-03-20'),('manager2','MARTA','Blue','2019-03-21'),('manager2','MARTA','Blue','2019-03-22'),('visitor1','MARTA','Blue','2019-03-21'),('manager3','Bike','Relay','2019-03-20'),('maria.hernandez','Bike','Relay','2019-03-20'),('mary.smith','Bike','Relay','2019-03-23');
/*!40000 ALTER TABLE `Take` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transit`
--

DROP TABLE IF EXISTS `Transit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Transit` (
  `Route` varchar(20) NOT NULL,
  `TransportType` varchar(20) NOT NULL,
  `Price` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`Route`,`TransportType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transit`
--

LOCK TABLES `Transit` WRITE;
/*!40000 ALTER TABLE `Transit` DISABLE KEYS */;
INSERT INTO `Transit` VALUES ('152','Bus',2.00),('Blue','MARTA',2.00),('Relay','Bike',1.00);
/*!40000 ALTER TABLE `Transit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `User` (
  `Username` varchar(20) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `Status` varchar(10) DEFAULT NULL,
  `Firstname` varchar(50) DEFAULT NULL,
  `Lastname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('david.smith','dsmith456','Approved','David','Smith'),('james.smith','jsmith123','Approved','James','Smith'),('manager1','manager1','Pending','Manager','One'),('manager2','manager2','Approved','Manager','Two'),('manager3','manager3','Approved','Manager','Three'),('manager4','manager4','Approved','Manager','Four'),('manager5','manager5','Approved','Manager','Five'),('maria.garcia','mgarcia123','Approved','Maria','Garcia'),('maria.hernandez','mhernandez','Approved','Maria','Hernandez'),('maria.rodriguez','mrodriguez','Declined','Maria','Rodriguez'),('mary.smith','msmith789','Approved','Mary','Smith'),('michael.smith','msmith456','Approved','Michael','Smith'),('robert.smith','rsmith789','Approved','Robert ','Smith'),('staff1','staff1234','Approved','Staff','One'),('staff2','staff4567','Approved','Staff','Two'),('staff3','staff7890','Approved','Staff','Three'),('user1','user123456','Pending','User','One'),('visitor1','visitor123','Approved','Visitor','One');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visit_Event`
--

DROP TABLE IF EXISTS `Visit_Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Visit_Event` (
  `Username` varchar(50) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `StartDate` date NOT NULL,
  `SiteName` varchar(50) NOT NULL,
  `EndDate` date NOT NULL,
  PRIMARY KEY (`Username`,`Name`,`StartDate`,`SiteName`,`EndDate`),
  KEY `SiteName` (`SiteName`,`Name`,`StartDate`),
  CONSTRAINT `visit_event_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `visit_event_ibfk_2` FOREIGN KEY (`SiteName`, `Name`, `StartDate`) REFERENCES `event` (`sitename`, `name`, `startdate`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visit_Event`
--

LOCK TABLES `Visit_Event` WRITE;
/*!40000 ALTER TABLE `Visit_Event` DISABLE KEYS */;
INSERT INTO `Visit_Event` VALUES ('mary.smith','Official Atlanta BeltLine Bike Tour','2019-02-09','Atlanta BeltLine Center','2019-02-10'),('visitor1','Official Atlanta BeltLine Bike Tour','2019-02-09','Atlanta BeltLine Center','2019-02-10'),('mary.smith','Eastside Trail','2019-02-13','Historic Fourth Ward Park','2019-02-13'),('mary.smith','Eastside Trail','2019-02-13','Historic Fourth Ward Park','2019-02-14'),('visitor1','Eastside Trail','2019-02-13','Historic Fourth Ward Park','2019-02-14'),('manager2','Bus Tour','2019-02-01','Inman Park','2019-02-02'),('manager4','Bus Tour','2019-02-01','Inman Park','2019-02-01'),('manager5','Bus Tour','2019-02-01','Inman Park','2019-02-02'),('maria.garcia','Bus Tour','2019-02-01','Inman Park','2019-02-02'),('mary.smith','Bus Tour','2019-02-01','Inman Park','2019-02-01'),('staff2','Bus Tour','2019-02-01','Inman Park','2019-02-02'),('mary.smith','Private Bus Tour','2019-02-01','Inman Park','2019-02-01'),('mary.smith','Private Bus Tour','2019-02-01','Inman Park','2019-02-02'),('mary.smith','Eastside Trail','2019-02-04','Piedmont Park','2019-02-04'),('mary.smith','Westside Trail','2019-02-18','Westview Cemetery','2019-02-19'),('visitor1','Westside Trail','2019-02-18','Westview Cemetery','2019-02-19');
/*!40000 ALTER TABLE `Visit_Event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visit_Site`
--

DROP TABLE IF EXISTS `Visit_Site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Visit_Site` (
  `Username` varchar(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `VisitSiteDate` date NOT NULL,
  PRIMARY KEY (`Username`,`Name`,`VisitSiteDate`),
  KEY `Name` (`Name`),
  CONSTRAINT `visit_site_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `visit_site_ibfk_2` FOREIGN KEY (`Name`) REFERENCES `site` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visit_Site`
--

LOCK TABLES `Visit_Site` WRITE;
/*!40000 ALTER TABLE `Visit_Site` DISABLE KEYS */;
INSERT INTO `Visit_Site` VALUES ('mary.smith','Atlanta Beltline Center','2019-02-01'),('mary.smith','Atlanta Beltline Center','2019-02-10'),('visitor1','Atlanta Beltline Center','2019-02-09'),('visitor1','Atlanta Beltline Center','2019-02-13'),('mary.smith','Historic Fourth Ward Park','2019-02-02'),('visitor1','Historic Fourth Ward Park','2019-02-11'),('mary.smith','Inman Park','2019-02-01'),('mary.smith','Inman Park','2019-02-02'),('mary.smith','Inman Park','2019-02-03'),('visitor1','Inman Park','2019-02-01'),('mary.smith','Piedmont Park','2019-02-02'),('visitor1','Piedmont Park','2019-02-01'),('visitor1','Piedmont Park','2019-02-11'),('visitor1','Westview Cemetery','2019-02-06');
/*!40000 ALTER TABLE `Visit_Site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Visitor`
--

DROP TABLE IF EXISTS `Visitor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Visitor` (
  `Username` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`),
  CONSTRAINT `visitor_ibfk_1` FOREIGN KEY (`Username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Visitor`
--

LOCK TABLES `Visitor` WRITE;
/*!40000 ALTER TABLE `Visitor` DISABLE KEYS */;
INSERT INTO `Visitor` VALUES ('manager2'),('manager4'),('manager5'),('maria.garcia'),('maria.rodriguez'),('mary.smith'),('michael.smith'),('staff2'),('staff3'),('visitor1');
/*!40000 ALTER TABLE `Visitor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'Beltline'
--

--
-- Dumping routines for database 'Beltline'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 21:28:29
