-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `username` varchar(25) DEFAULT NULL,
  `passwd` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('system','library@123'),('suresh','admin@2'),('atharv','arron09');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `agri_books`
--

DROP TABLE IF EXISTS `agri_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agri_books` (
  `section` int NOT NULL AUTO_INCREMENT,
  `books` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `Book_code` int DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`section`),
  UNIQUE KEY `Book_code` (`Book_code`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agri_books`
--

LOCK TABLES `agri_books` WRITE;
/*!40000 ALTER TABLE `agri_books` DISABLE KEYS */;
INSERT INTO `agri_books` VALUES (2,'Soil Mechanic','B.C.Punmai',1971,'Laxmi publication',680,'avaliable'),(3,'Applied Mechanic','R.B.Bhaskar',1543,'B-Tech',250,'avaliable');
/*!40000 ALTER TABLE `agri_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ce_books`
--

DROP TABLE IF EXISTS `ce_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ce_books` (
  `section` int NOT NULL AUTO_INCREMENT,
  `books` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `Book_code` int DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`section`),
  UNIQUE KEY `Book_code` (`Book_code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ce_books`
--

LOCK TABLES `ce_books` WRITE;
/*!40000 ALTER TABLE `ce_books` DISABLE KEYS */;
INSERT INTO `ce_books` VALUES (2,'Strutural Enginnering','V.K.Salunke',3540,'I-Scheme',599,'avaliable');
/*!40000 ALTER TABLE `ce_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cse_books`
--

DROP TABLE IF EXISTS `cse_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cse_books` (
  `section` int NOT NULL AUTO_INCREMENT,
  `books` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `Book_code` int DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`section`),
  UNIQUE KEY `Book_code` (`Book_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cse_books`
--

LOCK TABLES `cse_books` WRITE;
/*!40000 ALTER TABLE `cse_books` DISABLE KEYS */;
INSERT INTO `cse_books` VALUES (4,'JAVA ','V.K.Kaushalya',5580,'I-Scheme',459,'avaliable'),(5,'Visual Basic','V.B.Patel',5541,'B-Scheme',290,'Issued');
/*!40000 ALTER TABLE `cse_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ee_books`
--

DROP TABLE IF EXISTS `ee_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ee_books` (
  `section` int NOT NULL AUTO_INCREMENT,
  `books` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `Book_code` int DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`section`),
  UNIQUE KEY `Book_code` (`Book_code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ee_books`
--

LOCK TABLES `ee_books` WRITE;
/*!40000 ALTER TABLE `ee_books` DISABLE KEYS */;
INSERT INTO `ee_books` VALUES (2,'Renewable Energy technology','M.P.Patil',9096,'I-Scheme',150,'avaliable');
/*!40000 ALTER TABLE `ee_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_book`
--

DROP TABLE IF EXISTS `issue_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_book` (
  `Book_code` int NOT NULL,
  `issued_book` varchar(40) DEFAULT NULL,
  `id` int DEFAULT NULL,
  `Student_name` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_book`
--

LOCK TABLES `issue_book` WRITE;
/*!40000 ALTER TABLE `issue_book` DISABLE KEYS */;
INSERT INTO `issue_book` VALUES (5541,'Visual Basic',1103,'Jatin.M.Sawant');
/*!40000 ALTER TABLE `issue_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `me_books`
--

DROP TABLE IF EXISTS `me_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `me_books` (
  `section` int NOT NULL AUTO_INCREMENT,
  `books` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `Book_code` int DEFAULT NULL,
  `publisher` varchar(30) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Status` varchar(20) NOT NULL,
  PRIMARY KEY (`section`),
  UNIQUE KEY `Book_code` (`Book_code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `me_books`
--

LOCK TABLES `me_books` WRITE;
/*!40000 ALTER TABLE `me_books` DISABLE KEYS */;
INSERT INTO `me_books` VALUES (2,'Basic Workshop','S.H.Shevale',7129,'E-Scheme',300,'avaliable');
/*!40000 ALTER TABLE `me_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `ID` int DEFAULT NULL,
  `Student_name` varchar(80) DEFAULT NULL,
  `Trade` varchar(20) DEFAULT NULL,
  `Contact` bigint DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `username` varchar(25) DEFAULT NULL,
  `passwd` varchar(25) DEFAULT NULL,
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1101,'Rahul.M.Patil','TYCO',8976459835,'patilrahul04@gmail.com','rahul1102','patil8976'),(1102,'Atharv.V.Sultanpure','TYCO',9561864602,'atharvsultan@gmail.com','atharv1102','sultan9561'),(1103,'Jatin.M.Sawant','B.Tech',6729562865,'jatinsawant45@gmail.com','sawant6729','Jatin1102'),(1104,'Omkar.P.More','B-Tech',9900897834,'moreomkar45@gmail.com','omkar1104','more9900');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-29 12:54:33
