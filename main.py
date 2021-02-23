#https://github.com/MrTequila/kivy-PieChart/blob/master/LICENSE
#https://github.com/MrTequila/kivy-PieChart/blob/master/LICENSE
print("hi")
from kivy import Config
from KvString import *
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker,MDThemePicker
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from datetime import date
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
import math
import kivy
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.vector import Vector
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#from math import atan2, sqrt, pow, degrees, sin, cos, radians
import random
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.list import OneLineListItem, TwoLineIconListItem, IconLeftWidget,TwoLineAvatarIconListItem,IconRightWidget
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, NoTransition, FallOutTransition
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine, MDExpansionPanelThreeLine
from kivy.app import App

SizeList=[]


#Config.set('graphics','resizable',0)
Window.size=(400,600)

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class Content2(MDBoxLayout):
    pass
class Content3(MDBoxLayout):
    pass

class Content4(MDBoxLayout):
    pass
class Warning(MDBoxLayout):
    pass
class Warning1(MDBoxLayout):
    pass
class Content1(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)

class Add(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)


class Content(MDBoxLayout):
    name = ObjectProperty(None)
    cost = ObjectProperty(None)


class help(MDBoxLayout):
    pass
class helpTrack(MDBoxLayout):
    pass
class helpOverview(MDBoxLayout):
    pass
class helpSave(MDBoxLayout):
    pass
class viewAll(Screen):
    pass


class Existing(MDBoxLayout):
    pass

class Content5(MDBoxLayout):
    pass
class Bar(Screen):
    pass


class CircularProgressBar(ProgressBar):
    def __init__(self,**kwargs):
        super(CircularProgressBar,self).__init__(**kwargs)
        self.thickness = 40
        self.label = CoreLabel(text="0",font_size=self.thickness)
        self.texture_size= None
        self.refresh_text()
        self.draw()
    def draw(self):
        with self.canvas:
            self.canvas.clear()
            #No progress
            Color(0.26,0.26,0.26)
            Ellipse(pos=self.pos, size=self.size)
            #Progress Circle
            Color(0.2,0.8,0.8)
            Ellipse(pos=self.pos,size=self.size,angle_end=(self.value/100)*360) #will be replaced with necessary data
            #Inner Circle
            Color(0.9,0.9,0.9)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            #Inner text
            Color(0, 0, 0, 1)
            Rectangle(texture=self.label.texture,size=self.texture_size,pos=(285,200))
            self.label.text = str(int(self.value)) + "%"
    def refresh_text(self):
        self.label.refresh()
        self.texture_size=list(self.label.texture.size)
    def set_value(self, value):
        self.value = value
        self.label.text = str(int(self.value)) + "%"
        self.refresh_text()
        self.draw()


# Create the screen manager
sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))
sm.add_widget(Bar(name="Bar"))


class BudgetMeApp(MDApp):


    def build(self):
        self.saveCost="11"
        self.monthlySave="11"
        self.CheckDict = {}
        self.listCount=0
        self.CheckDict1 = {}
        self.SaveItems={}
        self.Del=False
        self.RecurringPayments = {}
        self.JustClosedBox = False
        self.recurringday = ""
        self.viewlist=[]
        self.count1=0
        self.saveDict={}
        self.listDict={}
        self.numLists=0
        self.plotdict={}
        self.saveListDict={}
        self.overviewList=[]
        self.count=0
        self.totalSpendings=0
        self.readTheme=False
        self.tracktypedict={}
        self.currentDate= date.today()
        self.currentDate= self.currentDate.strftime("%Y-%b-%d")
        self.tempGoal=""
        self.list_view2 = MDList()
        self.onViewAll=False
        self.listlist=[]
        self.listlist2=[]
        self.trackTrashList=[]
        self.tracklistList=[]
        self.themeList=[]
        self.trackDict={}
        self.screen = Builder.load_string(screenHelp)
        self.label = Builder.load_string(occurrence)
        self.boxContent1 = Builder.load_string(dialogBox1)
        self.boxContent = Builder.load_string(dialogBox)
        self.theme_cls.primary_palette = "Green"
        self.scroll = ScrollView(pos_hint={"center_y": 0.1})
        self.list_view = MDList()
        self.screen2 = Builder.load_string(viewScreen)
        self.listlist3=[]
        self.loadPanel = Builder.load_string(pannel)
        Clock.schedule_interval(self.animate, 0.1)
        self.tempAmount=""
        self.plotlabels=[]
        self.end=False
        self.readSave=False
        self.plotsizes=[]
        self.listDict1={}
        self.screen.save.remove_widget(self.screen.save.progress)
        self.CommonTrack=MDDialog(content_cls=Content5(),title="Reccuring item name",size_hint=(0.8, 11), type="custom", buttons=[
                         MDFlatButton(
                             text="Yes",
                             text_color=self.theme_cls.primary_color, on_release=self.ADD
                          ),MDFlatButton(
                             text="No, Make new item",
                             text_color=self.theme_cls.primary_color, on_release=self.DontADD

                          )])
        self.backBtn=MDRectangleFlatButton(text="Back",on_release=self.normalScreen,pos_hint={"center_x":0.9})
        self.origListList=[self.screen.recur.view.lists3.item1,self.screen.recur.view.lists3.item2,
                           self.screen.recur.view.lists3.item3,self.screen.recur.view.lists3.item4,
                           self.screen.recur.view.lists3.item5]
        self.readRecur=False
        self.readTrack=False
        self.lists=[]
        for i in range (1,21):
            self.lists.append("item"+str(i))
        return self.screen

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        self.recurringday = str(date)[8:]
        self.suffix = ""
        if self.recurringday[1] == "1" and self.recurringday != "11":
            self.suffix = "st"
        elif self.recurringday[1] == "2" and self.recurringday != "12":
            self.suffix = "nd"
        elif self.recurringday[1] == "3" and self.recurringday != 13:
            self.suffix = "rd"
        else:
            self.suffix = "th"

        self.recurringday = self.recurringday + self.suffix

        self.DayLabel = MDLabel(text=self.recurringday, halign="center")
        self.dialog.dismiss()
        return self.addRecurringItem()

    def on_pause(self):

        with open("data.txt","w") as data:
            data.write("Recur")
            data.write('\n')
            for key in self.RecurringPayments.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.RecurringPayments[key]))
                data.write("\n")
            data.write("Track")
            data.write("\n")
            for key in self.trackDict.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.trackDict[key]))
                data.write(" ")
                data.write(self.tracktypedict[key])
                data.write("\n")
            data.write("Save")
            data.write("\n")

            for key in self.saveDict.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.saveDict[key]))
                data.write("\n")
            data.write("SaveDone")
            data.write("\n")
            data.write(self.theme_cls.primary_palette)
            data.write("\n")
            data.write(self.theme_cls.accent_palette)
            data.write("\n")
            data.write(self.theme_cls.theme_style)

        return True

    def on_start(self):
        self.TrackPricePos=0
        self.SavePricePos=0
        self.RecurPricePos=0
        self.NameToAdd=""
        try:
            with open("data.txt", "r") as data:


                try:
                    for line in data:

                        self.lineList=line.split()
                        if self.lineList[0] == "SaveDone":
                            self.readSave = False
                            self.readTheme=True
                        if self.lineList[0]=="end":
                            self.end=True
                        if self.lineList[0]=="Recur":
                            self.readRecur = True
                        elif self.readRecur:
                            for i in range(len(self.lineList)):
                                try:
                                    print(float(self.lineList[i][3:-2]))
                                    self.RecurPricePos = i
                                    break
                                except ValueError:
                                    print("No")
                            if(self.lineList[0]=="Track"):
                                self.readRecur=False
                                self.readTrack=True
                            else:
                                self.NameToAdd = ""
                                for i in range(self.RecurPricePos):
                                    self.NameToAdd+=self.lineList[i]+" "
                                self.RecurringPayments[self.NameToAdd] = (self.lineList[self.RecurPricePos][2:-2], self.lineList[self.RecurPricePos+1][1:-2])
                                self.plotlabels.append(self.NameToAdd)
                                self.plotsizes.append(float(self.RecurringPayments[self.NameToAdd][0][1:]))
                        elif self.readTrack: #and not self.end:
                            for i in range(len(self.lineList)):
                                print(i)
                                try:
                                    print(float(self.lineList[i][1:]))
                                    self.TrackPricePos=i

                                except ValueError:
                                    print("No")
                            self.NameToAdd=""
                            if self.lineList[0] != "Save":
                                for i in range(self.TrackPricePos):
                                    self.NameToAdd+=self.lineList[i]+" "
                                self.trackDict[self.NameToAdd]=self.lineList[self.TrackPricePos]
                                self.tracktypedict[self.NameToAdd]=self.lineList[self.TrackPricePos+1]
                                if self.tracktypedict[self.NameToAdd]=="spend":
                                    self.plotlabels.append(self.lineList[0])
                                    self.plotsizes.append(float(self.trackDict[self.NameToAdd][1:]))

                            elif self.lineList[0]=="Save":
                                self.readTrack=False
                                self.readSave=True

                        elif self.readSave:

                           for i in range(len(self.lineList)):
                               try:
                                   print(float(self.lineList[i][3:-2]))
                                   self.SavePricePos = i
                                   break
                               except ValueError:
                                   print("No ", self.lineList[i])
                           for i in range(self.SavePricePos):
                               self.NameToAdd += self.lineList[i] + " "
                           self.saveDict[self.NameToAdd]=[self.lineList[self.SavePricePos][2:-2],self.lineList[self.SavePricePos+1][1:-2]]
                        elif self.readTheme:
                            self.themeList.append(self.lineList[0])
                    self.theme_cls.primary_palette=self.themeList[1]
                    self.theme_cls.accent_palette = self.themeList[2]
                    self.theme_cls.theme_style=self.themeList[3]
                    for name in self.saveDict.keys():
                        self.saveList = TwoLineAvatarIconListItem(text=name+"  "+self.saveDict[name][0],
                                                                  on_touch_up=self.new,
                                                                  secondary_text="Current amount: " + self.saveDict[name][1])  # str(self.months)+ " months left")
                        self.icon1 = IconRightWidget(icon="trash-can-outline", on_press=self.delSave)
                        self.saveList.add_widget(self.icon1)
                        self.screen.save.lists.add_widget(self.saveList)
                        self.saveListDict[self.saveList] = self.icon1

                    for name in self.trackDict.keys():
                        if self.tracktypedict[name]=="gain":
                            self.trackList=TwoLineAvatarIconListItem(text=name, secondary_text= "Gained  "+self.trackDict[name] + " so far")  # str(self.months)+ " months left")
                            icon2 = IconLeftWidget(icon="emoticon-happy-outline")
                        else:
                            self.trackList=TwoLineAvatarIconListItem(text=name, secondary_text= "Spent  "+self.trackDict[name] + " so far")  # str(self.months)+ " months left")
                            icon2 = IconLeftWidget(icon="emoticon-sad-outline")

                        icon = IconRightWidget(icon="trash-can-outline", on_release=self.delTrack)
                        self.trackList.add_widget(icon)
                        self.trackList.add_widget(icon2)
                        self.tracklistList.append(self.trackList)
                        self.trackTrashList.append(icon)
                        self.listlist.append(self.trackList)
                        self.screen.track.lists1.add_widget(self.trackList)

                    for name in self.RecurringPayments.keys():
                        if self.screen.item1.text == "":
                            self.screen.item1.text = name+":  " +self.RecurringPayments[name][0]

                            self.screen.item1.secondary_text = "Reoccurs on the " + self.RecurringPayments[name][1]
                        elif self.screen.item1.text != "" and self.screen.item2.text == "":
                            self.screen.item2.text = name+":  " +self.RecurringPayments[name][0]
                            self.screen.item2.secondary_text = "Reoccurs on the " + self.RecurringPayments[name][1]
                        elif self.screen.item2.text != "" and self.screen.item3.text == "":
                            self.screen.item3.text = name+":  " +self.RecurringPayments[name][0]
                            self.screen.item3.secondary_text = "Reoccurs on the " + self.RecurringPayments[name][1]
                        elif self.screen.item3.text != "" and self.screen.item4.text == "":
                            self.screen.item4.text = name+":  " +self.RecurringPayments[name][0]
                            self.screen.item4.secondary_text = "Reoccurs on the " + self.RecurringPayments[name][1]
                        elif self.screen.item4.text != "" and self.screen.item5.text == "":
                            self.screen.item5.text = name+":  " +self.RecurringPayments[name][0]
                            self.screen.item5.secondary_text = "Reoccurs on the " + self.RecurringPayments[name][1]

                except IndexError:
                    print(self.trackDict)

        except FileNotFoundError:
            print("No")
        self.pieplot()
    

    def show_date_picker(self):
        if len(self.boxContent.name.text) != 0:
            try:

                print(float(self.boxContent.cost.text[1:]))
                date_dialog = MDDatePicker(callback=self.get_date, size_hint_x=(None), width=200, )
                date_dialog.open()
            except ValueError:
                self.boxContent.cost.helper_text = "Please enter a value"
                self.boxContent.cost.error = True
                self.boxContent.cost.bind(
                    on_text_validate=self.set_error_message,
                )
        else:
            self.boxContent.name.helper_text = "Please enter a name"
            self.boxContent.name.error = True
            self.boxContent.name.bind(
                on_text_validate=self.set_error_message,
            )


    def set_error_message(self, instance_textfield):
        self.screen.ids.text_field_error.error = True
    def ThemeChange(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    def addRecurringItem(self):

        self.boxContent.cost.line_color_normal = self.theme_cls.primary_color
        self.boxContent.cost.error = False
        self.boxContent.cost.color_mode = 'primary'
        self.boxContent.name.line_color_normal = self.theme_cls.primary_color
        self.boxContent.name.error = False
        self.boxContent.name.color_mode = 'primary'

        if len(self.boxContent.name.text) != 0 and len(self.boxContent.cost.text) != 0:
            self.tempName = self.boxContent.name.text
            if self.boxContent.cost.text[0] !="$":
                if "$" in self.boxContent.cost.text:
                    for i in range(len(self.boxContent.cost.text)-1):
                        if self.boxContent.cost.text[i]=="$":
                            self.boxContent.cost.text="$"+self.boxContent.cost.text[0:i]+self.boxContent.cost.text[i+1:]
                else:
                    self.boxContent.cost.text="$"+self.boxContent.cost.text
            self.tempCost = self.boxContent.cost.text
            self.dialog1 = MDDialog(content_cls=Content1(), pos_hint={"center_x": 0.5, "center_y": 0.6},
                                    title="Is this Correct?",
                                    size_hint=(0.8, 1)

                                    , type="custom",
                                    buttons=[MDFlatButton(pos_hint={"center_x": 0.75, "center_y": -0.2},
                                                          text="Yes",
                                                          text_color=self.theme_cls.primary_color,
                                                          on_release=self.CheckRecurringPaymentsYes
                                                          ),
                                             MDFlatButton(
                                                 text="Back",
                                                 pos_hint={"center_x": 0.9, "center_y": -0.2},
                                                 text_color=self.theme_cls.primary_color,
                                                 on_release=self.CheckRecurringPaymentsBack
                                             )])
            self.dialog1.open()

        if len(self.recurringday) == 4:
            try:
                print("test")

            except AttributeError:
                print("No")

        else:
            try:
                self.dialog.remove_widget(self.boxContent)
            except AttributeError:
                print("NO")

            self.dialog = MDDialog(content_cls=Content(), pos_hint={"center_x": 0.5, "center_y": 0.6}, title="Add Item",
                                   size_hint=(0.8, 10)

                                   , type="custom", buttons=[
                    MDFlatButton(
                        text="Cancel", pos_hint={"center_x": 0.9, "center_y": -0.2},
                        text_color=self.theme_cls.primary_color, on_release=self.RecurringPaymentsCLOSE
                    )])
            self.dialog.open()
            self.dialog.add_widget(self.boxContent)

        self.tempRecurringday = self.recurringday

    def RecurringPaymentsOK(self, obj):

        cost = self.boxContent.cost.text
        name = self.boxContent.name.text

    def RecurringPaymentsCLOSE(self, obj):
        self.tempCostHelpertext = self.boxContent.cost.helper_text
        self.dialog.dismiss()
        self.boxContent.cost.text = "$"
        self.boxContent.name.text = ""
        self.boxContent.cost.error = False
        self.boxContent.cost.color_mode = 'custom'
        self.boxContent.cost.line_color_normal = self.theme_cls.primary_color
        self.boxContent.cost.helper_text = ""

    def CheckRecurringPaymentsYes(self, obj):
        self.boxContent.cost.text = "$"
        self.boxContent.name.text = ""
        self.RecurringPayments[self.tempName] = (self.tempCost, self.recurringday)
        self.recurringday = ""
        self.boxContent.cost.error = False
        self.boxContent.cost.color_mode = 'custom'
        self.boxContent.cost.line_color_normal = self.theme_cls.primary_color
        self.boxContent.cost.helper_text = ""
        if self.tempName not in self.plotlabels and self.RecurringPayments[self.tempName][1][0:2]==self.currentDate[-2:]:
            self.plotlabels.append(self.tempName)
            self.plotsizes.append(float(self.tempCost[1:]))
            self.pieplot()
        if self.tempName in self.CheckDict1.keys():
            self.dialog4 = MDDialog(content_cls=Existing(), pos_hint={"center_x": 0.5, "center_y": 0.6},
                                    title="Existing Item",
                                    size_hint=(0.8, 10)

                                    , type="custom", buttons=[
                    MDFlatButton(
                        text="Close",
                        text_color=self.theme_cls.primary_color, on_release=self.existingClose)
                ])
            self.dialog4.open()
        else:
            self.dialog1.dismiss()
            self.dialog.dismiss()
            if self.screen.item1.text == "":
                self.screen.item1.text = self.tempName + ":      " + self.tempCost

                self.screen.item1.secondary_text = "Reoccurs on the " + self.tempRecurringday
            elif self.screen.item1.text != "" and self.screen.item2.text == "":
                self.screen.item2.text = self.tempName + ":      " + self.tempCost
                self.screen.item2.secondary_text = "Reoccurs on the " + self.tempRecurringday
            elif self.screen.item2.text != "" and self.screen.item3.text == "":
                self.screen.item3.text = self.tempName + ":      " + self.tempCost
                self.screen.item3.secondary_text = "Reoccurs on the " + self.tempRecurringday
            elif self.screen.item3.text != "" and self.screen.item4.text == "":
                self.screen.item4.text = self.tempName + ":      " + self.tempCost
                self.screen.item4.secondary_text = "Reoccurs on the " + self.tempRecurringday
            elif self.screen.item4.text != "" and self.screen.item5.text == "":
                self.screen.item5.text = self.tempName + ":      " + self.tempCost
                self.screen.item5.secondary_text = "Reoccurs on the " + self.tempRecurringday

        self.CheckDict1[self.tempName] = ""


    def CheckRecurringPaymentsBack(self, obj):
        self.dialog1.dismiss()
        self.dialog.open()

    def helpReccuring(self):

        if self.screen.panel.current=="track":
            self.helpdialog = MDDialog(content_cls=helpTrack(), pos_hint={"center_x": 0.5, "center_y": 0.6}, title="Help",

                                       size_hint=(0.8, 10)

                                       , type="custom", buttons=[
                    MDFlatButton(
                        text="Close", pos_hint={"center_x": 0.9, "center_y": -0.2},
                        text_color=self.theme_cls.primary_color, on_release=self.helpdialogCLOSE
                    )])
        elif self.screen.panel.current=="save":
            self.helpdialog = MDDialog(content_cls=helpSave(), pos_hint={"center_x": 0.5, "center_y": 0.6}, title="Help",

                                       size_hint=(0.8, 10)

                                       , type="custom", buttons=[
                    MDFlatButton(
                        text="Close", pos_hint={"center_x": 0.9, "center_y": -0.2},
                        text_color=self.theme_cls.primary_color, on_release=self.helpdialogCLOSE
                    )])
        elif self.screen.panel.current=="overview":
            self.helpdialog = MDDialog(content_cls=helpOverview(), pos_hint={"center_x": 0.5, "center_y": 0.6}, title="Help",

                                       size_hint=(0.8, 10)

                                       , type="custom", buttons=[
                    MDFlatButton(
                        text="Close", pos_hint={"center_x": 0.9, "center_y": -0.2},
                        text_color=self.theme_cls.primary_color, on_release=self.helpdialogCLOSE
                    )])

        else:
            self.helpdialog = MDDialog(content_cls=help(), pos_hint={"center_x": 0.5, "center_y": 0.6}, title="Help",

                                       size_hint=(0.8, 10)

                                       , type="custom", buttons=[
                    MDFlatButton(
                        text="Close", pos_hint={"center_x": 0.9, "center_y": -0.2},
                        text_color=self.theme_cls.primary_color, on_release=self.helpdialogCLOSE
                    )])
        self.helpdialog.open()
    def helpdialogCLOSE(self, obj):
        self.helpdialog.dismiss()

    def existingClose(self, obj):
        self.dialog4.dismiss()

    def viewMore(self):
        self.onViewAll=True
        self.screen.recur.remove_widget(self.screen.recur.view)
        self.screen.recur.remove_widget(self.screen.recur.viewAll)
        self.screen.recur.remove_widget(self.screen.recur.recurLabel)
        self.screen.recur.remove_widget(self.screen.recur.recurBtn)
        self.screen.recur.add_widget(self.backBtn)

        try:
            self.scroll.remove_widget(self.list_view)
        except UnboundLocalError:
            print("ok")
        for key in self.RecurringPayments.keys():
            if key not in self.CheckDict.keys():
                icon1 = IconLeftWidget(icon="cash-usd-outline")
                icon2=IconRightWidget(icon="trash-can-outline",on_release=self.delList)
                list = TwoLineAvatarIconListItem(text=key + "      " + self.RecurringPayments[key][0],
                                           secondary_text="Occurs on the " + self.RecurringPayments[key][1])
                list.add_widget(icon1)
                list.add_widget(icon2)
                self.listlist3.append(icon2)
                self.listlist2.append(list)
                self.listDict1[list]=icon2
                self.list_view.add_widget(list)
            self.CheckDict[key] = "Done"
        self.CheckDict={}
        self.scroll = ScrollView(pos_hint={"center_x": 0.5, "center_y": 0.45}, size_hint_y=0.6)
        self.scroll.add_widget(self.list_view)

        self.screen.recur.add_widget(self.scroll)
        self.label1 = MDLabel(text="All Recurring Payments:", font_style="H5",
                              pos_hint={"center_x": 0.6, "center_y": 0.75})
        self.screen.recur.add_widget(self.label1)

    def normalScreen(self,obj):
        self.screen.recur.add_widget(self.screen.recur.view)
        self.screen.recur.add_widget(self.screen.recur.viewAll)
        self.screen.recur.add_widget(self.screen.recur.recurLabel)
        self.screen.recur.add_widget(self.screen.recur.recurBtn)
        self.screen.recur.remove_widget(self.backBtn)
        self.screen.recur.remove_widget(self.label1)

        self.screen.remove_widget(self.scroll)
        self.screen.remove_widget(self.label1)
        for list in self.listlist2:
            self.list_view.remove_widget(list)
        self.onViewAll=False

    def erase(self):
        pass
    def tab_switchView(self):
        self.screen.ids.panel.current=("overview")
        self.Blayout=MDBoxLayout()
    def tab_switchSave(self):
        self.screen.ids.panel.current=("save")
    def tab_switchTrack(self):
        self.screen.ids.panel.current=("track")
    def tab_switchRecur(self):
        self.screen.ids.panel.current=("recur")
    def changeScreen(self):
        self.screen.ids.panel.switch_tab("Recurring Payments")
    def ready(self):
        pass
    def SaveDialog(self):

        self.savedialog=MDDialog(content_cls=Content2(),title="New Item", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Ok",on_release=self.saveOK),MDFlatButton(text="Cancel",on_release=self.saveCancel)]
                                , height= 350
                                  )

        self.savedialog.open()

    def saveOK(self,obj):
        self.saveName = self.savedialog.content_cls.name.text
        if self.savedialog.content_cls.cost.text[0]!="$":
            self.savedialog.content_cls.cost.text="$"+self.savedialog.content_cls.cost.text
        self.saveCost = self.savedialog.content_cls.cost.text
        try:
            self.test=float(self.saveCost[1:])


            if self.saveName!="" and self.saveCost !="$" and self.saveCost[1]!="0":
                try:

                    print(float(self.saveCost[1:]))
                    self.savedialog.dismiss()
                    self.savedialog1=MDDialog(content_cls=Content3(), pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                     ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Ok",on_release=self.saveOK1)]
                                    , height= 350,title="How much would you like to save as a base amount for this item?"
                                      )
                    self.savedialog1.open()
                except ValueError:
                    print("No")
        except ValueError:
            print("No")
    def saveCancel(self,obj):
        self.savedialog.dismiss()
    def saveOK1(self,obj):
        try:
            if self.savedialog1.content_cls.month.text[0] != "$":
                self.savedialog1.content_cls.month.text= "$"+self.savedialog1.content_cls.month.text
            self.monthlySave = self.savedialog1.content_cls.month.text
            if self.monthlySave[1]!="0":
                try:
                    float(self.monthlySave[1:])

                    self.SaveItems[self.saveName] = (self.saveCost, self.monthlySave)
                    self.months=math.ceil(float(self.saveCost[1:])/float(self.monthlySave[1:]))
                    self.savedialog1.dismiss()
                    self.saveList=TwoLineAvatarIconListItem(text=self.saveName + "    " + self.saveCost,on_touch_up=self.new, secondary_text= "Current amount: "+self.monthlySave)#str(self.months)+ " months left")
                    self.icon1=IconRightWidget(icon="trash-can-outline", on_press=self.delSave)
                    self.saveList.add_widget(self.icon1)
                    self.screen.save.lists.add_widget(self.saveList)
                    self.saveListDict[self.saveList]=self.icon1
                    self.saveDict[self.saveName] = [self.saveCost, self.monthlySave]
                    self.numLists+=1

                except ValueError:
                    print("no")
        except ReferenceError:
            print("What")

    def do(self,touch,obj):
        pass

    def new(self,touch,obj):
        if self.count==0:
            self.tempList=touch
            self.tempGoal=touch.text[-5:]
            self.tempAmount=touch.secondary_text[16:]
            self.saveLabel = MDLabel(text="Details: ", font_style="H4", pos_hint={"center_x": 0.8, "center_y": 0.7})
            self.amountSavedLabel = MDLabel(text="  Current amount saved:  " + self.tempAmount,
                                            pos_hint={"center_y": 0.55}, font_style="H6",
                                            theme_text_color="Custom", text_color=(0, 0.4, 0.8, 1))
            self.saveGoal = MDLabel(text="  Goal:  " + self.tempGoal, pos_hint={"center_y": 0.45}, font_style="H6",
                                    theme_text_color="Custom", text_color=(0, 0.4, 0.8, 1))
            self.back = MDRectangleFlatButton(text="Back", on_release=self.Goback,
                                              pos_hint={"center_x": 0.9, "center_y": 0.125})
            self.addSave = MDRectangleFlatButton(text="Add to Savings", on_release=self.add_Save,
                                                 pos_hint={"center_x": 0.85})
            # self.screen.save.scroll1.remove_widget(self.screen.save.lists)

            self.screen.save.remove_widget(self.screen.save.scroll1)
            self.screen.save.remove_widget(self.screen.save.btn)
            try:
                self.screen.save.remove_widget(self.screen.save.progress)
                self.screen.save.add_widget(self.screen.save.progress)

            except ReferenceError:
                print("No")
            self.screen.save.add_widget(self.saveLabel)
            self.screen.save.add_widget(self.amountSavedLabel)
            self.screen.save.add_widget(self.saveGoal)
            self.screen.save.add_widget(self.back)
            self.screen.save.add_widget(self.addSave)
            self.count+=1

    def animate(self, dt):
        try:
            circProgressBar = self.root.cp
            self.percentValue=round(float(self.tempAmount.split("$")[1])/float(self.tempGoal.split("$")[1])*100)
            circProgressBar.set_value(self.percentValue)
        except IndexError:
            print("No")
    def Goback(self,obj):
        try:
            self.screen.save.remove_widget(self.screen.save.progress)
        except ReferenceError:
            print("No")
        self.screen.save.remove_widget(self.saveLabel)
        self.screen.save.remove_widget(self.amountSavedLabel)
        self.screen.save.remove_widget(self.saveGoal)
        self.screen.save.remove_widget(self.back)
        self.screen.save.remove_widget(self.addSave)
        self.screen.save.add_widget(self.screen.save.scroll1)
        self.screen.save.add_widget(self.screen.save.btn)
        self.count=0
    def add_Save(self,obj):
        self.screen.save.remove_widget(self.amountSavedLabel)

        self.AddDialog = MDDialog(content_cls=Add(), title="Add amount",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom", size_hint_y=None
                                    , size_hint=(0.9, None),
                                    buttons=[MDFlatButton(text="Ok", on_release=self.JustAdd),
                                             MDFlatButton(text="Cancel", on_release=self.CloseAdd)]
                                    , height=350
                                    )
        self.AddDialog.open()
    def JustAdd(self,obj):
        try:
            if self.AddDialog.content_cls.cost.text[0]!="$":
                self.AddDialog.content_cls.cost.text="$"+self.AddDialog.content_cls.cost.text
            self.AddAmount = self.AddDialog.content_cls.cost.text
            self.AddDialog.dismiss()
            self.tempAmount="$"+str(float(self.tempAmount[1:])+float(self.AddAmount[1:]))
            self.amountSavedLabel = MDLabel(text="  Current amount saved:  " + self.tempAmount,
                                            pos_hint={"center_y": 0.55}, font_style="H6",
                                            theme_text_color="Custom", text_color=(0, 0.4, 0.8, 1))
            self.screen.save.add_widget(self.amountSavedLabel)
            self.tempList.secondary_text="Current amount: "+self.tempAmount
            self.saveDict[self.tempList.text.split()[0]][1]=self.tempAmount
        except ValueError:
            print("No")
    def CloseAdd(self,obj):
        self.AddDialog.dismiss()

    def AddTrack(self):
        self.trackDialog=MDDialog(content_cls=Content4(),title="New Item", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Ok",on_release=self.AddTrackList),MDFlatButton(text="Cancel",on_release=self.saveCancel2)]
                                , height= 350
                                  )
        self.screen.add_widget(self.trackDialog)
    def AddTrackOutgo(self):
        self.trackDialog1=MDDialog(content_cls=Content4(),title="New Item", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Ok",on_release=self.AddTrackList2),MDFlatButton(text="Cancel",on_release=self.saveCancel2In)]
                                , height= 350
                                  )
        self.screen.add_widget(self.trackDialog1)
    def AddTrackList(self,obj):
        #self.tempTrackName=
        self.trackName = self.trackDialog.content_cls.name.text
        if self.trackDialog.content_cls.cost.text[0] !="$":
            if "$" in self.trackDialog.content_cls.cost.text:
                for i in range(len(self.trackDialog.content_cls.cost.text)-1):
                    if self.trackDialog.content_cls.cost.text[i]=="$":
                        self.trackDialog.content_cls.cost.text=self.trackDialog.content_cls.cost.text[0:i]+self.trackDialog.content_cls.cost.text[i+1:]
            else:
                self.trackDialog.content_cls.cost.text="$"+self.trackDialog.content_cls.cost.text

        self.trackCost = self.trackDialog.content_cls.cost.text

        try:
            self.test=float(self.trackCost[1:])
            self.screen.remove_widget(self.trackDialog)
            if self.trackName in self.trackDict.keys():
                self.CommonTrack.open()
            self.trackList= TwoLineAvatarIconListItem(text=self.trackName,
                                          secondary_text="Spent: "+self.trackCost+" so far")  # str(self.months)+ " months left")
            icon=IconRightWidget(icon="trash-can-outline",on_release=self.delTrack)
            icon2=IconLeftWidget(icon="emoticon-sad-outline")
            self.trackList.add_widget(icon)
            self.trackList.add_widget(icon2)
            self.tracklistList.append(self.trackList)
            self.trackTrashList.append(icon)
            if self.trackName not in self.trackDict.keys():
                self.listlist.append(self.trackList)
                self.trackDict[self.trackName] = self.trackCost

                self.screen.track.lists1.add_widget(self.trackList)
            if self.trackName not in self.plotlabels:

                self.plotlabels.append(self.trackName)
                self.plotsizes.append(float(self.trackCost[1:]))
            else:
                for i in range(len(self.plotlabels)):
                    if self.plotlabels[i]==self.trackName:
                        self.plotsizes[i]+=float(self.trackCost[1:])
            self.totalSpendings+=float(self.trackCost[1:])
            self.tracktypedict[self.trackName]="spend"
            self.pieplot()
        except ValueError:
            print("No")
    def AddTrackList2(self,obj):
        #self.tempTrackName=
        self.trackName = self.trackDialog1.content_cls.name.text
        if self.trackDialog1.content_cls.cost.text[0] != "$":
            if "$" in self.trackDialog1.content_cls.cost.text:
                for i in range(len(self.trackDialog1.content_cls.cost.text) - 1):
                    if self.trackDialog1.content_cls.cost.text[i] == "$":
                        self.trackDialog1.content_cls.cost.text = self.trackDialog1.content_cls.cost.text[
                                                                 0:i] + self.trackDialog1.content_cls.cost.text[i + 1:]
            else:
                self.trackDialog1.content_cls.cost.text = "$" + self.trackDialog1.content_cls.cost.text

        self.trackCost = self.trackDialog1.content_cls.cost.text
        try:
            self.test=float(self.trackCost[1:])
            self.screen.remove_widget(self.trackDialog1)
            if self.trackName in self.trackDict.keys():
                self.CommonTrack.open()

            icon2 = IconLeftWidget(icon="emoticon-happy-outline")
            self.trackList= TwoLineAvatarIconListItem(text=self.trackName,
                                          secondary_text="Gained: "+self.trackCost+" so far")  # str(self.months)+ " months left")
            icon = IconRightWidget(icon="trash-can-outline",on_release=self.delTrack)
            self.trackList.add_widget(icon2)
            self.tracklistList.append(self.trackList)
            self.trackTrashList.append(icon)
            if self.trackName not in self.trackDict.keys():
                self.listlist.append(self.trackList)
                self.trackDict[self.trackName]=self.trackCost
                self.screen.track.lists1.add_widget(self.trackList)
            self.tracktypedict[self.trackName]="gain"

        except ValueError:
            print("NO")
    def saveCancel2(self,obj):
        self.screen.remove_widget(self.trackDialog)
    def saveCancel2In(self,obj):
        self.screen.remove_widget(self.trackDialog1)

    def ADD(self,obj):
        self.trackDict[self.trackName]="$"+str(float(self.trackDict[self.trackName][1:])+float(self.trackCost[1:]))
        for list in self.listlist:
            if list.text==self.trackName:
                list.secondary_text="Spent: "+self.trackDict[self.trackName] +" so far"
        self.CommonTrack.dismiss()
    def DontADD(self,obj):
        self.trackList = TwoLineIconListItem(text=self.trackName,
                                             secondary_text="Gained: " + self.trackCost + " so far")
        self.screen.track.lists1.add_widget(self.trackList)
        self.CommonTrack.dismiss()
    def delItem1(self):
        self.warningDialog=MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.DelItem),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)
        if self.screen.view.lists3.item1.text != "":
            self.warningDialog.open()
    def delItem2(self):
        self.warningDialog=MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.DelItem2),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)
        if self.screen.view.lists3.item2.text != "":

            self.warningDialog.open()
    def delItem3(self):
        self.warningDialog=MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.DelItem3),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)
        if self.screen.view.lists3.item3.text != "":

            self.warningDialog.open()

    def delItem4(self):
        self.warningDialog=MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.DelItem4),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)
        if self.screen.view.lists3.item4.text != "":

            self.warningDialog.open()

    def delItem5(self):
        self.warningDialog=MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.DelItem5),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)
        if self.screen.view.lists3.item5.text != "":

            self.warningDialog.open()

    def DelItem(self,obj):

        self.warningDialog.dismiss()
        del self.RecurringPayments[self.screen.view.lists3.item1.text.split()[0][0:-1]]
        self.screen.view.lists3.remove_widget(self.screen.view.lists3.item1)
        self.screen.view.lists3.item1.text = ""
        self.screen.view.lists3.item1.secondary_text = ""
        self.screen.view.lists3.add_widget(self.screen.view.lists3.item1)

    def DelItem2(self,obj):
        self.warningDialog.dismiss()
        del self.RecurringPayments[self.screen.view.lists3.item2.text.split()[0][0:-1]]
        self.screen.view.lists3.remove_widget(self.screen.view.lists3.item2)
        self.screen.view.lists3.item2.text = ""
        self.screen.view.lists3.item2.secondary_text = ""
        self.screen.view.lists3.add_widget(self.screen.view.lists3.item2)

    def DelItem3(self,obj):
        self.warningDialog.dismiss()
        del self.RecurringPayments[self.screen.view.lists3.item3.text.split()[0][0:-1]]
        self.screen.view.lists3.remove_widget(self.screen.view.lists3.item3)
        self.screen.view.lists3.item3.text = ""
        self.screen.view.lists3.item3.secondary_text = ""
        self.screen.view.lists3.add_widget(self.screen.view.lists3.item3)
    def DelItem4(self,obj):
        self.warningDialog.dismiss()
        del self.RecurringPayments[self.screen.view.lists3.item4.text.split()[0][0:-1]]
        self.screen.view.lists3.remove_widget(self.screen.view.lists3.item4)
        self.screen.view.lists3.item4.text = ""
        self.screen.view.lists3.item4.secondary_text = ""
        self.screen.view.lists3.add_widget(self.screen.view.lists3.item4)
    def DelItem5(self,obj):
        self.warningDialog.dismiss()
        del self.RecurringPayments[self.screen.view.lists3.item5.text.split()[0][0:-1]]
        self.screen.view.lists3.remove_widget(self.screen.view.lists3.item5)
        self.screen.view.lists3.item5.text = ""
        self.screen.view.lists3.item5.secondary_text = ""
        self.screen.view.lists3.add_widget(self.screen.view.lists3.item5)
    def DontDel(self,obj):
        self.warningDialog.dismiss()
    def delList(self,touch):
        self.touch=touch
        self.warningDialog =MDDialog(content_cls=Warning(),title="Delete?", pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom",size_hint_y= None
                                 ,size_hint=(0.9,None), buttons=[MDFlatButton(text="Yes",on_release=self.Delete),MDFlatButton(text="No",on_release=self.DontDel)]
                                , height= 350)

        self.warningDialog.open()
    def Delete(self,obj):
        for icon in self.listlist3:
            if icon==self.touch:
                for list in self.listlist2:
                    if self.listDict1[list]==icon:
                        del self.RecurringPayments[list.text.split()[0]]

                        self.list_view.remove_widget(list)
                        for list1 in self.origListList:
                            try:
                                if list1.text.split()[0][0:-1]==list.text.split()[0]:
                                    list1.secondary_text=""
                                    list1.text=""
                            except IndexError:
                                print("ok")
                        list.text = ""
                        list.secondary_text = ""
        self.warningDialog.dismiss()
    def delTrack(self,touch):
        self.warningDialog = MDDialog(content_cls=Warning(), title="Delete?",
                                      pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom", size_hint_y=None
                                      , size_hint=(0.9, None),
                                      buttons=[MDFlatButton(text="Yes", on_release=self.ConfirmDelete),
                                               MDFlatButton(text="No", on_release=self.DontDel)]
                                      , height=350)
        self.touch=touch
        self.warningDialog.open()
    def ConfirmDelete(self,obj):
        for i in range(len(self.trackTrashList)):
            if self.trackTrashList[i]==self.touch:
                self.screen.track.lists1.remove_widget(self.tracklistList[i])
                del self.trackDict[self.tracklistList[i].text]
        self.warningDialog.dismiss()
    def delSave(self,touch):
        self.warningDialog = MDDialog(content_cls=Warning(), title="Delete?",
                                      pos_hint={"center_x": 0.5, "center_y": 0.5}, type="custom", size_hint_y=None
                                      , size_hint=(0.9, None),
                                      buttons=[MDFlatButton(text="Yes", on_release=self.ConfirmDeleteSave),
                                               MDFlatButton(text="No", on_release=self.DontDel)]
                                      , height=350)
        self.touch = touch
        self.warningDialog.open()
    def ConfirmDeleteSave(self,obj):
        for key in self.saveListDict.keys():
            if self.saveListDict[key]==self.touch:
                self.screen.save.lists.remove_widget(key)

                for key1 in self.saveDict.keys():
                    if key1 in key.text:
                        del self.saveDict[key1]
                        break
                del self.saveListDict[key]
                break
        for key in self.saveDict.keys():
            break
        self.Goback(1)
        self.warningDialog.dismiss()

    def pieplot(self):

        self.cols = 1
        self.rows = 2
        for i in range(len(self.plotlabels)):

            self.plotdict[self.plotlabels[i]] = (self.plotsizes[i],
                                                 [random.randint(0, 255) / 255, random.randint(0, 255) / 255,
                                                  random.randint(0, 255) / 255, 1])
        position = (300, 500)
        size = (400, 400)
        chart = PieChart(data=self.plotdict, position=position, size=size, legend_enable=True)
        try:
            self.label2 = MDLabel(text=self.plotlabels[0],pos_hint={"center_x": 100, "center_y": 0.45})
            self.screen.overview.add_widget(chart)
            self.screen.overview.add_widget(self.label2)
        except IndexError:
            print("No")
       # '''
    def on_stop(self):
        with open("data.txt","w") as data:
            data.write("Recur")
            data.write('\n')
            for key in self.RecurringPayments.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.RecurringPayments[key]))
                data.write("\n")
            data.write("Track")
            data.write("\n")
            for key in self.trackDict.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.trackDict[key]))
                data.write(" ")
                data.write(self.tracktypedict[key])
                data.write("\n")
            data.write("Save")
            data.write("\n")

            for key in self.saveDict.keys():
                data.write(key)
                data.write(" ")
                data.write(str(self.saveDict[key]))
                data.write("\n")
            data.write("SaveDone")
            data.write("\n")
            data.write(self.theme_cls.primary_palette)
            data.write("\n")
            data.write(self.theme_cls.accent_palette)
            data.write("\n")
            data.write(self.theme_cls.theme_style)

class PieChart(GridLayout):
    def __init__(self, data, position, size, legend_enable=True, **kwargs):
        super(PieChart, self).__init__(**kwargs)

        # main layout parameters
        self.position = position
        self.size_mine = size
        self.col_default_width = 100
        self.data = {}
        self.cols = 2
        self.rows = 1
        self.col_force_default = True
        self.col_default_width = 300
        self.row_force_default = True
        self.row_default_height = 250
        self.size_hint_y = None
        self.size = (600, 450)
        self.temp = []

        for key, value in data.items():
            if type(value) is int:
                percentage = (value / float(sum(data.values())) * 100)
                color = [random(), random(), random(), 1]
                self.data[key] = [value, percentage, color]

            elif type(value) is tuple:
                vals = []
                for l in data.values():
                    vals.append(l[0])
                percentage = (value[0] / float(sum(vals)) * 100)
                color = value[1]
                self.data[key] = [value[0], percentage, color]

        self.pie = Pie(self.data, self.position, self.size_mine)
        self.add_widget(self.pie)

        if legend_enable:
            self.legend = LegendTree(self.data, (self.position[0]+50,self.position[1]), self.size_mine)
            self.add_widget(self.legend)

    def _update_pie(self, instance, value):
        self.legend.pos = (instance.parent.pos[0], instance.parent.pos[1])
        self.pie.pos = (instance.pos[0], instance.pos[1])
class LegendTree(GridLayout):
    def __init__(self, data, position, size, **kwargs):
        super(LegendTree, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        self.position = position
        self.size = size
        self.row_default_height = 50
        self.spacing = 5
        self.count=0
        count = 0
        for key, value in data.items():
            percentage = value[1]
            color = value[2]
            self.legend = Legend(pos=(self.position[0], self.position[1] - count * self.size[1] * 0.15),
                                 size=self.size,
                                 color=color,
                                 name=key,
                                 value=percentage,
                                 i=self.count)
            self.add_widget(self.legend)
            self.rows += 1
            count += 1
            self.count+=1
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        try:
            self.legend.pos = (instance.parent.pos[0], instance.parent.pos[1])
        except AttributeError:
            print("Error")
        self.pos = (instance.parent.pos[0] + 260, instance.parent.pos[1])


# Class for creating Legend
class Legend(FloatLayout):

    def __init__(self, pos, size, color, name, value,i, **kwargs):
        super(Legend, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 1
        self.size_hint_x = 200
        self.size_hint_y = 50
        self.name = name
        self.label = MDLabel(text=name,
                             pos=(pos[0] + size[0] * 1.3 - 320, pos[1] + size[1] * 0.9 - 180), color=[1, 1, 1, 1])
        self.tempLabel = self.label

        with self.canvas.before:
            Color(*color)
            SizeList.append((pos[0] + size[0] * 1.3-400, pos[1] + size[1] * 0.9-350))

            self.rect = Rectangle(pos=[pos[0] + size[0] * 1.3 - 400, pos[1] + size[1] * 0.9 - 150],
                                 size=(size[0] * 0.1, size[1] * 0.1))
            if len(name)<6:
                self.label = MDLabel(text=name,
                                   pos=(pos[0] + size[0] * 1.3-320,pos[1] + size[1] * 0.9 - 180),color=[1, 1, 1, 1])


            else:
                self.label = MDLabel(text=name[0:6]+"...",
                                     pos=[pos[0] + size[0] * 1.3 - 320, pos[1] + size[1] * 0.9 - 180]
                                     ,color=[1, 1, 1, 1])

    def _update_rect(self, instance, value):
        self.rect.pos = (instance.pos[0] + 100, instance.pos[1] + 100)
        self.label.pos = (instance.pos[0] + 220, instance.pos[1] + 65)


class Pie(FloatLayout):
    def __init__(self, data, position, size, **kwargs):
        super(Pie, self).__init__(**kwargs)
        self.position = position
        self.size = size
        angle_start = 0
        count = 0
        self.temp = []
        for key, value in data.items():
            percentage = value[1]
            angle_end = angle_start + 3.6 * percentage
            color = value[2]
            # add part of Pie
            self.temp.append(PieSlice(pos=self.position, size=self.size,
                                      angle_start=angle_start,
                                      angle_end=angle_end, color=color, name=key))
            self.add_widget(self.temp[count])
            angle_start = angle_end
            count += 1
        self.bind(size=self._update_temp, pos=self._update_temp)

    def _update_temp(self, instance, value):
        for i in self.temp:
            i.pos = (instance.parent.pos[0] + 55, instance.parent.pos[1] + 60)


# Class for making one part of Pie
# Main functions for handling move out/in and click inside area recognition
class PieSlice(FloatLayout):
    def __init__(self, pos, color, size, angle_start, angle_end, name, **kwargs):
        super(PieSlice, self).__init__(**kwargs)
        self.moved = False
        self.angle = 0
        self.name = name
        with self.canvas.before:
            Color(*color)
            self.slice = Ellipse(pos=pos, size=size,
                                 angle_start=angle_start,
                                 angle_end=angle_end)
        self.bind(size=self._update_slice, pos=self._update_slice)

    def _update_slice(self, instance, value):
        self.slice.pos = (instance.pos[0], instance.pos[1])
    #def on_touch_down(self, touch):
    #    if self.is_inside_pie(*touch.pos):
            #self.move_pie_out()

    # Function for checking if click is inside Pie Slice

    def is_inside_pie(self, *touch_pos):
        y_pos = touch_pos[1] - self.slice.pos[1] - self.slice.size[1] / 2
        x_pos = touch_pos[0] - self.slice.pos[0] - self.slice.size[0] / 2
        angle = degrees(1.5707963268 - atan2(y_pos, x_pos))
        if angle < 0:
            angle += 360
        self.angle = angle
        radius = sqrt(pow(x_pos, 2) + pow(y_pos, 2))
        if self.slice.angle_start < angle < self.slice.angle_end:
            return radius < self.slice.size[0] / 2

BudgetMeApp().run()
