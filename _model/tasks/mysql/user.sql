CREATE TABLE `user` (
  `guid` char(36) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`guid`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
