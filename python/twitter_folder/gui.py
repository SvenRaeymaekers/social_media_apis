from distutils.command.build import build
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import tweepy_api_twitter_program


def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 400, 300)
    window.setWindowTitle("My Simple GUI")

    layout = QVBoxLayout()

    label = QLabel("Press the button below.")
    button = QPushButton("Press me.")
    textbox_account_name = QTextEdit()
    textbox_number_of_tweets = QTextEdit()

    button.clicked.connect(lambda: on_clicked(textbox_account_name.toPlainText(), int(textbox_number_of_tweets.toPlainText()) ))

    layout.addWidget(label)
    layout.addWidget(textbox_account_name)
    layout.addWidget(textbox_number_of_tweets)
    layout.addWidget(button)

    window.setLayout(layout)

    window.show()
    app.exec()


def on_clicked(account_name, number_of_tweets):
    tweepy_api_twitter_program.main(account_name, number_of_tweets)

    message = QMessageBox()
    message.setText("done.")
    message.exec_()


if __name__ == "__main__":
    main()
