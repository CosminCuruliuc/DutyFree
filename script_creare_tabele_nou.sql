create table ADRESE
(
    ADRESAID  NUMBER(4)    not null
        constraint ADRESE_PK
            primary key,
    STRADA    VARCHAR2(15) not null,
    ORAS      VARCHAR2(15) not null,
    STAT      VARCHAR2(15),
    TARA      VARCHAR2(15) not null,
    CODPOSTAL VARCHAR2(6)  not null
        constraint CD_UQ
            unique
        check (regexp_like(codpostal, '[0-9]{5,6}'))
)
/

create table ANGAJATI
(
    ANGAJATID     NUMBER(4)    not null
        constraint CLIENTI_PK
            primary key,
    NUME          VARCHAR2(15) not null
        check (regexp_like(Nume, '[A-Za-z]')),
    PRENUME       VARCHAR2(15) not null
        check (regexp_like(Prenume, '^[A-Za-z]')),
    POZITIE       VARCHAR2(15) not null
        constraint CHECK_POZITIE
            check (POZITIE IN ('Junior', 'Mediu', 'Senior', 'Expert')),
    DATAANGAJARII DATE         not null,
    EMAIL         VARCHAR2(30) not null
        constraint ANGAJATI_PK
            unique
        check (regexp_like(email, '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}'))
)
/

create table CLIENTI
(
    CLIENTID     NUMBER(4)    not null
        constraint CLIENTI_PKV1
            primary key,
    NUME         VARCHAR2(15) not null
        check (regexp_like(Nume, '[A-Za-z]')),
    PRENUME      VARCHAR2(15) not null
        check (regexp_like(Prenume, '^[A-Za-z]')),
    EMAIL        VARCHAR2(30) not null
        constraint CLIENTI_PKV2
            unique
        check (regexp_like(email, '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}')),
    NUMARTELEFON VARCHAR2(12) not null
        constraint NUMETELEFON
            unique
        check (REGEXP_LIKE("NUMARTELEFON", '[0-9]{10,11}')),
    ADRESAID     NUMBER(4)    not null
        constraint ADRESE_CLIENTI_FK
            references ADRESE
)
/

create unique index CLIENTI__IDX
    on CLIENTI (ADRESAID)
/

create table COMENZI
(
    COMANDAID   NUMBER(4)    not null
        constraint COMENZI_PK
            primary key,
    DATACOMANDA DATE         not null,
    STATUS      VARCHAR2(15) not null
        constraint CHECK_STATUS
            check (STATUS IN ('In procesare', 'In livrare', 'Finalizata', 'Preluata', 'In asteptare')),
    CLIENTID    NUMBER(4)    not null
        constraint CLIENTI_COMENZI_FK
            references CLIENTI,
    ANGAJATID   NUMBER(4)    not null
        constraint ANGAJATI_COMENZI_FK
            references ANGAJATI
)
/

create table DETALIICOMENZI
(
    CANTITATE NUMBER(4) not null
        check (cantitate BETWEEN 1 AND 100),
    COMANDAID NUMBER(4) not null
        constraint COMENZI_DETALIICOMENZI_FK
            references COMENZI,
    PRODUSID  NUMBER(4) not null
        constraint PRODUSE_DETALIICOMENZI_FK
            references PRODUSE,
    constraint DETALIICOMENZI_PK
        unique (COMANDAID, PRODUSID)
)
/

create table FURNIZORI
(
    FURNIZORID     NUMBER(4)    not null
        constraint FURNIZORI_PK
            primary key,
    NUMECOMPANIE   VARCHAR2(20) not null,
    CONTACTNUME    VARCHAR2(20) not null
        check (regexp_like(ContactNume, '[A-Za-z]')),
    CONTACTPRENUME VARCHAR2(20) not null
        check (regexp_like(ContactPrenume, '[A-Za-z]')),
    CONTACTTELEFON VARCHAR2(20) not null
        check (regexp_like(ContactTelefon, '[0-9]')),
    CONTACTEMAIL   VARCHAR2(25) not null
        constraint CONTACTEMAIL
            unique
        check (regexp_like(ContactEmail, '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}')),
    ADRESAID       NUMBER(4)    not null
        constraint ADRESE_FURNIZORI_FK
            references ADRESE
)
/

create unique index FURNIZORI__IDX
    on FURNIZORI (ADRESAID)
/

create table PRODUSE
(
    PRODUSID   NUMBER(4)    not null
        constraint PRODUSE_PK
            primary key,
    NUME       VARCHAR2(15) not null,
    PRET       NUMBER(5)    not null
        check (pret BETWEEN 0.01 AND 10000),
    STOC       NUMBER(8)    not null
        check (stoc > 0),
    FURNIZORID NUMBER(4)    not null
        constraint FURNIZORI_PRODUSE_FK
            references FURNIZORI
)
/

create trigger PRODUSE_PRODUSID_TRG
    before insert
    on PRODUSE
    for each row
    when (new.produsid IS NULL)
BEGIN
    :new.produsid := produse_produsid_seq.nextval;
END;
/

create trigger FURNIZORI_FURNIZORID_TRG
    before insert
    on FURNIZORI
    for each row
    when (new.furnizorid IS NULL)
BEGIN
    :new.furnizorid := furnizori_furnizorid_seq.nextval;
END;
/

create trigger COMENZI_COMANDAID_TRG
    before insert
    on COMENZI
    for each row
    when (new.comandaid IS NULL)
BEGIN
    :new.comandaid := comenzi_comandaid_seq.nextval;
END;
/

create trigger TRG_DATACOMANDA
    before insert or update
    on COMENZI
    for each row
DECLARE
    DataComanda DATE;
BEGIN
	IF( SYSDATE - :new.DataComanda < 0 )
	THEN
		RAISE_APPLICATION_ERROR( -20001,
		'Data invalida: ' || TO_CHAR(DataComanda, 'DD.MM.YYYY' ) || ('Data introdusa este din viitor !!'));
	END IF;
END;
/

create trigger CLIENTI_CLIENTID_TRG
    before insert
    on CLIENTI
    for each row
    when (new.clientid IS NULL)
BEGIN
    :new.clientid := clienti_clientid_seq.nextval;
END;
/

create trigger ANGAJATI_ANGAJATID_TRG
    before insert
    on ANGAJATI
    for each row
    when (new.angajatid IS NULL)
BEGIN
    :new.angajatid := angajati_angajatid_seq.nextval;
END;
/

create trigger TRG_DATAANGAJARII
    before insert or update
    on ANGAJATI
    for each row
DECLARE
    DataAngajarii DATE;
BEGIN
	IF( SYSDATE - :new.DataAngajarii < 0 )
	THEN
		RAISE_APPLICATION_ERROR( -20001,
		'Data invalida: ' || TO_CHAR(DataAngajarii, 'DD.MM.YYYY' ) || ('Data introdusa este din viitor !!'));
	END IF;
END;
/

create trigger ADRESE_ADRESAID_TRG
    before insert
    on ADRESE
    for each row
    when (new.adresaid IS NULL)
BEGIN
    :new.adresaid := adrese_adresaid_seq.nextval;
END;
/