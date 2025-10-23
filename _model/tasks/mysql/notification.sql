CREATE TABLE `notification` (
  `guid` char(36) NOT NULL DEFAULT 'UUID()',
  `context` json NOT NULL,
  `create-date` datetime NOT NULL,
  `read-date` datetime DEFAULT NULL,
  PRIMARY KEY (`guid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
