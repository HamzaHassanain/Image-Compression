
# import Qt
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PIL


import Compressor
from ImageViewer import QImageViewer


class AppUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.compressor = Compressor.Compressor()

        try:
            self.setWindowTitle("Image Compressor")
            self.setGeometry(200, 200, 800, 600)
            self.setWindowIcon(QtGui.QIcon("icon.png"))
            self.initUI()
        except Exception as e:
            print(f"Error: {str(e)}")

    def initUI(self):

        # set icons

        self.image_label = QtWidgets.QLabel("Image Path:")
        self.image_path = QtWidgets.QLineEdit()
        self.browse_btn = QtWidgets.QPushButton("Browse")
        self.quality_label = QtWidgets.QLabel("Quality:")
        self.quality_spin = QtWidgets.QSpinBox()
        self.quality_spin.setRange(0, 95)
        self.quality_spin.setValue(90)
        self.resize_label = QtWidgets.QLabel("Resize Ratio:")
        self.resize_spin = QtWidgets.QDoubleSpinBox()
        self.resize_spin.setRange(0, 1)
        self.resize_spin.setValue(1.0)
        # self.width_label = QtWidgets.QLabel("Width:")
        # self.width_spin = QtWidgets.QSpinBox()
        # self.height_label = QtWidgets.QLabel("Height:")
        # self.height_spin = QtWidgets.QSpinBox()
        self.to_jpg = QtWidgets.QCheckBox("Convert to JPEG")
        self.compress_btn = QtWidgets.QPushButton("Compress")
        self.output_label = QtWidgets.QLabel("Output:")
        self.output_text = QtWidgets.QTextEdit()
        self.output_text.setReadOnly(True)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.image_path)

        self.layout.addWidget(self.browse_btn)

        self.layout.addWidget(self.quality_label)
        self.layout.addWidget(self.quality_spin)
        self.layout.addWidget(self.resize_label)
        self.layout.addWidget(self.resize_spin)
        # self.layout.addWidget(self.width_label)
        # self.layout.addWidget(self.width_spin)
        # self.layout.addWidget(self.height_label)
        # self.layout.addWidget(self.height_spin)
        self.layout.addWidget(self.to_jpg)
        self.layout.addWidget(self.compress_btn)
        self.layout.addWidget(self.output_label)
        self.layout.addWidget(self.output_text)

        self.image_viewer = QImageViewer()

        self.setLayout(self.layout)

        self.browse_btn.clicked.connect(self.browse)
        self.compress_btn.clicked.connect(self.compress)

    def browse(self):
        # file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
        #     self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        # read the image while making sure you read the correct width and height and not rotated

        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        # get the file info

        if file_name:
            self.image_path.setText(file_name)
            self.image_viewer.show()
            self.image_viewer.open(file_name)
        else:
            pass

    def compress(self):

        image_path = self.image_path.text()

        quality = self.quality_spin.value()

        resize_ratio = self.resize_spin.value()

        # width = self.width_spin.value()

        # height = self.height_spin.value()

        to_jpg = self.to_jpg.isChecked()

        try:
            data = self.compressor.compress_img(image_path, resize_ratio,
                                                quality, 0, 0, to_jpg)

            self.output_text.setText(

                f"Image Saved To: {data['image']}\nSize Before: {data['size_before']}\nSize After: {
                    data['size_after']}\nSize Change: {data['size_change']}")

        except Exception as e:
            self.output_text.setText(f"Error: {str(e)}")

        self.image_path.clear()


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    window = AppUI()
    window.show()

    sys.exit(app.exec_())
