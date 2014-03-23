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
  `party0_bond` tinyint(4) DEFAULT NULL,
  `party1_solidarity` tinyint(4) DEFAULT NULL,
  `party2_committed` tinyint(4) DEFAULT NULL,
  `party3_glad` tinyint(4) DEFAULT NULL,
  `party4_proud` tinyint(4) DEFAULT NULL,
  `party5_pleasant` tinyint(4) DEFAULT NULL,
  `party6_goodfeel` tinyint(4) DEFAULT NULL,
  `party7_think` tinyint(4) DEFAULT NULL,
  `party8_identity` tinyint(4) DEFAULT NULL,
  `party9_seemyself` tinyint(4) DEFAULT NULL,
  `party10_common_avg` tinyint(4) DEFAULT NULL,
  `party11_similar_avg` tinyint(4) DEFAULT NULL,
  `party12_common_oth` tinyint(4) DEFAULT NULL,
  `party13_similar_oth` tinyint(4) DEFAULT NULL,
  `own_form11` varchar(32) DEFAULT NULL,
  `own_form12` varchar(32) DEFAULT NULL,
  `own_URL1` text,
  `own_form21` varchar(32) DEFAULT NULL,
  `own_form22` varchar(32) DEFAULT NULL,
  `own_URL2` text,
  `own_form31` varchar(32) DEFAULT NULL,
  `own_form32` varchar(32) DEFAULT NULL,
  `own_URL3` text,
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
  `fb_comments` text DEFAULT NULL,
  `fb_feel` tinyint(4) DEFAULT NULL,
  `fb_feel_comments` text DEFAULT NULL,
  `fb_doing` tinyint(4) DEFAULT NULL,
  `fb_doing_comments` text DEFAULT NULL,
  `fb_where` tinyint(4) DEFAULT NULL,
  `fb_where_comments` text DEFAULT NULL,
  `fb_entertain` tinyint(4) DEFAULT NULL,
  `fb_entertain_comments` text DEFAULT NULL,
  `fb_political` tinyint(4) DEFAULT NULL,
  `fb_political_comments` text DEFAULT NULL,
  `fb_family` tinyint(4) DEFAULT NULL,
  `fb_family_comments` text DEFAULT NULL,
  `fb_god` tinyint(4) DEFAULT NULL,
  `fb_god_comments` text DEFAULT NULL,
  `fb_academic` tinyint(4) DEFAULT NULL,
  `fb_academic_comments` text DEFAULT NULL,
  `fb_appearance` tinyint(4) DEFAULT NULL,
  `fb_appearance_comments` text DEFAULT NULL,
  `tw_comments` text DEFAULT NULL,
  `tw_feel` tinyint(4) DEFAULT NULL,
  `tw_feel_comments` text DEFAULT NULL,
  `tw_doing` tinyint(4) DEFAULT NULL,
  `tw_doing_comments` text DEFAULT NULL,
  `tw_where` tinyint(4) DEFAULT NULL,
  `tw_where_comments` text DEFAULT NULL,
  `tw_entertain` tinyint(4) DEFAULT NULL,
  `tw_entertain_comments` text DEFAULT NULL,
  `tw_political` tinyint(4) DEFAULT NULL,
  `tw_political_comments` text DEFAULT NULL,
  `tw_family` tinyint(4) DEFAULT NULL,
  `tw_family_comments` text DEFAULT NULL,
  `tw_god` tinyint(4) DEFAULT NULL,
  `tw_god_comments` text DEFAULT NULL,
  `tw_academic` tinyint(4) DEFAULT NULL,
  `tw_academic_comments` text DEFAULT NULL,
  `tw_appearance` tinyint(4) DEFAULT NULL,
  `tw_appearance_comments` text DEFAULT NULL,
  `con_agree_0` tinyint(4) DEFAULT NULL,
  `con_agree_1` tinyint(4) DEFAULT NULL,
  `con_agree_2` tinyint(4) DEFAULT NULL,
  `con_agree_3` tinyint(4) DEFAULT NULL,
  `con_agree_4` tinyint(4) DEFAULT NULL,
  `con_agree_5` tinyint(4) DEFAULT NULL,
  `con_agree_6` tinyint(4) DEFAULT NULL,
  `con_agree_7` tinyint(4) DEFAULT NULL,
  `con_agree_8` tinyint(4) DEFAULT NULL,
  `con_agree_9` tinyint(4) DEFAULT NULL,
  `con_agree_10` tinyint(4) DEFAULT NULL,
  `con_agree_11` tinyint(4) DEFAULT NULL,
  `con_agree_12` tinyint(4) DEFAULT NULL,
  `con_agree_13` tinyint(4) DEFAULT NULL,
  `con_agree_14` tinyint(4) DEFAULT NULL,
  `con_agree_15` tinyint(4) DEFAULT NULL,
  `con_agree_16` tinyint(4) DEFAULT NULL,
  `con_agree_17` tinyint(4) DEFAULT NULL,
  `con_agree_18` tinyint(4) DEFAULT NULL,
  `con_agree_19` tinyint(4) DEFAULT NULL,
  `con_agree_20` tinyint(4) DEFAULT NULL,
  `con_agree_21` tinyint(4) DEFAULT NULL,
  `con_agree_22` tinyint(4) DEFAULT NULL,
  `con_agree_23` tinyint(4) DEFAULT NULL,
  `con_agree_24` tinyint(4) DEFAULT NULL,
  `con_agree_25` tinyint(4) DEFAULT NULL,
  `con_agree_26` tinyint(4) DEFAULT NULL,
  `con_agree_27` tinyint(4) DEFAULT NULL,
  `con_agree_28` tinyint(4) DEFAULT NULL,
  `con_agree_29` tinyint(4) DEFAULT NULL,
  `con_agree_30` tinyint(4) DEFAULT NULL,
  `con_agree_31` tinyint(4) DEFAULT NULL,
  `con_agree_32` tinyint(4) DEFAULT NULL,
  `con_agree_33` tinyint(4) DEFAULT NULL,
  `con_agree_34` tinyint(4) DEFAULT NULL,
  `interested`  tinyint(4) DEFAULT NULL,
  `distressed`  tinyint(4) DEFAULT NULL,
  `excited`  tinyint(4) DEFAULT NULL,
  `upset`  tinyint(4) DEFAULT NULL,
  `strong`  tinyint(4) DEFAULT NULL,
  `guitly`  tinyint(4) DEFAULT NULL,
  `scared`  tinyint(4) DEFAULT NULL,
  `hostile`  tinyint(4) DEFAULT NULL,
  `enthusiastic`  tinyint(4) DEFAULT NULL,
  `proud`  tinyint(4) DEFAULT NULL,
  `tired`  tinyint(4) DEFAULT NULL,
  `irritable`  tinyint(4) DEFAULT NULL,
  `alert`  tinyint(4) DEFAULT NULL,
  `ashamed`  tinyint(4) DEFAULT NULL,
  `inspired`  tinyint(4) DEFAULT NULL,
  `nervous`  tinyint(4) DEFAULT NULL,
  `determined`  tinyint(4) DEFAULT NULL,
  `attentive`  tinyint(4) DEFAULT NULL,
  `jittery`  tinyint(4) DEFAULT NULL,
  `active`  tinyint(4) DEFAULT NULL,
  `afraid`  tinyint(4) DEFAULT NULL,

  `comments` text NOT NULL,
  `started` datetime NOT NULL,
  `ended` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table gidb.survey: ~0 rows (approximately)
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;

DROP TABLE IF EXISTS `aspects`;
CREATE TABLE IF NOT EXISTS `aspects` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `UserId` varchar(32) NOT NULL,
  `name` varchar(32) NOT NULL,
  `Label` int(9),
  `Positive` int(9),
  `Important` int(9),
  `Facebook` int(9),
  `Twitter` int(9),
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `traits`;
CREATE TABLE IF NOT EXISTS `traits` (
  `Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Trait` varchar(32) NOT NULL
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `traits` VALUES ('capable');
INSERT INTO `traits` VALUES ('comfortable');
INSERT INTO `traits` VALUES ('communicative');
INSERT INTO `traits` VALUES ('confident');
INSERT INTO `traits` VALUES ('disagreeing');
INSERT INTO `traits` VALUES ('disorganized');
INSERT INTO `traits` VALUES ('energetic');
INSERT INTO `traits` VALUES ('friendly');
INSERT INTO `traits` VALUES ('fun and entertaining');
INSERT INTO `traits` VALUES ('giving');
INSERT INTO `traits` VALUES ('happy');
INSERT INTO `traits` VALUES ('hardworking');
INSERT INTO `traits` VALUES ('hopeless');
INSERT INTO `traits` VALUES ('immature');
INSERT INTO `traits` VALUES ('incompetent');
INSERT INTO `traits` VALUES ('indecisive');
INSERT INTO `traits` VALUES ('independent');
INSERT INTO `traits` VALUES ('inferior');
INSERT INTO `traits` VALUES ('insecure');
INSERT INTO `traits` VALUES ('intelligent');
INSERT INTO `traits` VALUES ('interested');
INSERT INTO `traits` VALUES ('irresponsible');
INSERT INTO `traits` VALUES ('irritable');
INSERT INTO `traits` VALUES ('isolated');
INSERT INTO `traits` VALUES ('lazy');
INSERT INTO `traits` VALUES ('like a failure');
INSERT INTO `traits` VALUES ('lovable');
INSERT INTO `traits` VALUES ('mature');
INSERT INTO `traits` VALUES ('needed');
INSERT INTO `traits` VALUES ('optimistic');
INSERT INTO `traits` VALUES ('organized');
INSERT INTO `traits` VALUES ('outgoing');
INSERT INTO `traits` VALUES ('sad and blue');
INSERT INTO `traits` VALUES ('self-centered');
INSERT INTO `traits` VALUES ('successful');
INSERT INTO `traits` VALUES ('tense');
INSERT INTO `traits` VALUES ('uncomfortable');
INSERT INTO `traits` VALUES ('unloved');
INSERT INTO `traits` VALUES ('weary');
INSERT INTO `traits` VALUES ('worthless');

DROP TABLE IF EXISTS `aspects_traits`;
CREATE TABLE IF NOT EXISTS `aspects_traits` (
  `aspectId` bigint(20) NOT NULL,
  `TraitId` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
