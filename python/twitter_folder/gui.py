import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from sentiment_analysis import sentiment_analysis
from tweepy_operations import tweepy_operations
from general_operations import general_operations


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(self._data.iloc[index.row()][index.column()]))
        return QtCore.QVariant()


class MainWindow(QMainWindow):

    global tweepy_client

    def __init__(self):

        self.connection_tokens, self.tweepy_client = tweepy_operations.get_tweepy_client()

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
            + " the top 10 positive/negative tweets recently tweeted about this account.\nEnjoy!"
        )

        self.account_name_label = QLabel("Account Name:")
        self.account_name_input = QLineEdit()

        self.combobox_sentiment_choice = QComboBox()
        self.combobox_sentiment_choice.addItem("Positive")
        self.combobox_sentiment_choice.addItem("Negative")

        self.button_retrieve_tweets = QPushButton("Retrieve Tweets")
        self.button_retrieve_tweets.setStyleSheet("background-color: #0384fc; color: #ffffff")
        self.button_retrieve_tweets.clicked.connect(lambda: self.button_clicked(self.account_name_input.text(), self.combobox_sentiment_choice.currentText()))

        self.label_sentiment_choice = QLabel("Choose Tweet Category:")

        self.tweets_table_view = QTableView()

        intro_layout.addWidget(intro_text_label)
        account_info_layout.addWidget(self.account_name_label)
        account_info_layout.addWidget(self.account_name_input)
        account_info_layout.addWidget(self.label_sentiment_choice)
        account_info_layout.addWidget(self.combobox_sentiment_choice)
        account_info_layout.addWidget(self.button_retrieve_tweets)
        table_layout.addWidget(self.tweets_table_view)

        main_layout.addLayout(intro_layout)
        main_layout.addLayout(account_info_layout)
        main_layout.addLayout(table_layout)
        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)
        self.setBaseSize(1000, 1000)

    def button_clicked(self, account_name_value, sentiment):
        # function that is being called when a button is pressed. It will retrieve the account_name_value of QEditLine Widget
        # and pass it to retrieve tweets, together with the sentiment.
        # It will then call a function that fills the table with the data.
        top_10_sentiment_tweets_df = self.retrieve_tweets(account_name_value, sentiment)
        self.create_dataModel_and_fill_view(top_10_sentiment_tweets_df)
        return

    def retrieve_tweets(self, account_name_value, sentiment):
        # this function connects to the back-end and will retrieve the top 10 'sentiment("Positive" or "Negative") tweets.
        account_id = general_operations.get_account_id_by_account_name(account_name_value, self.connection_tokens["BEARER_TOKEN"])
        tweets = tweepy_operations.get_number_of_tweets_mentioning_account_id(self.tweepy_client, account_id, 500)
        tweets_df = general_operations.convert_tweet_objects_to_dataframe(tweets)
        tweets_english_df = tweets_df[tweets_df["language"] == "en"]
        tweets_sentiment_analysis_df = sentiment_analysis.add_sentiment_analysis(sentiment_analysis, tweets_english_df)
        top_10_sentiment_tweets_df = general_operations.retrieve_top_10_tweets_negative_or_positive(tweets_sentiment_analysis_df, sentiment)
        return top_10_sentiment_tweets_df

    def create_dataModel_and_fill_view(self, data):
        self.model = PandasModel(data)
        self.tweets_table_view.setModel(self.model)
        self.tweets_table_view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
