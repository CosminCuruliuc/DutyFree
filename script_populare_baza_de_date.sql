--inserare date in tabela adrese

INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Lombard Street', 'San Francisco', 'California', 'USA', '94111');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Calea Victoriei', 'București', 'București', 'România', '01007');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Gran Vía', 'Madrid', 'Madrid', 'Spania', '28013');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Champs-Élysés', 'Paris', 'Ile-de-France', 'Franța', '75008');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Via Dante', 'Milano', 'Lombardia', 'Italia', '20121');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Oxford Street', 'Londra', 'Londra', 'Regatul Unit', '45655');

INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Drum Industriei', 'Cluj-Napoca', 'Cluj', 'România', '400486');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'De la Industria', 'Valencia', 'Valencia', 'Spania', '46035');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Rue des Usines', 'Lyon', 'Rhône-Alpes', 'Franța', '69003');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Via Industriale', 'Torino', 'Piemonte', 'Italia', '10151');
INSERT INTO Adrese (AdresaID, Strada, Oras, Stat, Tara, CodPostal) VALUES (NULL, 'Industrial Road', 'Birmingham', 'West Midlands', 'Regatul Unit', '10011');

--inserare in tabela clienti

INSERT INTO Clienti (CLIENTID, NUME, PRENUME, EMAIL, NUMARTELEON, ADRESAID) VALUES (NULL, 'Ionescu', 'Andrei', 'andrei.ionescu@mail.com', '+40721234567', (SELECT ADRESAID FROM ADRESE WHERE STRADA = 'Calea Victoriei'));
INSERT INTO Clienti (CLIENTID, NUME, PRENUME, EMAIL, NUMARTELEON, ADRESAID) VALUES (NULL, 'García', 'Elena', 'elena.garcia@mail.es', '+34911234567', (SELECT ADRESAID FROM ADRESE WHERE STRADA = 'Gran Vía'));
INSERT INTO Clienti (CLIENTID, NUME, PRENUME, EMAIL, NUMARTELEON, ADRESAID) VALUES (NULL, 'Dubois', 'Luc', 'luc.dubois@mail.fr', '+33123456789', (SELECT ADRESAID FROM ADRESE WHERE STRADA = 'Champs-Élysés'));
INSERT INTO Clienti (CLIENTID, NUME, PRENUME, EMAIL, NUMARTELEON, ADRESAID) VALUES (NULL, 'Rossi', 'Marco', 'm.rossi@mail.it', '+39212345678', (SELECT ADRESAID FROM ADRESE WHERE STRADA = 'Via Dante'));
INSERT INTO Clienti (CLIENTID, NUME, PRENUME, EMAIL, NUMARTELEON, ADRESAID) VALUES (NULL, 'Smith', 'Emily', 'e.smith@mail.uk', '+44791245678', (SELECT ADRESAID FROM ADRESE WHERE STRADA = 'Oxford Street'));

--inserare in tabela furnizori

INSERT INTO Furnizori (FurnizorID, NumeCompanie, ContactNume, ContactPrenume, ContactTelefon, ContactEmail, AdresaID)
VALUES (NULL, 'Arome Cluj', 'Muresan', 'Laura', '0264123456', 'laura@aromecluj.ro', (SELECT AdresaID FROM Adrese WHERE Strada = 'Drum Industriei' AND Oras = 'Cluj-Napoca'));

INSERT INTO Furnizori (FurnizorID, NumeCompanie, ContactNume, ContactPrenume, ContactTelefon, ContactEmail, AdresaID)
VALUES (NULL, 'Bodegas Val', 'Navarro', 'Alej', '963123456', 'alej@bodegasval.es', (SELECT AdresaID FROM Adrese WHERE Strada = 'De la Industria' AND Oras = 'Valencia'));

INSERT INTO Furnizori (FurnizorID, NumeCompanie, ContactNume, ContactPrenume, ContactTelefon, ContactEmail, AdresaID)
VALUES (NULL, 'Lux Lyon', 'Girard', 'Sophie', '0472123456', 'sophie@luxlyon.fr', (SELECT AdresaID FROM Adrese WHERE Strada = 'Rue des Usines' AND Oras = 'Lyon'));

INSERT INTO Furnizori (FurnizorID, NumeCompanie, ContactNume, ContactPrenume, ContactTelefon, ContactEmail, AdresaID)
VALUES (NULL, 'Gioielli Tor', 'Bianchi', 'Luca', '0111234567', 'luca@gioitor.it', (SELECT AdresaID FROM Adrese WHERE Strada = 'Via Industriale' AND Oras = 'Torino'));

INSERT INTO Furnizori (FurnizorID, NumeCompanie, ContactNume, ContactPrenume, ContactTelefon, ContactEmail, AdresaID)
VALUES (NULL, 'Brit Lux Goods', 'Taylor', 'Emma', '0121123456', 'emma@blgoods.uk', (SELECT AdresaID FROM Adrese WHERE Strada = 'Industrial Road' AND Oras = 'Birmingham'));

-- Inserare tabela Produse

-- Produse pentru Arome Cluj (furnizor de arome și parfumuri)
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Parfum Lav', 50, 100, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Arome Cluj'));
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Esenta Trand', 70, 200, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Arome Cluj'));

-- Produse pentru Bodegas Val (furnizor de băuturi alcoolice)
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Vin Rioja', 30, 150, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Bodegas Val'));
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Whisky Malt', 100, 50, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Bodegas Val'));

-- Produse pentru Lux Lyon (furnizor de produse de lux)
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Ceas', 250, 20, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Lux Lyon'));
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Portofel', 150, 50, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Lux Lyon'));

-- Produse pentru Gioielli Tor (furnizor de bijuterii)
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Inel Aur', 500, 15, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Gioielli Tor'));
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Bratara', 300, 30, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Gioielli Tor'));

-- Produse pentru Brit Lux Goods (furnizor de bunuri de lux)
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Geanta', 200, 40, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Brit Lux Goods'));
INSERT INTO Produse (ProdusID, Nume, Pret, Stoc, FurnizorID) VALUES (NULL, 'Cravata', 80, 100, (SELECT FurnizorID FROM Furnizori WHERE NumeCompanie = 'Brit Lux Goods'));

-- Inserare tabela Angajati

INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Popescu', 'Ion', 'Junior', TO_DATE('2020-01-15', 'YYYY-MM-DD'), 'ion.popescu@email.com');
INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Ionescu', 'Ana', 'Mediu', TO_DATE('2019-08-23', 'YYYY-MM-DD'), 'ana.ionescu@email.com');
INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Mihai', 'Dan', 'Senior', TO_DATE('2021-03-10', 'YYYY-MM-DD'), 'dan.mihai@email.com');
INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Vasile', 'Elena', 'Mediu', TO_DATE('2022-07-01', 'YYYY-MM-DD'), 'elena.vasile@email.com');
INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Dobre', 'Marius', 'Senior', TO_DATE('2018-05-16', 'YYYY-MM-DD'), 'marius.dobre@email.com');
INSERT INTO Angajati (AngajatID, Nume, Prenume, Pozitie, DataAngajarii, Email) VALUES (NULL, 'Nistor', 'Laura', 'Expert', TO_DATE('2017-11-30', 'YYYY-MM-DD'), 'laura.nistor@email.com');

-- Inserare tabela Comenzi

INSERT INTO Comenzi (ComandaID, DataComanda, Status, ClientID, AngajatID)
VALUES (NULL, TO_DATE('2023-06-01', 'YYYY-MM-DD'), 'In procesare',
        (SELECT CLIENTID FROM Clienti WHERE Nume = 'Ionescu' AND PRENUME = 'Andrei'),
        (SELECT AngajatID FROM Angajati WHERE Pozitie = 'Junior' AND ROWNUM = 1));

INSERT INTO Comenzi (ComandaID, DataComanda, Status, ClientID, AngajatID)
VALUES (NULL, TO_DATE('2023-06-02', 'YYYY-MM-DD'), 'Finalizata',
        (SELECT CLIENTID FROM Clienti WHERE Nume = 'García' AND PRENUME = 'Elena'),
        (SELECT AngajatID FROM Angajati WHERE Pozitie = 'Mediu' AND ROWNUM = 1));

INSERT INTO Comenzi (ComandaID, DataComanda, Status, ClientID, AngajatID)
VALUES (NULL, TO_DATE('2023-06-03', 'YYYY-MM-DD'), 'In asteptare',
        (SELECT CLIENTID FROM Clienti WHERE Nume = 'Dubois' AND PRENUME = 'Luc'),
        (SELECT AngajatID FROM Angajati WHERE Pozitie = 'Senior' AND ROWNUM = 1));

INSERT INTO Comenzi (ComandaID, DataComanda, Status, ClientID, AngajatID)
VALUES (NULL, TO_DATE('2023-06-04', 'YYYY-MM-DD'), 'In livrare',
        (SELECT CLIENTID FROM Clienti WHERE Nume = 'Rossi' AND PRENUME = 'Marco'),
        (SELECT AngajatID FROM Angajati WHERE Pozitie = 'Expert' AND ROWNUM = 1));

INSERT INTO Comenzi (ComandaID, DataComanda, Status, ClientID, AngajatID)
VALUES (NULL, TO_DATE('2023-06-05', 'YYYY-MM-DD'), 'Preluata',
        (SELECT CLIENTID FROM Clienti WHERE Nume = 'Smith' AND PRENUME = 'Emily'),
        (SELECT AngajatID FROM Angajati WHERE Pozitie = 'Junior' AND ROWNUM = 1));

-- Inserare tabel DetaliiComenzi

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Ionescu' AND PRENUME = 'Andrei')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Parfum Lav'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(1, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Ionescu' AND PRENUME = 'Andrei')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Vin Rioja'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(3, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'García' AND PRENUME = 'Elena')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Esenta Trand'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'García' AND PRENUME = 'Elena')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Whisky Malt'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(1, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Ionescu' AND PRENUME = 'Andrei')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Ceas'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Dubois' AND PRENUME = 'Luc')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Inel Aur'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(1, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Rossi' AND PRENUME = 'Marco')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Geanta'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(3, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Smith' AND PRENUME = 'Emily')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Parfum Lav'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Dubois' AND PRENUME = 'Luc')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Portofel'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(1, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Rossi' AND PRENUME = 'Marco')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Vin Rioja'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(3, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Smith' AND PRENUME = 'Emily')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Ceas'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'García' AND PRENUME = 'Elena')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Cravata'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(1, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Ionescu' AND PRENUME = 'Andrei')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Bratara'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(3, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Dubois' AND PRENUME = 'Luc')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Whisky Malt'));

INSERT INTO DetaliiComenzi (Cantitate, ComandaID, ProdusID) VALUES
(2, (SELECT ComandaID FROM Comenzi WHERE ClientID = (SELECT CLIENTID FROM Clienti WHERE Nume = 'Rossi' AND PRENUME = 'Marco')),
(SELECT ProdusID FROM Produse WHERE Nume = 'Esenta Trand'));