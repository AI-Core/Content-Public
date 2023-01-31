import preprocessing


class Database:
    def get_data(self):
        # code to get data from database
        print('getting data from database')
        pass

    def insert_data(self, data):
        # code to insert data into database
        print('inserting data into database')
        pass


database = Database()

data = database.get_data()
data = preprocessing.remove_duplicate_data(data)
data = preprocessing.remove_rows_with_missing_data(data)
database.insert_data(data)
