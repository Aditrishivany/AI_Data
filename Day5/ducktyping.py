class Pycharm:
    def execute(self):
        print("Compiling+Running")
class VSCode:
    def execute(self):
        print("Running+Linting")
def code(editor):
    editor.execute()
code(Pycharm())
code(VSCode())