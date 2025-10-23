CREATE TABLE `recurring-task` (
  `guid` char(36) NOT NULL DEFAULT 'UUID()',
  `title` varchar(45) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `frequency` json DEFAULT NULL,
  `context` json DEFAULT NULL,
  `user` char(36) NOT NULL,
  PRIMARY KEY (`guid`),
  KEY `FK_user-guid_idx` (`user`),
  CONSTRAINT `FK_user_user-guid` FOREIGN KEY (`user`) REFERENCES `user` (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
