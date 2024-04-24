# Rajasurang Wongkrasaemongkol (Prim)
# Student ID : 1323047
# Define the schema of the data record using a class
class DataRecord:
    def __init__(self, id, name, email, phone, dob, gender, balance, last_login, country):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.gender = gender
        self.balance = balance
        self.last_login = last_login
        self.country = country

    def anonymize(self):
        self.name = f"User{str(self.id).zfill(3)}"
        self.email = f"user{str(self.id).zfill(3)}@example.com"
        self.phone = self.phone[:3] + '-000-000' + self.phone[-4:-1] + '0'
        self.dob = self.dob[:4]
        self.balance = str(round(int(self.balance.replace(',', '')) / 1000) * 1000)

# Sample usage
record = DataRecord(1, 'Prima Thomas', 'prima_t@gmail.com', '+66-855-012-345', '1980-04-20', 'M', '42,000', '2024-04-10 08:30:00', 'Thailand')
record.anonymize()
print(vars(record))
