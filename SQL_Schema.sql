CREATE TABLE finance (
    fraud_bool int,
    income float8,
    name_email_similarity float8,
    prev_address_months_count int,
    current_address_months_count int,
    customer_age int,
    days_since_request float8,
    intended_balcon_amount float8,
    payment_type varchar(255), 
    zip_count_4w int,
    velocity_6h float8,
    velocity_24h float8,
    velocity_4w float8,
    bank_branch_count_8w int,
    date_of_birth_distinct_emails_4w int,
    employment_status varchar(255),
    credit_risk_score int,
    email_is_free int,
    housing_status varchar(255), 
    phone_home_valid int,
    phone_mobile_valid int,
    bank_months_count int,
    has_other_cards int,
    proposed_credit_limit float8,
    foreign_request int,
    source varchar(255), 
    session_length_in_minutes float8,
    device_os varchar(255),
    keep_alive_session int,
    device_distinct_emails_8w int,
    device_fraud_count int,
    month int
);

SELECT *
FROM finance
LIMIT 100;
