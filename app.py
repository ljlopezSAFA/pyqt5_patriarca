# from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
# from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi
from metodos_bbdd import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('diseño.ui', self)

        # CONECTAR BOTONES CON PAGINAS
        self.Buscar.clicked.connect(self.cargar_datos_tabla)
        self.Crear.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Creacion))
        # self.Editar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Edicion))
        # self.Eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Eliminacion))
        self.guardar.clicked.connect(self.crear_nuevo)

    #CARGAR DATOS
    def cargar_datos_tabla(self):
        self.stackedWidget.setCurrentWidget(self.Busqueda)
        mantecados,columnas = extraer_datos()
        self.tableWidget.setRowCount(len(mantecados))
        # Agregar datos a la tabla
        for fila, mantecado in enumerate(mantecados, start=0):
            for columna, campo_mantecado in enumerate(mantecado.values(), start=0):
                self.tableWidget.setItem(fila, columna, QTableWidgetItem(str(campo_mantecado)))
        self.tableWidget.resizeColumnsToContents()

    #CREAR
    def crear_nuevo(self):
        nuevo_mantecado = dict()
        nuevo_mantecado['nombre'] = self.nombre.text()
        nuevo_mantecado['descripcion'] = self.descripcion.text()
        nuevo_mantecado['url'] = self.url.text()
        nuevo_mantecado['precio'] = float(self.precio.text())
        insertar_dato(nuevo_mantecado)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())