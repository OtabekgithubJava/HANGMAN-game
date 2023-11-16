import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class HangmanGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Hangman Game")
        self.setGeometry(100, 100, 300, 150)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.info_label = QLabel("Guess the word:")
        self.layout.addWidget(self.info_label)

        self.word_display = QLabel("_ _ _ _ _")  # Placeholder for the word
        self.layout.addWidget(self.word_display)

        self.input_box = QLineEdit()
        self.layout.addWidget(self.input_box)

        self.guess_button = QPushButton("Guess")
        self.guess_button.clicked.connect(self.check_guess)
        self.layout.addWidget(self.guess_button)

        self.central_widget.setLayout(self.layout)

        self.word_to_guess = "PYTHON"  # Change this to set a different word
        self.current_guess = ["_" for _ in self.word_to_guess]
        self.allowed_attempts = 7
        self.remaining_attempts = self.allowed_attempts

    def update_word_display(self):
        displayed_word = " ".join(self.current_guess)
        self.word_display.setText(displayed_word)

    def check_guess(self):
        guessed_letter = self.input_box.text().upper()

        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in self.word_to_guess:
                for idx, letter in enumerate(self.word_to_guess):
                    if letter == guessed_letter:
                        self.current_guess[idx] = guessed_letter
                self.update_word_display()

                if "_" not in self.current_guess:
                    QMessageBox.information(self, "Congratulations!", "You guessed the word!")
                    self.reset_game()
            else:
                self.remaining_attempts -= 1
                if self.remaining_attempts == 0:
                    QMessageBox.information(self, "Game Over", f"The word was {self.word_to_guess}. You lost!")
                    self.reset_game()

            self.input_box.clear()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a single valid letter.")

    def reset_game(self):
        self.word_to_guess = "PYTHON"  # Change this to set a different word
        self.current_guess = ["_" for _ in self.word_to_guess]
        self.allowed_attempts = 7
        self.remaining_attempts = self.allowed_attempts
        self.update_word_display()


def run_game():
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_game()
