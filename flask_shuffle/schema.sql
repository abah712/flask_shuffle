drop table if exists terms;
create table terms (
    id   integer primary key autoincrement,
    term varchar(125) not null,
    pronunciation varchar(125) not null,
    response varchar(125) not null,
    url  varchar(200) not null,
    showed integer not null
);