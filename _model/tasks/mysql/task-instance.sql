CREATE TABLE `task-instance` (
  `guid` char(36) NOT NULL DEFAULT 'UUID()',
  `recurring-task` char(36) DEFAULT NULL,
  `user` char(36) NOT NULL,
  `create-date` datetime DEFAULT NULL,
  `completion-date` datetime DEFAULT NULL,
  PRIMARY KEY (`guid`),
  KEY `FK_user-guid_idx` (`user`),
  CONSTRAINT `FK_task-instance-user_user-guid` FOREIGN KEY (`user`) REFERENCES `user` (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
