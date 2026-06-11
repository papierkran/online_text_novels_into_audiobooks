/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 90100
 Source Host           : localhost:3306
 Source Schema         : audio_novels

 Target Server Type    : MySQL
 Target Server Version : 90100
 File Encoding         : 65001

 Date: 23/10/2024 22:27:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for novels_info
-- ----------------------------
DROP TABLE IF EXISTS `novels_info`;
CREATE TABLE `novels_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `file_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `cover_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of novels_info
-- ----------------------------
INSERT INTO `novels_info` VALUES (1, '重生之我在长职写代码', 'www.114514.com', '无555555555555555555555555555555', '123456', 'www.baidu.com');
INSERT INTO `novels_info` VALUES (2, '关于我在长职遇到代码这档事', 'www.1433223', '无', NULL, NULL);
INSERT INTO `novels_info` VALUES (3, '震惊！我的作业竟然在开学前一天自己写好了', 'www.aomenfengyun.com', '还是无', NULL, NULL);
INSERT INTO `novels_info` VALUES (4, 'jdiafjd', 'dfasfd', 'daffdadsf', 'dfafads', 'dffd');
INSERT INTO `novels_info` VALUES (5, '2111', 'uiui', 'adsfasdfsazsdfx', 'zsfdasfa', 'fhdfgh');

-- ----------------------------
-- Table structure for reading_history
-- ----------------------------
DROP TABLE IF EXISTS `reading_history`;
CREATE TABLE `reading_history`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `novel_id` int NOT NULL,
  `read_time` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `read_content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_user`(`user_id` ASC) USING BTREE,
  INDEX `fk_novel`(`novel_id` ASC) USING BTREE,
  CONSTRAINT `fk_novel` FOREIGN KEY (`novel_id`) REFERENCES `novels_info` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `fk_user` FOREIGN KEY (`user_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of reading_history
-- ----------------------------
INSERT INTO `reading_history` VALUES (1, 1, 1, '2024-10-23 12:26:01', '无555555555555555555555555555555');
INSERT INTO `reading_history` VALUES (2, 1, 2, '2024-10-23 12:26:12', '无');
INSERT INTO `reading_history` VALUES (3, 1, 1, '2024-10-23 12:26:31', '无555555555555555555555555555555');
INSERT INTO `reading_history` VALUES (4, 1, 1, '2024-10-23 14:25:36', '无555555555555555555555555555555');
INSERT INTO `reading_history` VALUES (5, 1, 4, '2024-10-23 14:27:14', 'daffdadsf');

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES (1, 'laonai', 'scrypt:32768:8:1$4epUFazcMhcDxTus$c3ff82383be0aaa108a97ebbd53eba600ff9f5500b2ec00ff7cfebc354a698d0b295b9b8bd71cf3f03015ba92a199ba4dc27786a5be4979a182cb589217fb6ae');
INSERT INTO `user_info` VALUES (2, 'root', '123456');

SET FOREIGN_KEY_CHECKS = 1;
