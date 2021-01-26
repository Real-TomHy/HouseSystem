/*
Navicat MySQL Data Transfer

Source Server         : No
Source Server Version : 80019
Source Host           : localhost:3306
Source Database       : manage

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-07-15 10:58:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `RentingHouseInfo`
-- ----------------------------
DROP TABLE IF EXISTS `RentingHouseInfo`;
CREATE TABLE `RentingHouseInfo` (
  `cus_id` varchar(4) NOT NULL,
  `cus_name` varchar(15) NOT NULL,
  `cus_cell` bigint(11) NOT NULL,
  `cus_type` varchar(2) NOT NULL,
  `cus_price` int NOT NULL,
  `hous_type` varchar(4) NOT NULL,
  `hous_area` int NOT NULL,
  `ren_situation` varchar(4) NOT NULL,
  `hous_address` varchar(9) NOT NULL,
  `hous_situation` varchar(3) NOT NULL,
  PRIMARY KEY (`cus_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of RentingHouseInfo
-- ----------------------------
INSERT INTO `RentingHouseInfo` VALUES ('1001', '小张', 13623122890, '楼房',600,'三室一厅',345,'中档装修','阳光小区3单元10','已出租');
INSERT INTO `RentingHouseInfo` VALUES ('1002', '小李', 13723122890, '平房',400,'两室一厅',234,'简单装修','阳光小区5单元1','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1003', '老王', 13823122890, '平房',1000,'独门独院',675,'高档装修','阳光小区4单元5','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1004', '老赵', 13923122890, '楼房',800,'独门独院',700,'简单装修','阳光小区1单元5','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1005', '小刘', 18623122890, '其他',300,'其他',100,'无装修','阳光小区2单元5','已出租');
INSERT INTO `RentingHouseInfo` VALUES ('1006', '小郭', 18723122890, '楼房',150,'单间',40,'无装修','阳光小区5单元9','已出租');
INSERT INTO `RentingHouseInfo` VALUES ('1007', '老李', 18823122890, '平房',300,'一室一厅',236,'简单装修','阳光小区5单元10','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1008', '老张', 13423122890, '平房',2500,'独门独院',1000,'高档装修','阳光小区7单元10','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1009', '老刘', 13523122890, '其他',200,'其他',60,'简单装修','阳光小区4单元10','未出租');
INSERT INTO `RentingHouseInfo` VALUES ('1010', '小曹', 13323122890, '楼房',500,'两室一厅',366,'简单装修','阳光小区1单元10','未出租');


-- ----------------------------
-- Table structure for `stu_user`
-- ----------------------------
DROP TABLE IF EXISTS `hous_user`;
CREATE TABLE `hous_user` (
  `user_account` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`user_account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stu_user
-- ----------------------------
INSERT INTO `hous_user` VALUES ('1234', '1234');
INSERT INTO `hous_user` VALUES ('12345', '12345');
INSERT INTO `hous_user` VALUES ('12345678', '12345678');

DROP TABLE IF EXISTS `SellHouseInfo`;
CREATE TABLE `SellHouseInfo` (
  `cell_id` varchar(4) NOT NULL,
  `cell_name` varchar(15) NOT NULL,
  `cell_cell` bigint(11) NOT NULL,
  `cell_type` varchar(2) NOT NULL,
  `cell_price` int NOT NULL,
  `hous_type` varchar(10) NOT NULL,
  `hous_area` int NOT NULL,
  `ren_situation` varchar(10) NOT NULL,
  `hous_address` varchar(10) NOT NULL,
  `hous_situation` varchar(10) NOT NULL,
  PRIMARY KEY (`cell_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of SellHouseInfo
-- ----------------------------
INSERT INTO `SellHouseInfo` VALUES ('2001', '小张', 13623122678, '楼房',60,'两室一厅',414,'中档装修','阳光家园3单元10','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2002', '小李', 13609877890, '平房',40,'两室一厅',134,'简单装修','阳光家园5单元1','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2003', '老王', 15952553400, '平房',100,'独门独院',414,'高档装修','阳光家园4单元5','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2004', '老张', 15863445457, '楼房',80,'独门独院',511,'无装修','阳光家园1单元5','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2005', '老赵', 13465456345, '其他',30,'一室一厅',112,'简单装修','阳光家园2单元5','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2006', '老李', 13265235653, '楼房',50,'三室一厅',341,'中档装修','阳光家园5单元9','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2007', '张三', 13409098978, '平房',79,'两室一厅',121,'高装修','阳光家园5单元10','未出售');
INSERT INTO `SellHouseInfo` VALUES ('2008', '李四', 15668988678, '平房',40,'独门独院',312,'无装修','阳光家园7单元10','已出售');
INSERT INTO `SellHouseInfo` VALUES ('2000', '小赵', 13623122678, '楼房',60,'三室一厅',134,'简单装修','阳光家园5单元10','已出售');

DROP TABLE IF EXISTS `PurchasePeopleInfo`;
CREATE TABLE `PurchasePeopleInfo` (
  `cusPeo_id` varchar(4) NOT NULL,
  `cusPeo_name` varchar(15) NOT NULL,
  `cusPeo_cell` bigint(11) NOT NULL,
  `cusPeo_type` varchar(2) NOT NULL,
  `housPeo_type` varchar(4) NOT NULL,
  `housPeo_area` int NOT NULL,
  `renPeo_situation` varchar(4) NOT NULL,
  PRIMARY KEY (`cusPeo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of PurchasePeopleInfo
-- ----------------------------
INSERT INTO `PurchasePeopleInfo` VALUES ('3001', '老赵', 13411313133, '平房','独门独院',140,'中档装修');
INSERT INTO `PurchasePeopleInfo` VALUES ('3002', '老李', 13623122920, '平房','独门独院',150,'简单装修');
INSERT INTO `PurchasePeopleInfo` VALUES ('3003', '老刘', 13443244131, '楼房','两室一厅',120,'高档装修');
INSERT INTO `PurchasePeopleInfo` VALUES ('3004', '小赵', 13545132423, '楼房','独门独院',120,'高档装修');
INSERT INTO `PurchasePeopleInfo` VALUES ('3005', '小李', 15714232313, '楼房','三室一厅',150,'中档装修');
INSERT INTO `PurchasePeopleInfo` VALUES ('3006', '小刘', 15812343212, '平房','独门独院',158,'高档装修');

DROP TABLE IF EXISTS `RentingPeopleInfo`;
CREATE TABLE `RentingPeopleInfo` (
  `cusPeo_id` varchar(4) NOT NULL,
  `cusPeo_name` varchar(15) NOT NULL,
  `cusPeo_cell` bigint(11) NOT NULL,
  `cusPeo_type` varchar(2) NOT NULL,
  `housPeo_type` varchar(4) NOT NULL,
  `housPeo_area` int NOT NULL,
  `renPeo_situation` varchar(4) NOT NULL,
  PRIMARY KEY (`cusPeo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of RentingHouseInfo
-- ----------------------------
INSERT INTO `RentingPeopleInfo` VALUES ('4001', '老李', 13623122820, '平房','独门独院',500,'简单装修');
INSERT INTO `RentingPeopleInfo` VALUES ('4002', '老刘', 13635677890, '楼房','两室一厅',600,'简单装修');
INSERT INTO `RentingPeopleInfo` VALUES ('4003', '老找', 13511343123, '楼房','三室一厅',400,'高档装修');
INSERT INTO `RentingPeopleInfo` VALUES ('4004', '小李', 13513241321, '平房','独门独院',450,'高档装修');
INSERT INTO `RentingPeopleInfo` VALUES ('4005', '小刘', 15713231221, '平他','独门独院',900,'中档装修');




