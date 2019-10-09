'''
批量给图片添加水印
zmister.com/archives/1006.html
by 张强 2019。9。27
'''
import  sys,os
from PyQt5 import QtWidgets,QtCore
class MianApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("一键图片水印")
        self.setFixedSize(350,160)

        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.folder_input = QtWidgets.QLineEdit()
        self.folder_input.setReadOnly(True)
        self.folder_btn = QtWidgets.QPushButton("选择文件夹")

        self.wm_input = QtWidgets.QLineEdit()
        self.wm_input.setReadOnly(True)
        self.wm_btn = QtWidgets.QPushButton("选择水印图片")

        self.save_input = QtWidgets.QLineEdit()
        self.save_input.setReadOnly(True)
        self.save_btn = QtWidgets.QPushButton("保存目录")

        self.position_label = QtWidgets.QLabel('水印位置：')
        self.position_box = QtWidgets.QComboBox()
        self.position_box.addItem("左上")
        self.position_box.addItem("左下")
        self.position_box.addItem("右上")
        self.position_box.addItem("右下")
        self.position_box.addItem("居中")

        self.submit_btn = QtWidgets.QPushButton("生成图片")

        self.main_layout.addWidget(self.folder_input,0,0,1,1)
        self.main_layout.addWidget(self.folder_btn,0,1,1,1)
        self.main_layout.addWidget(self.wm_input,1,0,1,1)
        self.main_layout.addWidget(self.wm_btn,1,1,1,1)
        self.main_layout.addWidget(self.save_input,2,0,1,1)
        self.main_layout.addWidget(self.save_btn,2,1,1,1)
        self.main_layout.addWidget(self.position_label,3,0,1,1)
        self.main_layout.addWidget(self.position_box,3,1,1,1)
        self.main_layout.addWidget(self.submit_btn,4,0,1,2)
        self.setCentralWidget(self.main_widget)

        # 信号与槽函数相连
        self.save_btn.clicked.connect(self.select_save_folder)
        self.wm_btn.clicked.connect(self.select_wm_img)
        self.folder_btn.clicked.connect(self.select_folder)
        self.submit_btn.clicked.connect(self.generate_img)

    #选择文件
    def select_folder(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self,'选择文件夹'))
        print('文件夹为：',file)
        if file != '':
            self.folder_input.setText(file)
    #选择水印图片
    def select_wm_img(self):
        file,_=QtWidgets.QFileDialog.getOpenFileName(
            self,'选择水印图片','','Images(*.png *.xpm *.jpg)'
        )
        print('水印图片为：',file)
        if file !='':
            self.wm_input.setText(file)
    #选择保存目录
    def select_save_folder(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self,"选择文件夹"))
        print("文件夹为：",file)
        if file !='':
            self.save_input.setText(file)
    #生成水印图片
    def generate_img(self):
        try:
            print("获取图片目录及水印文件名")
            folder_text self.folder_input.text()
            wm_text = self.wm_input.text()
            save_text = self.save_input.text()
            posistion_text = self.position_box.currentText()
            print("判断是否为空")
            if folder_text != '' wm_text != '':
                self.submit_btn.setEnabled(False)
                self.genare_thred = WmThread(
                    wm_file = wm_text,
                    fpath=folder_text,
                    save_path= save_text,
                    position = posistion_text
                )
                print('启动线程')
                self.genare_thred.finished_signal.connect(self.thread_resp)
                self.genare_thred.start()
        except Exception as e:
            print(traceback.print_exc())
    def thread_resp(self,value):
        if value == 1:
            QtWidgets.QMessageBox.information(self,'提示','处理完成！',QtWidgets.QMessageBox.Yes)
        if value == 0:
            QtWidgets.QMessageBox.information(self,'提示','处理错误！',QtWidgets.QMessageBox.Yes)
        self.submit_btn.setEnabled(True)

#子线程处理
class WmThread(QtCore.QThread):
    finished_signal = QtCore.pyqtSignal(int) #使用PySide2模块需要将pyqtSignal改成Signal

    def __init__(self,parent=None,wm_file = None,fpath = None,save_path = None,position = None):
        super().__init__()
        self.wm_file = wm_file
        self.fpath = fpath
        self.save_path = save_path
        self.position = position
        print(self.wm_file,self.fpath)

    #获取文件夹图片
    def get_folder(self,fpath):
        try:
            img_suffix_list =['png','jpg','bmp']
            for i in os.listdir(fpath):
                if i.split('.')[-1] in img_suffix_list:
                    img_path = fpath +'/'+ i
                    self.img_water_mark(img_file=img_path,wm_file=self.wm_file)
        except Exception as e:
            print(traceback.print_exc())
    #图片添加水印
    def img_water_mark(self,img_file,wm_file):
        try:
            img = Image.open(img_file)#打开图片
            watermark = Image.open(wm_file)
            img_size = img.size
            wm_size = watermark.size
            #如果图片大小小于水印大小
            if img_size[0] &lt; wm_size[0]:
                watermark.resize(tuple(map(lambda x:int(x * 0.5),watermark.size)))
            print('图片大小：',img_size,"水印位置：",self.position)
            if self.position =='左上':
                wm_position = (0,0)
            elif self.position =='左下':
                wm_position = (0,img_size[1] - wm_size[1])
            elif self.position =='右上':
                wm_position = (img_size[0] - wm_size[0],0)
            elif self.position == '右下':
                wm_position =(img_size[0] - wm_size[0],img_size[1] - wm_size[1])
            elif self.position =='居中':
                wm_position = (img_size[0]//2 - wm_size[0]//2,img_size[1]//2 - wm_size[1]//2)
            layer = Image.new('RGBA',img.size)
            layer.paste(watermark,wm_position)
            mark_img = Image.composite(layer,img,layer)
            new_file_name ='/new_'+img_file.split('/')[-1]
            if self.save_path == '':
                mark_img.save(self.fpath+new_file_name)
            else:
                mark_img.save(self.save_path+new_file_name)
        except Exception as e:
            print(traceback.print_exc())

    def run(self):
        try:
            print("开始处理...")
            self.get_folder(fpath=self.fpath)
            self.finished_signal.emit(1)
        except Exception as e:
            print(traceback.print_exc())
            self.finished_signal.emit(0)




def main():
    app =QtWidgets.QApplication(sys.argv)
    win = MianApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()