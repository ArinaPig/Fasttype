import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QStackedWidget

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Мое приложение с несколькими страницами')

        self.stackedWidget = QStackedWidget(self)

        # Создаем и добавляем страницы
        page1 = self.createPage('Это страница 1', 'Перейти на страницу 2', 1)
        page2 = self.createPage('Это страница 2', 'Перейти на страницу 1', 0)

        self.stackedWidget.addWidget(page1)
        self.stackedWidget.addWidget(page2)

        # Устанавливаем начальную страницу
        self.stackedWidget.setCurrentIndex(0)

        # Создаем кнопки для переключения страниц
        self.button1 = QPushButton('Перейти на страницу 1', self)
        self.button1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

        self.button2 = QPushButton('Перейти на страницу 2', self)
        self.button2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Размещаем кнопки в макете
        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def createPage(self, text, buttonText, index):
        page = QWidget()
        layout = QVBoxLayout()

        label = QLabel(text, page)

        button = QPushButton(buttonText, page)
        button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(index))

        layout.addWidget(label)
        layout.addWidget(button)

        page.setLayout(layout)

        return page

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
