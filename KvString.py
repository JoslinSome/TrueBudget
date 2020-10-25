from kivy.lang.builder import Builder

CircleProgress= Builder.load_string("""
<Bar>:

""")
screenHelp = """
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
Screen:
    
    
    profile: profile
    manage:manage
    toolbar:toolbar
    layout:layout
    scroll2:scroll2
    item1: item1
    item2: item2
    item3: item3
    item4: item4
    item5: item5
    view: view
    track:track
    panel: panel
    save:save
    recur:recur
    overview:overview
    scroll1:scroll1
    cp:cp.__self__

    MDBottomNavigation:
        id: panel
        scroll2:scroll2
        panel_color: 1, 1, 1, 1
        MDBottomNavigationItem:
            name: 'recur'
            id: recur
            on_tab_release: app.tab_switchRecur()
            view:view
            viewAll:viewAll
            recurBtn:recurBtn
            recurLabel:recurLabel
            text: 'Recurring'
            icon: 'calendar-month'
            MDRectangleFlatButton:
                id:viewAll
                text: 'View All'
                pos_hint: {"center_x":0.87,"center_y":0.52} 

                on_release:
                    app.viewMore()
                text_color: app.theme_cls.primary_color
            MDLabel:
                id:recurLabel
                text: "Reccuring payments"
                font_style: "H6"       
                pos_hint: {"center_x":0.65,"center_y":0.7}

            MDIconButton:
                icon: "help-circle-outline"
                pos_hint: {"center_x":0.9,"center_y":0.95}
                theme_text_color: "Custom"
                on_release: app.helpReccuring()


            ScrollView:
                lists3:lists3
                id: view
                pos_hint: {"center_y":0.3}
                size_hint_y: 0.4
                MDList:
                    id:lists3
                    item1:item1
                    item2:item2
                    item3:item3
                    item4:item4
                    item5:item5

                    TwoLineAvatarIconListItem:
                        id: item1
                        text: ""
                        secondary_text: ""
                        IconLeftWidget:
                            icon: "cash-usd-outline"
                        IconRightWidget:
                            icon: "trash-can-outline"
                            on_release:
                                app.delItem1()

                    TwoLineAvatarIconListItem:
                        id: item2
                        text: ""
                        secondary_text: ""
                        IconLeftWidget:
                            icon: "cash-usd-outline"
                        IconRightWidget:
                            icon: "trash-can-outline"
                            on_release:
                                app.delItem2()
                    TwoLineAvatarIconListItem:
                        id: item3
                        text: ""
                        secondary_text: ""
                        IconLeftWidget:
                            icon: "cash-usd-outline"
                        IconRightWidget:
                            icon: "trash-can-outline"
                            on_release:
                                app.delItem3()
                    TwoLineAvatarIconListItem:
                        id: item4
                        text: ""
                        secondary_text: ""
                        IconLeftWidget:
                            icon: "cash-usd-outline"
                        IconRightWidget:
                            icon: "trash-can-outline"
                            on_release:
                                app.delItem4()
                    TwoLineAvatarIconListItem:
                        id: item5
                        text: ""
                        secondary_text: ""
                        IconLeftWidget:
                            icon: "cash-usd-outline"
                        IconRightWidget:
                            icon: "trash-can-outline"
                            on_release:
                                app.delItem5()
            MDFloatingActionButton:
                id: recurBtn
                icon: "plus"
                pos_hint: {"center_x":0.12,"center_y":0.1}
                md_bg_color: app.theme_cls.primary_color
                elevation_normal: 10
                user_font_size: "20sp"
                on_release: app.addRecurringItem()
        MDBottomNavigationItem:
            name: 'track'
            text: 'Track'
            on_tab_release: app.tab_switchTrack()
            id:track
            lists1:lists1
            icon: 'book-open-page-variant'
            MDLabel:
                text: 'Track your money flow'
                font_style: "H5"
                pos_hint: {"center_x":0.6, "center_y": 0.8}
            MDFillRoundFlatButton:
                text: "Money Income"
                pos_hint: {"center_x": 0.5,"center_y": 0.25}
                size_hint: (0.8,0.1)

                on_release: 
                    app.AddTrackOutgo()
            MDFillRoundFlatButton:
                text: "Money Outgo"
                pos_hint: {"center_x": 0.5,"center_y": 0.1}
                size_hint: (0.8,0.1)
                on_release: 
                    app.AddTrack()
            ScrollView:
                size_hint_y: 0.3
                id: scroll2
                pos_hint: {"center_y": 0.6}
                MDList:
                    id:lists1

            

        MDBottomNavigationItem:
            id:save
            name: 'save'
            text: 'Save'
            icon: 'trophy'
            lists:lists
            scroll1:scroll1
            on_tab_release: app.tab_switchSave()
            btn:btn.__self__
            progress:progress
        
            MDFillRoundFlatButton:
                id:btn
                text: "New Item"
                
                pos_hint: {"center_x": 0.5,"center_y": 0.7}
                size_hint: (0.7,0.1)
                on_release:
                    app.SaveDialog()
                
            ScrollView:
                size_hint_y: 0.6
                id: scroll1
                MDList:
                    id:lists
            FloatLayout:
                
                id: progress
                canvas.before:
                    Rectangle:
                        # self here refers to the widget i.e BoxLayout
                        pos: self.pos
                        size: self.size
                CircularProgressBar:
                    id: cp
                    size_hint:(None,None)
                    height:300
                    width:300
                    max:100
                    pos_hint: {"center_x": 0.5, "center_y": 0.25}
        MDBottomNavigationItem:
            id:overview
            name: 'overview'
            text: 'Overview'
            on_tab_release: app.tab_switchView()
            icon: 'view-grid-outline'
            MDLabel: 
                text: "View your total spendings"
                font_style: "H5"
                pos_hint: {"center_x":0.55, "center_y": 0.75}
            

    BoxLayout:
        orientation: "vertical"
        MDToolbar:
            title: "TrueBudget"
                
            id: toolbar
            left_action_items: [["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
            right_action_items: [["help-circle-outline",lambda x: app.helpReccuring()]]

            size_hint_y: None
            elevation: 10

       
        NavigationLayout:
            id: layout
            ScreenManager:
                id:manage
                viewAll:


            MDNavigationDrawer:
                id: nav_drawer
                size_hint_x: None   
                 
                width: 300
                
                BoxLayout:
                    orientation: "vertical"

                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: "Theme"
                                on_release: app.ThemeChange()
                                IconLeftWidget:  
                                    icon:"format-color-text"
                    Widget:
                    Widget:


    ScreenManager:

        MenuScreen:
            
            Widget:


            NavigationLayout:
                id: layout
                ScreenManager:
                    id:manage
                    viewAll:


                MDNavigationDrawer:
                    id: nav_drawer2
                    size_hint_x: None    
                    width: 300
                    BoxLayout:
                        orientation: "vertical"

                        Image: 
                            
                        Widget:
                        Widget:
            


        ProfileScreen:
            id: profile

        UploadScreen:
        

<MenuScreen>:
    name: 'menu'


    


<UploadScreen>:
    name: 'upload'


        
<ProfileScreen>:
   
    
"""
dialogBox = """

Content:
    id:Content
    name: name
    cost: cost
    orientation: "vertical"
    spacing: "1dp"
    size_hint_y: None
    height: "200dp"
    MDTextField:
        id: name 
        hint_text: "Item Name"
        helper_text: "Example: Netflix,Rent"
        helper_text_mode: "on_focus"
        pos_hint:{"center_x":0.5,"center_y":0.8}
    MDTextField:
        hint_text: "Item Cost"
        text: "$"
        id: cost
        helper_text: "Please enter a value"
        helper_text_mode: "on_error"
        halign: "auto"
        pos_hint:{"center_x":0.5,"center_y":0.8}
    MDFlatButton:
        text: "Date:"
        on_press: app.show_date_picker()
        text_color: app.theme_cls.primary_color

"""
occurrence = """
MDLabel:
    text: app.recurringday
"""

dialogBox1 = """


<Content1>:
    id: Content1
    orientation: "vertical"

    size_hint_y: None
    height: "200dp"
    BoxLayout:
        orientation: "vertical"
        MDLabel:
            text: "Item Name: "+  app.tempName
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
        MDLabel:
            text: "Item Cost: "+  app.tempCost
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
        MDLabel:
            text: "Occurs Monthly on the "+ app.recurringday
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color

    
<help>:

    MDLabel:
        text: "Track your recurring monthly payments like Rent and Netflix. Click on the plus icon at the bottom left of the screen to add a recurring item!"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpTrack>:

    MDLabel:
        text: "Keep track of the money you gain and spend, press the buttons below to create an Item"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpOverview>:

    MDLabel:
        text: "View your monthly spendings so far. First create a spending item on the reccuring or track tab before being able to view"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<helpSave>:

    MDLabel:
        text: "Want to save up for something?, create a new item and keep track of how much hou have saved"
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.2}
<Existing>:
    MDLabel:
        text: "The Item you entered already exists. Please change its Name" 
<Content2>:
    title: "hello" 
    name: name
    cost: cost
    BoxLayout:
        spacing: "20dp"

        MDTextField: 
            id: name
            hint_text: "Item Name:"
        MDTextField:
            hint_text: "Item Cost:"
            id:cost
            text: "$"
    
<Content3>:
    month:month
    MDTextField:
        id: month
        hint_text: "Amount"
        text: "$"
        
<Content4>:
    title: "hello" 
    name: name
    cost: cost
    BoxLayout:
        spacing: "20dp"

        MDTextField: 
            id: name
            hint_text: "Item Name:"
        MDTextField:
            hint_text: "Item Cost:"
            id:cost
            text: "$"

<Content5>:
    title: "hello" 
    MDLabel:
        text: "The Item you entered already exists, would you like to add onto it? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}
    
<Warning>:
    MDLabel:
        text: "Are you sure you want to delete this item? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}
<Warning1>:
    MDLabel:
        text: "Are you sure you want to delete this item? "
        theme_text_color: "Secondary"
        pos_hint: {"center_y": 0.6}

<Add>:
    title: "hello" 
    cost: cost
    BoxLayout:
        spacing: "20dp"

        MDTextField:
            hint_text: "Add amount:"
            id:cost
            text: "$"
    
"""
dialogBox2 = """
Content2:
    scroll: scroll

"""
viewScreen = """
<viewAll>:

    ScrollView:


"""

pannel = """

"""

