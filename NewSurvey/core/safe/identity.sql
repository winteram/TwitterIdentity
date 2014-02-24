-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.25 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- Date/time:                    2012-07-06 09:39:27
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for gidb
DROP DATABASE IF EXISTS `gidb`;
CREATE DATABASE IF NOT EXISTS `gidb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `gidb`;

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `Id` VARCHAR(32) NOT NULL, 
  `Twitid` VARCHAR(32) NOT NULL, 
  `FBid` VARCHAR(32) NOT NULL, 
  `IUname` VARCHAR(32) DEFAULT NULL, 
  `Agree` tinyint(4) NOT NULL DEFAULT '0',
  `Referred_by` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `Twitid` (`Twitid`),
  KEY `FBid` (`FBid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping structure for table gidb.tw_accounttype
DROP TABLE IF EXISTS `tw_accounttype`;
CREATE TABLE IF NOT EXISTS `tw_accounttype` (
  `Id` int(4) NOT NULL AUTO_INCREMENT,
  `Value` mediumtext,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.accounttype: ~4 rows (approximately)
/*!40000 ALTER TABLE `tw_accounttype` DISABLE KEYS */;
INSERT INTO `tw_accounttype` (`Id`, `Value`) VALUES
	(1, 'Unknown'),
	(2, 'Authorized'),
	(3, 'Protected'),
	(4, 'Non_Existent');
/*!40000 ALTER TABLE `tw_accounttype` ENABLE KEYS */;


-- Dumping structure for table gidb.tw_mention
DROP TABLE IF EXISTS `tw_mention`;
CREATE TABLE IF NOT EXISTS `tw_mention` (
  `Id` bigint(20) NOT NULL,
  `UserId` varchar(32) NOT NULL,
  `SenderId` varchar(32) NOT NULL,
  `Text` longtext NOT NULL,
  `TwitterCreationDate` datetime NOT NULL,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_MentionUserId_TwitterAccountNodeId` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.tw_mention: ~0 rows (approximately)
/*!40000 ALTER TABLE `tw_mention` DISABLE KEYS */;
/*!40000 ALTER TABLE `tw_mention` ENABLE KEYS */;


-- Dumping structure for table gidb.tw_profile
DROP TABLE IF EXISTS `tw_profile`;
CREATE TABLE IF NOT EXISTS `tw_profile` (
  `Id` varchar(32) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Screen_name` varchar(22) NOT NULL,
  `Location` text DEFAULT NULL,
  `Created_at` datetime NOT NULL,
  `Favourites_count` int(11) NOT NULL,
  `Url` text DEFAULT NULL,
  `Followers_count` int(11) NOT NULL,
  `Lang` char(2) DEFAULT NULL,
  `Verified` tinyint(1) DEFAULT NULL,
  `Profile_bgd_color` char(6) DEFAULT NULL,
  `Geo_enabled` tinyint(1) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  `Time_zone` text DEFAULT NULL,
  `Friends_count` int(11) NOT NULL,
  `Statuses_count` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.tw_profile: ~0 rows (approximately)
/*!40000 ALTER TABLE `tw_profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `tw_profile` ENABLE KEYS */;


-- Dumping structure for table gidb.tw_relationship
DROP TABLE IF EXISTS `tw_relationship`;
CREATE TABLE IF NOT EXISTS `tw_relationship` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `TwitterAccountNodeId` varchar(32) NOT NULL,
  `TwitterAccountParentId` varchar(32) NOT NULL,
  `Type` int(4) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Relationships_TwitterAccountNode` (`TwitterAccountNodeId`),
  KEY `FK_Relationships_TwitterAccountNode1` (`TwitterAccountParentId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.tw_relationship: ~0 rows (approximately)
/*!40000 ALTER TABLE `tw_relationship` DISABLE KEYS */;
/*!40000 ALTER TABLE `tw_relationship` ENABLE KEYS */;


-- Dumping structure for table gidb.survey
DROP TABLE IF EXISTS `survey`;
CREATE TABLE IF NOT EXISTS `survey` (
  `Id` varchar(32) NOT NULL,
  `gender` enum('M','F','decline') DEFAULT NULL,
  `yob` year(4) DEFAULT NULL,
  `country` char(2) DEFAULT NULL,
  `ethnicity` set('white','black','latino','indian','asian','hawaiian','amind','other') DEFAULT NULL,
  `income` int(9) DEFAULT NULL,
  `edu` enum('none','elem','hs','hsgrad','college','as','bs','ms','md','phd') DEFAULT NULL,
  `party` enum('democrat','republican','constitution','green','libertarian') DEFAULT NULL,
  `party1_bond` tinyint(4) DEFAULT NULL,
  `party2_solidarity` tinyint(4) DEFAULT NULL,
  `party3_committed` tinyint(4) DEFAULT NULL,
  `party4_glad` tinyint(4) DEFAULT NULL,
  `party5_proud` tinyint(4) DEFAULT NULL,
  `party6_pleasant` tinyint(4) DEFAULT NULL,
  `party7_goodfeel` tinyint(4) DEFAULT NULL,
  `party8_think` tinyint(4) DEFAULT NULL,
  `party9_identity` tinyint(4) DEFAULT NULL,
  `party10_seemyself` tinyint(4) DEFAULT NULL,
  `party11_common_avg` tinyint(4) DEFAULT NULL,
  `party12_similar_avg` tinyint(4) DEFAULT NULL,
  `party13_common_oth` tinyint(4) DEFAULT NULL,
  `party14_similar_oth` tinyint(4) DEFAULT NULL,
  `nationality` text,
  `nation1_bond` tinyint(4) DEFAULT NULL,
  `nation2_solidarity` tinyint(4) DEFAULT NULL,
  `nation3_committed` tinyint(4) DEFAULT NULL,
  `nation4_glad` tinyint(4) DEFAULT NULL,
  `nation5_proud` tinyint(4) DEFAULT NULL,
  `nation6_pleasant` tinyint(4) DEFAULT NULL,
  `nation7_goodfeel` tinyint(4) DEFAULT NULL,
  `nation8_think` tinyint(4) DEFAULT NULL,
  `nation9_identity` tinyint(4) DEFAULT NULL,
  `nation10_seemyself` tinyint(4) DEFAULT NULL,
  `nation11_common_avg` tinyint(4) DEFAULT NULL,
  `nation12_similar_avg` tinyint(4) DEFAULT NULL,
  `nation13_common_oth` tinyint(4) DEFAULT NULL,
  `nation14_similar_oth` tinyint(4) DEFAULT NULL,
  `own_form1` varchar(32) DEFAULT NULL,
  `own_form2` varchar(32) DEFAULT NULL,
  `own_URL` text,
  `own1_bond` tinyint(4) DEFAULT NULL,
  `own2_solidarity` tinyint(4) DEFAULT NULL,
  `own3_committed` tinyint(4) DEFAULT NULL,
  `own4_glad` tinyint(4) DEFAULT NULL,
  `own5_proud` tinyint(4) DEFAULT NULL,
  `own6_pleasant` tinyint(4) DEFAULT NULL,
  `own7_goodfeel` tinyint(4) DEFAULT NULL,
  `own8_think` tinyint(4) DEFAULT NULL,
  `own9_identity` tinyint(4) DEFAULT NULL,
  `own10_seemyself` tinyint(4) DEFAULT NULL,
  `own11_common_avg` tinyint(4) DEFAULT NULL,
  `own12_similar_avg` tinyint(4) DEFAULT NULL,
  `own13_common_oth` tinyint(4) DEFAULT NULL,
  `own14_similar_oth` tinyint(4) DEFAULT NULL,
  `comments` text NOT NULL,
  `started` datetime NOT NULL,
  `ended` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table gidb.survey: ~0 rows (approximately)
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;


-- Dumping structure for table gidb.tweet
DROP TABLE IF EXISTS `tweet`;
CREATE TABLE IF NOT EXISTS `tweet` (
  `Id` bigint(20) NOT NULL,
  `UserId` varchar(32) NOT NULL,
  `IsRetweet` tinyint(1) NOT NULL,
  `TweetText` longtext NOT NULL,
  `TwitterCreationDate` datetime NOT NULL,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Tweet_TwitterAccountNode` (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.tweet: ~0 rows (approximately)
/*!40000 ALTER TABLE `tweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweet` ENABLE KEYS */;


-- Dumping structure for table gidb.twitteraccountnode
DROP TABLE IF EXISTS `twitteraccountnode`;
CREATE TABLE IF NOT EXISTS `twitteraccountnode` (
  `Id` varchar(32) NOT NULL,
  `Marked` tinyint(1) NOT NULL,
  `CreationDate` datetime NOT NULL,
  `AccountTypeId` int(11) NOT NULL DEFAULT '0',
  `PrimaryParent` varchar(32) DEFAULT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  `Seed` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Id`),
  KEY `FK_TwitterAccountNode_AccountType` (`AccountTypeId`),
  KEY `FK_TwitterAccountNode_TwitterAccountNode1` (`PrimaryParent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.twitteraccountnode: ~1 rows (approximately)
/*!40000 ALTER TABLE `twitteraccountnode` DISABLE KEYS */;
/*User Stevens Dev: 579529593*/
INSERT INTO `twitteraccountnode` (`Id`, `Marked`, `CreationDate`, `AccountTypeId`, `PrimaryParent`, `UpdatingDate`, `Seed`) VALUES
	('r7SNiaCfqJaq', 0, '2012-07-05 22:37:32', 1, NULL, NULL, 1);
/*User salut67: 472271418*/
INSERT INTO `twitteraccountnode` (`Id`, `Marked`, `CreationDate`, `AccountTypeId`, `PrimaryParent`, `UpdatingDate`, `Seed`) VALUES
	('sLSUjJunqZ6l', 0, '2012-07-05 22:37:32', 1, NULL, NULL, 1);
/*User ThomasngijolV: 182328629*/
/*INSERT INTO `twitteraccountnode` (`Id`, `Marked`, `CreationDate`, `AccountTypeId`, `PrimaryParent`, `UpdatingDate`, `Seed`) VALUES
	('rLWNipumqper', 0, '2012-07-05 22:37:32', 1, NULL, NULL, 1);*/
/*!40000 ALTER TABLE `twitteraccountnode` ENABLE KEYS */;

-- Dumping structure for table gidb.twitterconnectionaccounts
DROP TABLE IF EXISTS `twitterconnectionaccounts`;
CREATE TABLE IF NOT EXISTS `twitterconnectionaccounts` (
  `Id` varchar(32) NOT NULL,
  `AccessToken` longtext NOT NULL,
  `AccessTokenSecret` longtext NOT NULL,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  `ResetTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table gidb.twitterconnectionaccounts: ~2 rows (approximately)
/*!40000 ALTER TABLE `twitterconnectionaccounts` DISABLE KEYS */;
INSERT INTO `twitterconnectionaccounts` (`Id`, `AccessToken`, `AccessTokenSecret`, `CreationDate`, `UpdatingDate`, `ResetTime`) VALUES
	('r7SNiaCfqJaq', '472271418-APfmKALKbmeRrnZiWwy5O79g5Ii8QJ126bMo6f4', 'nEuyamDpNhvE2DQkNExjBvdMuJpgUIpYNYpk6UiPPoc', '2012-07-05 00:00:00', NULL, NULL),
	('sLSUjJunqZ6l', '579529593-wSDL0mNoIjrfdoB7Vie3fGqZQRYjbIckqziPONLR', 'G1Cc8rPO6qOngjQqXzIEqEuo6kzwO0e3lSpE5U8Db54', '2012-07-05 00:00:00', NULL, NULL);
/*!40000 ALTER TABLE `twitterconnectionaccounts` ENABLE KEYS */;

-- Dumping structure for table gidb.fbconnectionaccounts
DROP TABLE IF EXISTS `fbconnectionaccounts`;
CREATE TABLE IF NOT EXISTS `fbconnectionaccounts` (
  `Id` VARCHAR(32) NOT NULL,
  `AccessToken` VARCHAR( 120 ) NOT NULL ,
  `AppAccessToken` VARCHAR( 120 ) NOT NULL ,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  `ResetTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping structure for table gidb.visitors
DROP TABLE IF EXISTS `visitors`;
CREATE TABLE IF NOT EXISTS `visitors` (
  `visitid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `visited` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`visitid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table gidb.visitors: ~0 rows (approximately)
/*!40000 ALTER TABLE `visitors` DISABLE KEYS */;
/*!40000 ALTER TABLE `visitors` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
