/*
 Navicat Premium Data Transfer

 Source Server         : nuocheng
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : sale

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 09/03/2022 21:00:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 48 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add product', 7, 'add_product');
INSERT INTO `auth_permission` VALUES (26, 'Can change product', 7, 'change_product');
INSERT INTO `auth_permission` VALUES (27, 'Can delete product', 7, 'delete_product');
INSERT INTO `auth_permission` VALUES (28, 'Can view product', 7, 'view_product');
INSERT INTO `auth_permission` VALUES (29, 'Can add user_info', 8, 'add_user_info');
INSERT INTO `auth_permission` VALUES (30, 'Can change user_info', 8, 'change_user_info');
INSERT INTO `auth_permission` VALUES (31, 'Can delete user_info', 8, 'delete_user_info');
INSERT INTO `auth_permission` VALUES (32, 'Can view user_info', 8, 'view_user_info');
INSERT INTO `auth_permission` VALUES (33, 'Can add score', 9, 'add_score');
INSERT INTO `auth_permission` VALUES (34, 'Can change score', 9, 'change_score');
INSERT INTO `auth_permission` VALUES (35, 'Can delete score', 9, 'delete_score');
INSERT INTO `auth_permission` VALUES (36, 'Can view score', 9, 'view_score');
INSERT INTO `auth_permission` VALUES (37, 'Can add cart', 10, 'add_cart');
INSERT INTO `auth_permission` VALUES (38, 'Can change cart', 10, 'change_cart');
INSERT INTO `auth_permission` VALUES (39, 'Can delete cart', 10, 'delete_cart');
INSERT INTO `auth_permission` VALUES (40, 'Can view cart', 10, 'view_cart');
INSERT INTO `auth_permission` VALUES (41, 'Can add paymentInfo', 11, 'add_payment');
INSERT INTO `auth_permission` VALUES (42, 'Can change paymentInfo', 11, 'change_payment');
INSERT INTO `auth_permission` VALUES (43, 'Can delete paymentInfo', 11, 'delete_payment');
INSERT INTO `auth_permission` VALUES (44, 'Can view paymentInfo', 11, 'view_payment');
INSERT INTO `auth_permission` VALUES (45, 'Can add credit_card', 12, 'add_credit_card');
INSERT INTO `auth_permission` VALUES (46, 'Can change credit_card', 12, 'change_credit_card');
INSERT INTO `auth_permission` VALUES (47, 'Can delete credit_card', 12, 'delete_credit_card');
INSERT INTO `auth_permission` VALUES (48, 'Can view credit_card', 12, 'view_credit_card');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cart
-- ----------------------------
DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `flag` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cart_product_id_id_ad4479a7_fk_product_id`(`product_id_id`) USING BTREE,
  INDEX `cart_user_id_id_aeb465f1_fk_user_info_id`(`user_id_id`) USING BTREE,
  CONSTRAINT `cart_product_id_id_ad4479a7_fk_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `cart_user_id_id_aeb465f1_fk_user_info_id` FOREIGN KEY (`user_id_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cart
-- ----------------------------
INSERT INTO `cart` VALUES (34, 7, 1, 22, 15);
INSERT INTO `cart` VALUES (38, 4, 1, 22, 15);
INSERT INTO `cart` VALUES (56, 3, 0, 21, 15);
INSERT INTO `cart` VALUES (57, 1, 0, 22, 15);
INSERT INTO `cart` VALUES (59, 1, 0, 22, 15);
INSERT INTO `cart` VALUES (61, 1, 0, 22, 15);
INSERT INTO `cart` VALUES (62, 1, 0, 21, 15);
INSERT INTO `cart` VALUES (63, 1, 0, 22, 15);
INSERT INTO `cart` VALUES (64, 1, 0, 21, 15);

-- ----------------------------
-- Table structure for credit_card
-- ----------------------------
DROP TABLE IF EXISTS `credit_card`;
CREATE TABLE `credit_card`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `card_num` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_card_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `credit_card_user_card_id_cc373fdf_fk_user_info_id`(`user_card_id`) USING BTREE,
  CONSTRAINT `credit_card_user_card_id_cc373fdf_fk_user_info_id` FOREIGN KEY (`user_card_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of credit_card
-- ----------------------------
INSERT INTO `credit_card` VALUES (1, 'nuocheng1', '12345678901', '2022-02-03 00:00:00.000000', 15);

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (10, 'backstage', 'cart');
INSERT INTO `django_content_type` VALUES (12, 'backstage', 'credit_card');
INSERT INTO `django_content_type` VALUES (7, 'backstage', 'product');
INSERT INTO `django_content_type` VALUES (9, 'backstage', 'score');
INSERT INTO `django_content_type` VALUES (8, 'backstage', 'user_info');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'payment', 'payment');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-12-22 14:43:32.331008');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-12-22 14:43:32.432736');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-12-22 14:43:32.627285');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-12-22 14:43:32.672165');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-22 14:43:32.679113');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-12-22 14:43:32.728985');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2021-12-22 14:43:32.757903');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2021-12-22 14:43:32.793806');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2021-12-22 14:43:32.801788');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2021-12-22 14:43:32.834705');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2021-12-22 14:43:32.837690');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2021-12-22 14:43:32.844671');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2021-12-22 14:43:32.877615');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2021-12-22 14:43:32.913487');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2021-12-22 14:43:32.943406');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2021-12-22 14:43:32.951387');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2021-12-22 14:43:32.987323');
INSERT INTO `django_migrations` VALUES (18, 'backstage', '0001_initial', '2021-12-22 14:43:33.030175');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2021-12-22 14:43:33.085029');
INSERT INTO `django_migrations` VALUES (20, 'backstage', '0002_remove_user_info_money', '2021-12-23 04:19:38.255959');
INSERT INTO `django_migrations` VALUES (21, 'backstage', '0003_product_user', '2021-12-23 13:54:20.118719');
INSERT INTO `django_migrations` VALUES (22, 'backstage', '0004_auto_20220207_1017', '2022-02-07 10:17:58.817472');
INSERT INTO `django_migrations` VALUES (23, 'backstage', '0005_user_info_position', '2022-02-07 15:56:20.008008');
INSERT INTO `django_migrations` VALUES (24, 'payment', '0001_initial', '2022-02-08 16:33:27.944133');
INSERT INTO `django_migrations` VALUES (25, 'backstage', '0006_auto_20220308_1427', '2022-03-08 14:27:19.020175');
INSERT INTO `django_migrations` VALUES (26, 'payment', '0002_auto_20220308_1427', '2022-03-08 14:27:19.091983');
INSERT INTO `django_migrations` VALUES (27, 'backstage', '0007_auto_20220309_2049', '2022-03-09 20:49:10.620179');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('en3579rsshb7cms718e0kvjv4x0rxfy5', 'eyJ1c2VybmFtZSI6IjEiLCJ1c2VyaWQiOjE1LCJmbGFnIjowfQ:1nRrvh:c3gidBnJchRUnAzSZFJiOWWlKlIt3de-4Jfm9vn22eA', '2022-03-23 16:44:21.745972');
INSERT INTO `django_session` VALUES ('fy4plsed8x6smf96fd5xf5uij54xfyjg', 'eyJ1c2VybmFtZSI6IjExMTEiLCJ1c2VyaWQiOjEzLCJmbGFnIjowfQ:1nGe6E:4guT3M1xmfyojaBbzEIRNxGfVPsBz8y5p69ARPnMlsI', '2022-02-20 17:44:50.434229');
INSERT INTO `django_session` VALUES ('ge1kgb3y6bdhucqx4yuebs1jy0sa8bl8', 'eyJ1c2VybmFtZSI6IjExIiwidXNlcmlkIjo3LCJmbGFnIjowfQ:1n2yyp:yS3yaN0jS89MbNZIFj2YURKXh3tjMIx41j3NcSW3wbM', '2022-01-14 01:12:43.312339');
INSERT INTO `django_session` VALUES ('p2g8zi7nwzy8obmemfzjxddnopgxe172', 'eyJ1c2VybmFtZSI6IjEiLCJ1c2VyaWQiOjE1LCJmbGFnIjowfQ:1nNnxE:tgDlaqkNI1nY-uwmjJr7__MRgeSCV5a95tL6NsF7nVs', '2022-03-12 11:41:08.811976');
INSERT INTO `django_session` VALUES ('q56d2b9hw5wdgdjlnmyl47la92ccu78b', 'eyJ1c2VybmFtZSI6Im5AMTYzLmNvbSIsInVzZXJpZCI6MSwiZmxhZyI6MX0:1nASnG:vswlHItMO_nBf17loEIT2AiW3ru5wrh3V66mlqSS9gg', '2022-02-03 16:27:42.479349');
INSERT INTO `django_session` VALUES ('smvxiaif10or6dgicj6dhrazcyj3xbf3', 'eyJ1c2VybmFtZSI6IjEiLCJ1c2VyaWQiOjE1LCJmbGFnIjowfQ:1nNclz:Uvwnrks8fKhPZRg83T-NsJic8aqFWT6Dp96iCE3PvyM', '2022-03-11 23:44:47.025049');
INSERT INTO `django_session` VALUES ('xqw0aqc72kcqrop1l9rgz7bvexjx44e9', 'eyJ1c2VybmFtZSI6IjExMTEiLCJ1c2VyaWQiOjEzLCJmbGFnIjowfQ:1nHjYH:xpeGYib6YDVBi3ohdfTkwFEnTSu9yglbUBLOtLU5vt8', '2022-02-23 17:46:17.781519');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(225) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `desc` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `create_at` datetime(6) NOT NULL,
  `change_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product_user_id_091f6d86_fk_user_info_id`(`user_id`) USING BTREE,
  CONSTRAINT `product_user_id_091f6d86_fk_user_info_id` FOREIGN KEY (`user_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (21, 'Potato', 'PotatoPotatoPotatoPotatoPotato', 'upload/20220208/3.jpg', '2022-02-25 23:43:03.093838', '2022-02-25 23:43:03.093838', 1, 3.6);
INSERT INTO `product` VALUES (22, 'tomato', 'tomatotomatotomatotomatotomato', 'upload/20220208/7.jpg', '2022-02-25 23:43:23.232020', '2022-02-25 23:43:23.232020', 1, 1.3);

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `score_product_id_id_d00e121e_fk_product_id`(`product_id_id`) USING BTREE,
  INDEX `score_user_id_id_5f1ab22c_fk_user_info_id`(`user_id_id`) USING BTREE,
  CONSTRAINT `score_product_id_id_d00e121e_fk_product_id` FOREIGN KEY (`product_id_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `score_user_id_id_5f1ab22c_fk_user_info_id` FOREIGN KEY (`user_id_id`) REFERENCES `user_info` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of score
-- ----------------------------
INSERT INTO `score` VALUES (30, 6, 22, 15);
INSERT INTO `score` VALUES (31, 9, 21, 15);

-- ----------------------------
-- Table structure for tb_payment
-- ----------------------------
DROP TABLE IF EXISTS `tb_payment`;
CREATE TABLE `tb_payment`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trade_id` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `trade_id`(`trade_id`) USING BTREE,
  INDEX `tb_payment_order_id_e3bfc510_fk_cart_id`(`order_id`) USING BTREE,
  CONSTRAINT `tb_payment_order_id_e3bfc510_fk_cart_id` FOREIGN KEY (`order_id`) REFERENCES `cart` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phonenum` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `superuser` int(11) NOT NULL,
  `position` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  UNIQUE INDEX `phonenum`(`phonenum`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES (1, 'n@163.com', '1', '1642342180@qq.com', '17853317000', 1, 'empty');
INSERT INTO `user_info` VALUES (15, '1', '1', '12345@163.com', '17854469855', 0, '广东省深圳市');

SET FOREIGN_KEY_CHECKS = 1;
