CREATE TABLE `schueler` (
  `id` integer PRIMARY KEY,
  `vorname` varchar(255),
  `nachname` varchar(255),
  `geburtsjahr` integer,
  `unterscheider` varchar(255),
  `geschlecht` ENUM ('m', 'w', 'd'),
  `anwesenheit` boolean,
  `riegen_id` integer
);

CREATE TABLE `riegen` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `disziplinen` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `a` float,
  `c` float,
  `geschlecht` ENUM ('m', 'w', 'd'),
  `formel` integer,
  `d` integer,
  `bedingungen` varchar(255)
);

CREATE TABLE `ergebnisse` (
  `id` integer PRIMARY KEY,
  `disziplin` integer,
  `wert` integer,
  `punkte` integer,
  `schueler_id` integer
);

ALTER TABLE `riegen` ADD FOREIGN KEY (`id`) REFERENCES `schueler` (`riegen_id`);

ALTER TABLE `disziplinen` ADD FOREIGN KEY (`id`) REFERENCES `ergebnisse` (`disziplin`);

ALTER TABLE `schueler` ADD FOREIGN KEY (`id`) REFERENCES `ergebnisse` (`schueler_id`);
