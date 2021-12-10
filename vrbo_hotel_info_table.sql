-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 10, 2021 at 06:33 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vrboDatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `vrbo_hotel_info_table`
--

CREATE TABLE `vrbo_hotel_info_table` (
  `Id` varchar(100) NOT NULL,
  `Location` varchar(100) NOT NULL,
  `Hotel_Name` varchar(100) NOT NULL,
  `Sleeping` varchar(20) NOT NULL,
  `Bedroom` varchar(20) NOT NULL,
  `Bathroom` varchar(20) NOT NULL,
  `Price` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vrbo_hotel_info_table`
--

INSERT INTO `vrbo_hotel_info_table` (`Id`, `Location`, `Hotel_Name`, `Sleeping`, `Bedroom`, `Bathroom`, `Price`) VALUES
('a0d0d120-597a-11ec-bb94-658709469207', 'usa maryland', ' #1 Rated Condo, Oceanfront, with Bay View Too ', '6', '2', '1', '$109'),
('a0d0d122-597a-11ec-bb94-658709469207', 'usa maryland', 'Beautiful 2 Bedroom Unit in One of the Most Popular Hi-Rises in OC', '6', '2', '2', '$116'),
('a0d0d11e-597a-11ec-bb94-658709469207', 'usa maryland', 'Beautiful updated Midtown Ocean View/Block 36th St', '4', '1', 'No Bathroom', '$60'),
('a0d0d11f-597a-11ec-bb94-658709469207', 'usa maryland', 'Huge Oceanfront Balcony | 3BR | 2 King Rooms | Pool | Perfect spot for families!', '10', '3', '2', '$127'),
('a0d0d121-597a-11ec-bb94-658709469207', 'usa maryland', 'Must See - Beautiful Oceanfront Condo On The Boardwalk - Private Balcony!', '5', '1', '1', '$94'),
('a0d0d123-597a-11ec-bb94-658709469207', 'usa maryland', 'Stunning corner unit over looking the beach and the boardwalk', '8', '3', '3', '$225');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vrbo_hotel_info_table`
--
ALTER TABLE `vrbo_hotel_info_table`
  ADD PRIMARY KEY (`Hotel_Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
