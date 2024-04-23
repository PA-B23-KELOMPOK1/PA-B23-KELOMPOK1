-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 22, 2024 at 11:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kelompok1_orppp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `nama_admin` varchar(20) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id_admin`, `nama_admin`, `email`, `password`) VALUES
(1, 'rizqy', 'rizqy@gmail.com', 'rizqy01'),
(2, 'tikha', 'tikha@gmail.com', 'tikha02'),
(3, 'rizal', 'rizal@gmail.com', 'rizal03');

-- --------------------------------------------------------

--
-- Table structure for table `petani`
--

CREATE TABLE `petani` (
  `id_petani` int(11) NOT NULL,
  `nama_petani` varchar(40) DEFAULT NULL,
  `lokasi_pertanian` varchar(50) DEFAULT NULL,
  `metode_pertanian` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `petani`
--

INSERT INTO `petani` (`id_petani`, `nama_petani`, `lokasi_pertanian`, `metode_pertanian`) VALUES
(1, 'Pak Budi', 'Banyuwangi', 'Pertanian organik'),
(2, 'Bu Sri', 'Kaliwu', 'Agroforestry'),
(3, 'Bu Susi', 'Probolinggo', 'Permaculture'),
(4, 'Pak Agus', 'Banyuwangi', 'Pertanian organik'),
(5, 'Pak Irfan', 'Desa Nduari', 'Pertanian organik'),
(6, 'Bu Rini', 'Batam', 'Hidroponik'),
(7, 'Bu Dian', 'Kampung Baratan', 'Permaculture'),
(8, 'Bu Siti', 'Boyolali', 'Pertanian organik'),
(9, 'Pak Anton', 'Gianyar', 'Permaculture'),
(10, 'Bu Maya', 'Tobelo', 'Agroforestry'),
(11, 'Bu Tini', 'Gianyar', 'Permaculture'),
(12, 'Pak Anton', 'Kaliwu', 'Agroforestry'),
(13, 'Bu Dewi', 'Kepulauan Riau', 'Hidroponik'),
(14, 'Bu Astuti', 'Desa Cikurubuk', 'Pertanian organik'),
(15, 'Pak Slamet', 'Banyuwangi', 'Pertanian organik'),
(16, 'Bu Ani', 'Kampung Baratan', 'Permaculture'),
(17, 'Pak Bambang', 'Probolinggo', 'Permaculture'),
(18, 'Bu Eni', 'Boyolali', 'Pertanian organik'),
(19, 'Pak Heri', 'Kepulauan Riau', 'Hidroponik'),
(20, 'Pak Dedi', 'Desa Darsono', 'Pertanian organik'),
(21, 'Pak Joko', 'Boyolali', 'Pertanian organik'),
(22, 'Pak Sugeng', 'Desa Cianjur', 'Pertanian organik'),
(23, 'Bu Dewi', 'Desa Darsono', 'Pertanian organik'),
(24, 'Pak Mulyono', 'Desa Cikurubuk', 'Pertanian organik'),
(25, 'Pak Adi', 'Desa Cirebon', 'Pertanian organik'),
(26, 'Pak Suharto', 'Desa Sumedang', 'Permaculture'),
(27, 'Pak Hadi', 'Desa Subang', 'Pertanian organik'),
(28, 'Bu Yuli', 'Batam', 'Hidroponik'),
(29, 'Pak Slamet', 'Desa Subang', 'Permaculture'),
(30, 'Pak Agung', 'Desa Ciamis', 'Permaculture'),
(31, 'Pak Sutrisno', 'Batam', 'Hidroponik'),
(32, 'Bu Maya', 'Repong Damar', 'Agroforestry'),
(33, 'Bu Irma', 'Jawa Barat', 'Hidroponik'),
(34, 'Bu Rina', 'Jawa Barat', 'Hidroponik'),
(35, 'Bu Yuni', 'Simpunk', 'Agroforestry'),
(36, 'Pak Irfan', 'Desa Bekasi', 'Permaculture'),
(37, 'Bu Wati', 'Desa Nduari', 'Pertanian organik'),
(38, 'Bu Sinta', 'Desa Nduari', 'Pertanian organik'),
(39, 'Pak Heri', 'Desa Pangandaran', 'Pertanian organik'),
(40, 'Pak Anto', 'Desa Sumedang', 'Permaculture');

-- --------------------------------------------------------

--
-- Table structure for table `produk`
--

CREATE TABLE `produk` (
  `id_produk` int(11) NOT NULL,
  `id_petani` int(11) DEFAULT NULL,
  `nama_produk` varchar(30) DEFAULT NULL,
  `harga` varchar(12) DEFAULT NULL,
  `stok` int(11) DEFAULT NULL,
  `jenis_produk` varchar(25) DEFAULT NULL,
  `metode_produksi` varchar(20) DEFAULT NULL,
  `sertifikasi` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produk`
--

INSERT INTO `produk` (`id_produk`, `id_petani`, `nama_produk`, `harga`, `stok`, `jenis_produk`, `metode_produksi`, `sertifikasi`) VALUES
(1, 1, 'Tomat Organik', '15000', 100, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(2, 2, 'Pepaya Organik', '20000', 80, 'Buah-buahan', 'Pertanian organik', 'Sertifikasi Organik'),
(3, 3, 'Bawang Merah Lokal', '12000', 120, 'Sayuran', 'Pertanian organik', 'Sertifikasi Fair Trade'),
(4, 4, 'Apel Lokal', '25000', 60, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(5, 5, 'Selada Hijau Organik', '10000', 150, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(6, 6, 'Jeruk Manis Organik', '18000', 90, 'Buah-buahan', 'Pertanian organik', 'Sertifikasi Organik'),
(7, 7, 'Kentang Lokal', '8000', 200, 'Sayuran', 'Pertanian organik', 'Sertifikasi Fair Trade'),
(8, 8, 'Nanas Lokal', '30000', 50, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(9, 9, 'Bayam Organik', '12000', 100, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(10, 10, 'Mangga Harum Manis Organik', '22000', 70, 'Buah-buahan', 'Pertanian organik', 'Sertifikasi Organik'),
(11, 11, 'Wortel Lokal', '9000', 180, 'Sayuran', 'Pertanian organik', 'Sertifikasi Fair Trade'),
(12, 12, 'Alpukat Lokal', '28000', 40, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(13, 13, 'Brokoli Organik', '13000', 120, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(14, 14, 'Anggur Lokal', '35000', 60, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(15, 15, 'Kacang Panjang Organik', '11000', 150, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(16, 16, 'Durian Lokal', '40000', 30, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(17, 17, 'Terong Organik', '10000', 130, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(18, 18, 'Pisang Lokal', '18000', 80, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(19, 19, 'Kembang Kol Organik', '15000', 100, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(20, 20, 'Jambu Lokal', '20000', 70, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(21, 21, 'Labu Organik', '12000', 120, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(22, 22, 'Rambutan Lokal', '25000', 50, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(23, 23, 'Cabe Merah Organik', '13000', 110, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(24, 24, 'Sirsak Lokal', '30000', 40, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(25, 25, 'Kacang Hijau Organik', '10000', 140, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(26, 26, 'Srikaya Lokal', '35000', 60, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(27, 27, 'Kangkung Lokal', '9000', 160, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(28, 28, 'Nangka Lokal', '38000', 50, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(29, 29, 'Kubis Lokal', '11000', 120, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(30, 30, 'Salak Lokal', '20000', 60, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(31, 31, 'Labu Siam Lokal', '14000', 100, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(32, 32, 'Markisa Lokal', '28000', 40, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(33, 33, 'Kailan Lokal', '12000', 110, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(34, 34, 'Belimbing Lokal', '32000', 50, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(35, 35, 'Kacang Tanah Lokal', '9000', 130, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(36, 36, 'Pepino Lokal', '25000', 60, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(37, 37, 'Daun Singkong Lokal', '10000', 140, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(38, 38, 'Aprikot Lokal', '35000', 50, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc'),
(39, 39, 'Buncis Lokal', '11000', 120, 'Sayuran', 'Pertanian organik', 'Sertifikasi Organik'),
(40, 40, 'Pisang Ambon Lokal', '18000', 70, 'Buah-buahan', 'Agroforestry', 'Sertifikasi Rainforest Allianc');

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `id_user` int(11) DEFAULT NULL,
  `id_produk` int(11) DEFAULT NULL,
  `tanggal_transaksi` date DEFAULT NULL,
  `jumlah_transaksi` int(11) DEFAULT NULL,
  `metode_pembayaran` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id_transaksi`, `id_user`, `id_produk`, `tanggal_transaksi`, `jumlah_transaksi`, `metode_pembayaran`) VALUES
(1, 3, 10, '2023-04-20', 5, 'Transfer Bank'),
(2, 2, 5, '2023-04-21', 3, 'Kartu Kredit'),
(3, 4, 8, '2023-04-22', 2, 'Transfer Bank'),
(4, 1, 12, '2023-04-23', 1, 'E-Wallet'),
(5, 5, 15, '2023-04-24', 4, 'Transfer Bank'),
(6, 3, 18, '2023-04-25', 6, 'Kartu Kredit'),
(7, 7, 3, '2023-04-26', 3, 'Transfer Bank'),
(8, 6, 2, '2023-04-27', 2, 'E-Wallet'),
(9, 2, 7, '2023-04-28', 1, 'Transfer Bank'),
(10, 4, 14, '2023-04-29', 5, 'Kartu Kredit'),
(11, 1, 9, '2023-04-30', 3, 'Transfer Bank'),
(12, 6, 13, '2023-05-01', 2, 'E-Wallet'),
(13, 8, 6, '2023-05-02', 4, 'Transfer Bank'),
(14, 7, 1, '2023-05-03', 3, 'Kartu Kredit'),
(15, 5, 4, '2023-05-04', 6, 'Transfer Bank'),
(16, 3, 11, '2023-05-05', 1, 'E-Wallet'),
(17, 6, 19, '2023-05-06', 3, 'Transfer Bank'),
(18, 2, 16, '2023-05-07', 2, 'Kartu Kredit'),
(19, 4, 10, '2023-05-08', 5, 'Transfer Bank'),
(20, 7, 7, '2023-05-09', 3, 'E-Wallet'),
(21, 1, 20, '2023-05-10', 2, 'Transfer Bank'),
(22, 5, 2, '2023-05-11', 1, 'Kartu Kredit'),
(23, 8, 5, '2023-05-12', 3, 'Transfer Bank'),
(24, 3, 9, '2023-05-13', 2, 'E-Wallet'),
(25, 6, 17, '2023-05-14', 4, 'Transfer Bank'),
(26, 7, 13, '2023-05-15', 3, 'Kartu Kredit'),
(27, 4, 18, '2023-05-16', 6, 'Transfer Bank'),
(28, 2, 4, '2023-05-17', 1, 'E-Wallet'),
(29, 1, 1, '2023-05-18', 3, 'Transfer Bank'),
(30, 5, 6, '2023-05-19', 5, 'Kartu Kredit'),
(31, 8, 11, '2023-05-20', 2, 'Transfer Bank'),
(32, 7, 16, '2023-05-21', 3, 'E-Wallet'),
(33, 3, 10, '2023-05-22', 6, 'Transfer Bank'),
(34, 6, 19, '2023-05-23', 1, 'Kartu Kredit'),
(35, 2, 8, '2023-05-24', 5, 'Transfer Bank'),
(36, 4, 12, '2023-05-25', 3, 'E-Wallet'),
(37, 5, 3, '2023-05-26', 2, 'Transfer Bank'),
(38, 7, 14, '2023-05-27', 4, 'Kartu Kredit'),
(39, 1, 17, '2023-05-28', 6, 'Transfer Bank'),
(40, 8, 20, '2023-05-29', 3, 'E-Wallet');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `nama_user` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `no_telp` char(12) DEFAULT NULL,
  `alamat` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id_user`, `nama_user`, `email`, `password`, `no_telp`, `alamat`) VALUES
(1, 'Andi Surya', 'andi.surya@gmail.com', 'password12', '081234567891', 'Jl. Dago No. 123, Bandung'),
(2, 'Budi Prasetyo', 'budi.prasetyo@gmail.com', 'password45', '082345678912', 'Jl. Jendral Sudirman No. 45, Jakarta'),
(3, 'Citra Rahayu', 'citra.rahayu@gmail.com', 'password78', '083456789123', 'Jl. Ahmad Yani No. 67, Surabaya'),
(4, 'Dewi Lestari', 'dewi.lestari@gmail.com', 'passwordab', '084567891234', 'Jl. Diponegoro No. 89, Yogyakarta'),
(5, 'Eko Wijaya', 'eko.wijaya@gmail.com', 'passwordde', '085678912345', 'Jl. K.H. Hasyim Ashari No. 12, Semarang'),
(6, 'Fitri Indah', 'fitri.indah@gmail.com', 'passwordgh', '086789123456', 'Jl. Pahlawan No. 34, Medan'),
(7, 'Gita Permata', 'gita.permata@gmail.com', 'passwordjk', '087891234567', 'Jl. Gatot Subroto No. 56, Makassar'),
(8, 'Hadi Setiawan', 'hadi.setiawan@gmail.com', 'passwordmn', '088912345678', 'Jl. Kartini No. 78, Palembang'),
(9, 'Indra Gunawan', 'indra.gunawan@gmail.com', 'passwordpq', '089123456789', 'Jl. A. Yani No. 90, Malang'),
(10, 'Joko Santoso', 'joko.santoso@gmail.com', 'passwordst', '081234567890', 'Jl. Gajah Mada No. 123, Denpasar'),
(11, 'Kartika Dewi', 'kartika.dewi@gmail.com', 'passwordvw', '082345678901', 'Jl. Hayam Wuruk No. 45, Bandung'),
(12, 'Lia Putri', 'lia.putri@gmail.com', 'passwordyz', '083456789012', 'Jl. Raya Bogor No. 67, Jakarta'),
(13, 'Maulana Firdaus', 'maulana.firdaus@gmail.com', 'password23', '084567890123', 'Jl. Pemuda No. 89, Surabaya'),
(14, 'Nadia Utami', 'nadia.utami@gmail.com', 'password56', '085678901234', 'Jl. Cendrawasih No. 12, Yogyakarta'),
(15, 'Oscar Ramadhan', 'oscar.ramadhan@gmail.com', 'password89', '086789012345', 'Jl. Dipatiukur No. 34, Semarang'),
(16, 'Putra Wijaya', 'putra.wijaya@gmail.com', 'passwordab', '087891023456', 'Jl. Soekarno Hatta No. 56, Medan'),
(17, 'Rini Septiani', 'rini.septiani@gmail.com', 'passwordde', '088912345678', 'Jl. Jendral Sudirman No. 67, Makassar'),
(18, 'Satria Nugraha', 'satria.nugraha@gmail.com', 'passwordgh', '089123456789', 'Jl. Ahmad Yani No. 78, Palembang'),
(19, 'Tia Putri', 'tia.putri@gmail.com', 'passwordjk', '081234567890', 'Jl. Gatot Subroto No. 90, Malang'),
(20, 'Umar Abdullah', 'umar.abdullah@gmail.com', 'passwordmn', '082345678901', 'Jl. A. Yani No. 123, Denpasar'),
(21, 'Vina Rahmawati', 'vina.rahmawati@gmail.com', 'passwordpq', '083456789012', 'Jl. Gajah Mada No. 45, Bandung'),
(22, 'Wawan Kurniawan', 'wawan.kurniawan@gmail.com', 'passwordst', '084567890123', 'Jl. Hayam Wuruk No. 67, Jakarta'),
(23, 'Xena Kartika', 'xena.kartika@gmail.com', 'passwordvw', '085678901234', 'Jl. Raya Bogor No. 89, Surabaya'),
(24, 'Yudha Setiawan', 'yudha.setiawan@gmail.com', 'passwordyz', '086789012345', 'Jl. Pemuda No. 12, Yogyakarta'),
(25, 'Zara Pramudya', 'zara.pramudya@gmail.com', 'password23', '087891023456', 'Jl. Cendrawasih No. 34, Semarang'),
(26, 'Aldi Saputra', 'aldi.saputra@gmail.com', 'password56', '088912345678', 'Jl. Dipatiukur No. 56, Medan'),
(27, 'Bella Putri', 'bella.putri@gmail.com', 'password89', '089123456789', 'Jl. Soekarno Hatta No. 78, Makassar'),
(28, 'Cakra Wijaya', 'cakra.wijaya@gmail.com', 'passwordab', '081234567890', 'Jl. Jendral Sudirman No. 90, Palembang'),
(29, 'Dini Fitriani', 'dini.fitriani@gmail.com', 'passwordde', '082345678901', 'Jl. Ahmad Yani No. 123, Malang'),
(30, 'Edo Santoso', 'edo.santoso@gmail.com', 'passwordgh', '083456789012', 'Jl. Gatot Subroto No. 45, Denpasar'),
(31, 'Fani Septiani', 'fani.septiani@gmail.com', 'passwordjk', '084567890123', 'Jl. A. Yani No. 67, Bandung'),
(32, 'Gita Rahmawati', 'gita.rahmawati@gmail.com', 'passwordmn', '085678901234', 'Jl. Gajah Mada No. 89, Jakarta'),
(33, 'Hendra Wijaya', 'hendra.wijaya@gmail.com', 'passwordpq', '086789012345', 'Jl. Hayam Wuruk No. 12, Surabaya'),
(34, 'Indra Nugraha', 'indra.nugraha@gmail.com', 'passwordst', '087891023456', 'Jl. Raya Bogor No. 34, Yogyakarta'),
(35, 'Jasmine Kartika', 'jasmine.kartika@gmail.com', 'passwordvw', '088912345678', 'Jl. Pemuda No. 56, Semarang'),
(36, 'Kunto Pratama', 'kunto.pratama@gmail.com', 'passwordyz', '089123456789', 'Jl. Cendrawasih No. 78, Medan'),
(37, 'Laras Putri', 'laras.putri@gmail.com', 'password23', '081234567890', 'Jl. Dipatiukur No. 90, Makassar'),
(38, 'Mira Safitri', 'mira.safitri@gmail.com', 'password56', '082345678901', 'Jl. Soekarno Hatta No. 123, Palembang'),
(39, 'Nanda Wijaya', 'nanda.wijaya@gmail.com', 'password89', '083456789012', 'Jl. Jendral Sudirman No. 45, Malang'),
(40, 'Anto', 'anto.ramadhan@gmail.com', 'passwordda', '084628473077', 'Jl. Ahmad Yani No. 67, Denpasar');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `petani`
--
ALTER TABLE `petani`
  ADD PRIMARY KEY (`id_petani`);

--
-- Indexes for table `produk`
--
ALTER TABLE `produk`
  ADD PRIMARY KEY (`id_produk`),
  ADD KEY `id_petani` (`id_petani`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_user` (`id_user`),
  ADD KEY `id_produk` (`id_produk`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `petani`
--
ALTER TABLE `petani`
  MODIFY `id_petani` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `produk`
--
ALTER TABLE `produk`
  MODIFY `id_produk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `petani`
--
ALTER TABLE `petani`
  ADD CONSTRAINT `fk_petani_id_petani` FOREIGN KEY (`id_petani`) REFERENCES `produk` (`id_produk`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `produk`
--
ALTER TABLE `produk`
  ADD CONSTRAINT `produk_ibfk_1` FOREIGN KEY (`id_petani`) REFERENCES `petani` (`id_petani`);

--
-- Constraints for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`),
  ADD CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`id_produk`) REFERENCES `produk` (`id_produk`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `fk_user_id_user` FOREIGN KEY (`id_user`) REFERENCES `produk` (`id_produk`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
