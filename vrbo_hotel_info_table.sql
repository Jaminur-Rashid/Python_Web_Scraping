-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 08, 2021 at 08:35 AM
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
  `Bathroom` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vrbo_hotel_info_table`
--

INSERT INTO `vrbo_hotel_info_table` (`Id`, `Location`, `Hotel_Name`, `Sleeping`, `Bedroom`, `Bathroom`) VALUES
('48756f5f-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', ' #1 Rated Condo, Oceanfront, with Bay View Too ', '6', '2', '1'),
('48756f61-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Beautiful 2 Bedroom Unit in One of the Most Popular Hi-Rises in OC', '6', '2', '2'),
('5cfacf0a-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Check_Hotel', '10', '3', '2'),
('48756f5e-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Huge Oceanfront Balcony | 3BR | 2 King Rooms | Pool | Perfect spot for families!', '10', '3', '2'),
('48756f63-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Lovely 2BR Ocean Front Property with Awesome Ocean Views & Community Pool!', '6', '2', '2'),
('48756f60-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Must See - Beautiful Oceanfront Condo On The Boardwalk - Private Balcony!', '5', '1', '1'),
('48756f62-57f7-11ec-b091-2b2f00c3950e', 'usa maryland', 'Stunning corner unit over looking the beach and the boardwalk', '8', '3', '3');

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
