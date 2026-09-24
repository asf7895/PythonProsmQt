CREATE TABLE `admin1` (
  `login` varchar(255) NOT NULL,
  `pwd` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `prof` varchar(255) NOT NULL,
  `fullname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `opros1` (
  `r_answer` int NOT NULL,
  `user` varchar(255) NOT NULL,
  `data1` date NOT NULL,
  `num_answer` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
