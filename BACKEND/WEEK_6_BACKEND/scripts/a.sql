create table public.users(
	id integer not null generated always as identity,
	full_name varchar(255) not null,
	username varchar(100) unique not null,
	password varchar(255)  not null,
	primary key(id)
);

create table public.products(
	id integer not null generated always as identity,
	code varchar(50) unique not null,
	name varchar(255) not null,
	stock integer not null,
	price numeric(10,2) not null,
	primary key(id)
);

create table public.invoices(
	id integer not null generated always as identity,
	user_id integer not null references public.users(id),
	total_amount numeric(10,2) not null,
	invoice_date date not null default current_date,
	status varchar(20) not null default 'pending'
        check (status in ('pending', 'canceled', 'delivered','returned')),
	primary key(id)
);

create table public.invoice_products(
	id integer not null generated always as identity,
	invoice_id integer not null references public.invoices(id),
	product_id integer not null references public.products(id),
	quantity integer not null check (quantity > 0),
	price numeric(10,2) not null check (price >= 0),
	delivered boolean not null default false,
	primary key(id),
	unique(invoice_id,product_id)
);


