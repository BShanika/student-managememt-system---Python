-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 08, 2024 at 03:57 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `std`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `ID` varchar(50) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `DOB` varchar(100) NOT NULL,
  `Grade` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Contact_No` varchar(50) NOT NULL,
  `Guardian_Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`ID`, `Name`, `Gender`, `DOB`, `Grade`, `Address`, `Contact_No`, `Guardian_Name`) VALUES
('001', 'Emma', 'Female', '2000/01/08', '5', 'Colombo', '712223311', 'Lucas'),
('002', 'Oliver', 'Male', '1999/05/03', '6', 'Jafna', '776661122', 'Maya'),
('003', 'Anne', 'Female', '2003/05/10', '4', 'Kandy', '7745451111', 'Sam'),
('004', 'Sophia', 'Female', '2007/09/07', '2', 'Galle', '0779004545', 'Liam'),
('005', 'Alex', 'Male', '1998/09/01', '7', 'Matara', '0784400111', 'Chloe');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
