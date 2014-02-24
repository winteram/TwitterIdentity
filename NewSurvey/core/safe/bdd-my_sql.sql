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

-- Dumping database structure for twittergraph
DROP DATABASE IF EXISTS `twittergraph`;
CREATE DATABASE IF NOT EXISTS `twittergraph` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `twittergraph`;


-- Dumping structure for table twittergraph.accounttype
DROP TABLE IF EXISTS `accounttype`;
CREATE TABLE IF NOT EXISTS `accounttype` (
  `Id` int(4) NOT NULL AUTO_INCREMENT,
  `Value` mediumtext,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.accounttype: ~4 rows (approximately)
/*!40000 ALTER TABLE `accounttype` DISABLE KEYS */;
INSERT INTO `accounttype` (`Id`, `Value`) VALUES
	(1, 'Unknown'),
	(2, 'Authorized'),
	(3, 'Protected'),
	(4, 'Non_Existent');
/*!40000 ALTER TABLE `accounttype` ENABLE KEYS */;


-- Dumping structure for table twittergraph.mention
DROP TABLE IF EXISTS `mention`;
CREATE TABLE IF NOT EXISTS `mention` (
  `Id` bigint(20) NOT NULL,
  `UserId` varchar(32) NOT NULL,
  `SenderId` varchar(32) NOT NULL,
  `Text` longtext NOT NULL,
  `TwitterCreationDate` datetime NOT NULL,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_MentionUserId_TwitterAccountNodeId` (`UserId`),
  CONSTRAINT `FK_MentionUserId_TwitterAccountNodeId` FOREIGN KEY (`UserId`) REFERENCES `twitteraccountnode` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.mention: ~0 rows (approximately)
/*!40000 ALTER TABLE `mention` DISABLE KEYS */;
/*!40000 ALTER TABLE `mention` ENABLE KEYS */;


-- Dumping structure for table twittergraph.profile
DROP TABLE IF EXISTS `profile`;
CREATE TABLE IF NOT EXISTS `profile` (
  `Id` varchar(32) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Screen_name` varchar(16) NOT NULL,
  `Location` text NOT NULL,
  `Created_at` datetime NOT NULL,
  `Favourites_count` int(11) NOT NULL,
  `Url` text NOT NULL,
  `Followers_count` int(11) NOT NULL,
  `Lang` char(2) NOT NULL,
  `Verified` tinyint(1) NOT NULL,
  `Profile_bgd_color` char(6) NOT NULL,
  `Geo_enabled` tinyint(1) NOT NULL,
  `Description` text NOT NULL,
  `Time_zone` text NOT NULL,
  `Friends_count` int(11) NOT NULL,
  `Statuses_count` int(11) NOT NULL,
  PRIMARY KEY (`Id`),
  CONSTRAINT `FK_ProfileId_TwitterAccountNodeId` FOREIGN KEY (`Id`) REFERENCES `twitteraccountnode` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.profile: ~0 rows (approximately)
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;


-- Dumping structure for table twittergraph.relationship
DROP TABLE IF EXISTS `relationship`;
CREATE TABLE IF NOT EXISTS `relationship` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `TwitterAccountNodeId` varchar(32) NOT NULL,
  `TwitterAccountParentId` varchar(32) NOT NULL,
  `Type` int(4) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `FK_Relationships_TwitterAccountNode` (`TwitterAccountNodeId`),
  KEY `FK_Relationships_TwitterAccountNode1` (`TwitterAccountParentId`),
  CONSTRAINT `FK_Relationships_TwitterAccountNode_Child` FOREIGN KEY (`TwitterAccountNodeId`) REFERENCES `twitteraccountnode` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_Relationships_TwitterAccountNode_Parent` FOREIGN KEY (`TwitterAccountParentId`) REFERENCES `twitteraccountnode` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.relationship: ~0 rows (approximately)
/*!40000 ALTER TABLE `relationship` DISABLE KEYS */;
/*!40000 ALTER TABLE `relationship` ENABLE KEYS */;


-- Dumping structure for table twittergraph.survey
DROP TABLE IF EXISTS `survey`;
CREATE TABLE IF NOT EXISTS `survey` (
  `Id` varchar(32) NOT NULL,
  `username` varchar(16) NOT NULL,
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
  PRIMARY KEY (`Id`),
  KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table twittergraph.survey: ~0 rows (approximately)
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;


-- Dumping structure for table twittergraph.tweet
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
  KEY `FK_Tweet_TwitterAccountNode` (`UserId`),
  CONSTRAINT `FK_Tweet_TwitterAccountNode` FOREIGN KEY (`UserId`) REFERENCES `twitteraccountnode` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.tweet: ~0 rows (approximately)
/*!40000 ALTER TABLE `tweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `tweet` ENABLE KEYS */;


-- Dumping structure for table twittergraph.twitteraccountnode
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
  KEY `FK_TwitterAccountNode_TwitterAccountNode1` (`PrimaryParent`),
  CONSTRAINT `FK_TwitterAccountNode_AccountType` FOREIGN KEY (`AccountTypeId`) REFERENCES `accounttype` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `FK_TwitterAccountNode_TwitterAccountNode_PrimaryParent` FOREIGN KEY (`PrimaryParent`) REFERENCES `twitteraccountnode` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.twitteraccountnode: ~1 rows (approximately)
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


-- Dumping structure for table twittergraph.twitterconnectionaccounts
DROP TABLE IF EXISTS `twitterconnectionaccounts`;
CREATE TABLE IF NOT EXISTS `twitterconnectionaccounts` (
  `Id` varchar(32) NOT NULL,
  `AccountName` longtext NOT NULL,
  `AccessToken` longtext NOT NULL,
  `AccessTokenSecret` longtext NOT NULL,
  `CreationDate` datetime NOT NULL,
  `UpdatingDate` datetime DEFAULT NULL,
  `ResetTime` datetime DEFAULT NULL,
  `Agree1` tinyint(4) NOT NULL DEFAULT '0',
  `Agree2` tinyint(4) NOT NULL DEFAULT '0',
  `Referred_by` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  CONSTRAINT `FK_TwitterConnectionAccountsId_TwitterAccountNodeId` FOREIGN KEY (`Id`) REFERENCES `twitteraccountnode` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table twittergraph.twitterconnectionaccounts: ~2 rows (approximately)
/*!40000 ALTER TABLE `twitterconnectionaccounts` DISABLE KEYS */;
INSERT INTO `twitterconnectionaccounts` (`Id`, `AccountName`, `AccessToken`, `AccessTokenSecret`, `CreationDate`, `UpdatingDate`, `ResetTime`) VALUES
	('r7SNiaCfqJaq', 'salut67', '472271418-APfmKALKbmeRrnZiWwy5O79g5Ii8QJ126bMo6f4', 'nEuyamDpNhvE2DQkNExjBvdMuJpgUIpYNYpk6UiPPoc', '2012-07-05 00:00:00', NULL, NULL),
	('sLSUjJunqZ6l', 'StevensDev', '579529593-wSDL0mNoIjrfdoB7Vie3fGqZQRYjbIckqziPONLR', 'G1Cc8rPO6qOngjQqXzIEqEuo6kzwO0e3lSpE5U8Db54', '2012-07-05 00:00:00', NULL, NULL);
/*!40000 ALTER TABLE `twitterconnectionaccounts` ENABLE KEYS */;


-- Dumping structure for table twittergraph.visitors
DROP TABLE IF EXISTS `visitors`;
CREATE TABLE IF NOT EXISTS `visitors` (
  `visitid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `visited` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`visitid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table twittergraph.visitors: ~0 rows (approximately)
/*!40000 ALTER TABLE `visitors` DISABLE KEYS */;
/*!40000 ALTER TABLE `visitors` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
