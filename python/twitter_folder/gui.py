import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor

from sentiment_analysis import sentiment_analysis


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class TableView(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)
        self.horizontalHeader().setStretchLastSection(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def set_data(data_df):
        # function that takes a dataframe of 10 rows and inserts it into the datatable.
        column_names = data_df.columns()
        return


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        main_layout = QVBoxLayout()
        intro_layout = QHBoxLayout()
        account_info_layout = QHBoxLayout()
        table_layout = QVBoxLayout()

        intro_text_label = QLabel(
            "Hello and welcome to this small project that I developed.\n"
            + "This application allows you to insert a Twitter Account name, "
            + "it will then retrieve a larger number of tweets and return you"
            + " the top 10 negative tweets recently tweeted about this account.\nEnjoy!"
        )

        account_name_label = QLabel("Account Name:")
        account_name_input = QLineEdit()

        combobox_sentiment_choice = QComboBox()
        combobox_sentiment_choice.addItem("Positive")
        combobox_sentiment_choice.addItem("Negative")

        button_retrieve_tweets = QPushButton("Retrieve Tweets")

        label_sentiment_choice = QLabel("Choose Tweet Category:")

        tweets_table = TableView()
        tweets_table.setRowCount(10)
        tweets_table.setColumnCount(10)

        intro_layout.addWidget(intro_text_label)
        account_info_layout.addWidget(account_name_label)
        account_info_layout.addWidget(account_name_input)
        account_info_layout.addWidget(label_sentiment_choice)
        account_info_layout.addWidget(combobox_sentiment_choice)
        table_layout.addWidget(tweets_table)

        main_layout.addLayout(intro_layout)
        main_layout.addLayout(account_info_layout)
        main_layout.addLayout(table_layout)
        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)
        self.setBaseSize(1000, 1000)

    def button_clicked(account_name_value, sentiment):
        # function that is being called when a button is pressed. It will retrieve the account_name_value of QEditLine Widget
        # and pass it to retrieve tweets, together with the sentiment.
        #It will then call a function that fills the table with the data.
        return

    def retrieve_tweets(account_name_value, sentiment):
        #this function connects to the back-end and will retrieve the top 10 'sentiment("Positive" or "Negative") tweets.
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
