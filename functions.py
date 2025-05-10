from PyQt6.QtWidgets import *
import csv
from book import *

class Functions(QMainWindow, Ui_Recipe_Book):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Group_Add.hide()
        self.Group_Search.hide()
        self.Combo_Beef.hide()
        self.Combo_Fish.hide()
        self.Combo_Pork.hide()
        self.Combo_Tofu.hide()
        self.Combo_Chicken.hide()
        self.Group_Success.hide()
        self.Button_Search.clicked.connect(lambda : self.open_search())
        self.Button_Add.clicked.connect(lambda : self.open_add())
        self.Button_Select.clicked.connect(lambda : self.open_show())
        self.Button_Submit.clicked.connect(lambda : self.add_recipe())
        self.Button_Show_B.clicked.connect(lambda : self.show_beef())
        self.Button_Show_C.clicked.connect(lambda : self.show_chicken())
        self.Button_Show_F.clicked.connect(lambda : self.show_fish())
        self.Button_Show_P.clicked.connect(lambda : self.show_pork())
        self.Button_Show_T.clicked.connect(lambda : self.show_tofu())
        self.Button_Back.clicked.connect(lambda : self.backspace())

    def open_search(self):
        """
        Method to open the "Search" box
        :return:
        """
        self.Group_Search.show()
        self.Group_Add.hide()

    def open_add(self):
        """
        Method to open the "Add" box
        :return:
        """
        self.Group_Add.show()
        self.Group_Search.hide()

    def open_show(self):
        """
        Method to open the "Show" box
        :return:
        """
        if self.Button_Show_P.isChecked():
            recipe = self.Combo_Pork.currentText()
        elif self.Button_Show_T.isChecked():
            recipe = self.Combo_Tofu.currentText()
        elif self.Button_Show_F.isChecked():
            recipe = self.Combo_Fish.currentText()
        elif self.Button_Show_B.isChecked():
            recipe = self.Combo_Beef.currentText()
        else:
            recipe = self.Combo_Chicken.currentText()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if recipe == line[1]:
                    self.Text_Recipe.setText(line[2])

    def add_recipe(self):
        """
        Method to add recipe to csv file.
        :return:
        """
        with open('my_recipes.csv', 'a', newline="") as recipe_output:
            content = csv.writer(recipe_output)
            if self.Button_Chicken.isChecked():
                content.writerow(['Chicken', self.Input_Recipe_Name.text(), self.Input_Recipe_Text.toPlainText()])
            elif self.Button_Beef.isChecked():
                content.writerow(['Beef', self.Input_Recipe_Name.text(), self.Input_Recipe_Text.toPlainText()])
            elif self.Button_Pork.isChecked():
                content.writerow(['Pork', self.Input_Recipe_Name.text(), self.Input_Recipe_Text.toPlainText()])
            elif self.Button_Tofu.isChecked():
                content.writerow(['Tofu', self.Input_Recipe_Name.text(), self.Input_Recipe_Text.toPlainText()])
            elif self.Button_Fish.isChecked():
                content.writerow(['Fish', self.Input_Recipe_Name.text(), self.Input_Recipe_Text.toPlainText()])
        self.Group_Add.hide()
        self.Group_Success.show()

    def show_tofu(self):
        """
        Method to display combo box for tofu options.
        :return:
        """
        self.Combo_Tofu.show()
        self.Combo_Beef.hide()
        self.Combo_Fish.hide()
        self.Combo_Pork.hide()
        self.Combo_Chicken.hide()
        self.Button_Show_P.hide()
        self.Button_Show_F.hide()
        self.Button_Show_C.hide()
        self.Button_Show_B.hide()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if line[0] == 'Tofu':
                    self.Combo_Tofu.addItem(line[1])

    def show_fish(self):
        """
        Method to display combo box for fish options.
        :return:
        """
        self.Combo_Fish.show()
        self.Combo_Beef.hide()
        self.Combo_Pork.hide()
        self.Combo_Tofu.hide()
        self.Combo_Chicken.hide()
        self.Button_Show_T.hide()
        self.Button_Show_P.hide()
        self.Button_Show_C.hide()
        self.Button_Show_B.hide()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if line[0] == 'Fish':
                    self.Combo_Fish.addItem(line[1])

    def show_beef(self):
        """
        Method to display combo box for beef options.
        :return:
        """
        self.Combo_Beef.show()
        self.Combo_Fish.hide()
        self.Combo_Pork.hide()
        self.Combo_Tofu.hide()
        self.Combo_Chicken.hide()
        self.Button_Show_T.hide()
        self.Button_Show_P.hide()
        self.Button_Show_F.hide()
        self.Button_Show_C.hide()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if line[0] == 'Beef':
                    self.Combo_Beef.addItem(line[1])

    def show_chicken(self):
        """
        Method to display combo box for chicken options.
        :return:
        """
        self.Combo_Chicken.show()
        self.Combo_Beef.hide()
        self.Combo_Fish.hide()
        self.Combo_Pork.hide()
        self.Combo_Tofu.hide()
        self.Button_Show_T.hide()
        self.Button_Show_P.hide()
        self.Button_Show_F.hide()
        self.Button_Show_B.hide()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if line[0] == 'Chicken':
                    self.Combo_Chicken.addItem(line[1])

    def show_pork(self):
        """
        Method to display combo box for pork options.
        :return:
        """
        self.Combo_Pork.show()
        self.Combo_Beef.hide()
        self.Combo_Fish.hide()
        self.Combo_Tofu.hide()
        self.Combo_Chicken.hide()
        self.Button_Show_T.hide()
        self.Button_Show_F.hide()
        self.Button_Show_C.hide()
        self.Button_Show_B.hide()
        with open('my_recipes.csv', 'r') as recipe_book:
            content = csv.reader(recipe_book)
            for line in content:
                if line[0] == 'Pork':
                    self.Combo_Pork.addItem(line[1])

    def backspace(self):
        """
        Method to clear Text_Recipe and let user reselect protein.
        :return:
        """
        self.Combo_Chicken.hide()
        self.Combo_Chicken.clear()
        self.Combo_Beef.hide()
        self.Combo_Beef.clear()
        self.Combo_Tofu.hide()
        self.Combo_Tofu.clear()
        self.Combo_Fish.hide()
        self.Combo_Fish.clear()
        self.Combo_Pork.hide()
        self.Combo_Pork.clear()
        self.Button_Show_T.show()
        self.Button_Show_F.show()
        self.Button_Show_C.show()
        self.Button_Show_B.show()
        self.Button_Show_P.show()
        self.Text_Recipe.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Functions()
    sys.exit(app.exec())