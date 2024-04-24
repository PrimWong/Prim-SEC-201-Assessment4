# Rajasurang Wongkrasaemongkol (Prim)
# Student ID : 1323047

# Define the data record class
import pandas as pd

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
        # Assuming the phone number is a string and stripping any non-numeric characters for uniformity
        numeric_filter = filter(str.isdigit, self.phone)
        numeric_phone = "".join(numeric_filter)
        # Anonymize the phone number, keeping the country code intact
        self.phone = numeric_phone[:len(numeric_phone)-10] + '-000-000' + numeric_phone[-4:-1] + '0'
        self.dob = self.dob[:4]
        self.balance = str(round(int(self.balance.replace(',', '')) / 1000) * 1000)

# Define the dataset
data = [
    [1, 'Prima Thomas', 'prima_t@gmail.com', '+66-855-012-345', '1980-04-20', 'M', '42,000', '2024-04-10 08:30:00', 'Thailand'],
    [2, 'Primrose Evergrow', 'primrosee@cmkl.com', '+1-202-555-0182', '1992-08-15', 'F', '90,325', '2024-04-15 14:45:00', 'USA'],
    [3, 'Agus Salim', 'aguss@prim.com', '+62-21-555-0123', '1985-12-05', 'M', '177,100', '2024-04-18 16:00:00', 'Indonesia'],
    [4, 'Tran Cam Tu', 'tranc@superprim.net', '+84-24-3555-0123', '1990-05-22', 'F', '119,730', '2024-03-30 19:20:00', 'Vietnam'],
    [5, 'Dara Sok', 'darasok@gmail.com', '+855-23-555-0123', '1975-02-15', 'M', '151,040', '2024-04-08 09:50:00', 'Cambodia'],
    [6, 'Shang Lan Chi', 'shanglan@cmkl.com', '+60-3-2117-5000', '1988-09-10', 'F', '68,280', '2024-04-01 12:35:00', 'Malaysia'],
    [7, 'Lwin Moe Aung', 'lwinmoe@prim.com', '+95-1-212-123', '1995-07-30', 'M', '237,300', '2024-04-20 08:15:00', 'Myanmar'],
    [8, 'Joy Gomez', 'joyg@superprim.net', '+63-2-8888-1200', '1983-03-17', 'F', '245,000', '2024-03-25 17:45:00', 'Philippines'],
    [9, 'Kong Xin Cai', 'caikx@gmail.com', '+65-6-555-0123', '1978-01-25', 'M', '116,220', '2024-04-15 11:30:00', 'Singapore'],
    [10, 'Chanthra Saechao', 'chanthras@cmkl.com', '+856-21-250-000', '1993-10-30', 'F', '295,740', '2024-04-17 20:30:00', 'Laos'],
]

# Create DataRecord instances and anonymize them
anonymized_data = []
for row in data:
    record = DataRecord(*row)
    record.anonymize()
    anonymized_data.append(vars(record))

# Now we will convert the anonymized data into a DataFrame to display it
anonymized_df = pd.DataFrame(anonymized_data)

# Display the anonymized DataFrame
anonymized_df

anonymized_df.to_csv('SEC201_Anonymized_Data.csv', index=False)