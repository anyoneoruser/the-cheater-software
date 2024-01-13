# packages import
from tkinter import *
from tkinter.ttk import Combobox
import calculator,json
from translate import Translator
from PIL import ImageGrab,ImageFilter
# gui creating and basical config
gui=Tk()
gui.title("the cheater software - welcoming software preesentation")
gui.geometry("550x500+30+30")
# creating variablees for frames to insert in the gui
operation_input_frame=Frame(gui)
operation_inputs_input_frame=Frame(gui)
theme_input_frame=Frame(gui)
lang_input_frame=Frame(gui)
# creating a variable for the result canvas to display the posed operation in it
result_canvas=Canvas(gui,height=400,width=550,borderwidth=1,relief="solid",background="#96D5E0")
# creating a variable for settings button image
settings_image=PhotoImage(file="settings_icon.png").subsample(10,10)
# creating a variable for app gui elements,options and vocation of the elemnt in the gui
app_gui_structures={
    "presentation":[
    {
        "element":Button(gui,image=settings_image,borderwidth=0),
        "inserting mode":"pack",
        "inserting options":"pady=30",
        "dynamical":"def handle_click(event):\n  update_gui_structure(app_gui_structures['settings'],gui);\n  gui.title('the cheater software - settings');\nelement_informations['element'].bind('<Button-1>',handle_click)",
        "vocation":"settings button"
    },
    {
        "element":Label(gui,font=("Arial",30),text="Welcome on the cheater software!"),
        "inserting mode":"pack",
        "inserting options":"",
        "vocation":"app preesentation title"
    },
    {
        "element":Label(gui,font=("Arial",20),width=44,text="The cheater software is a calculator that can\ndisplay the posed operation and calculate all the\nmathematics functions as exponential\n(https://en.wikipedia.org/wiki/\nExponential_function for more informations)\nor specials operations as pow(https://en.wikipedia.org/wiki/\nExponentiation\nfor more informations) for you."),
        "inserting mode":"pack",
        "inserting options":"",
        "vocation":"app preesentation"
    },
    {
        "element":Button(gui,text="continue ->"),
        "inserting mode":"pack",
        "inserting options":"",
        "dynamical":"def handle_click(event):\n  update_gui_structure(app_gui_structures['use'],gui);\n  gui.title('the cheater software - use')\nelement_informations['element'].bind('<Button-1>',handle_click);",
        "vocation":"button for go to use application"
    }
    ],
    "use":[
    {
        "element":Button(gui,image=settings_image,borderwidth=0),
        "inserting mode":"pack",
        "inserting options":"pady=30",
        "dynamical":"def handle_click(event):\n  update_gui_structure(app_gui_structures['settings'],gui);\n  gui.title('the cheater software - settings');\nelement_informations['element'].bind('<Button-1>',handle_click)",
        "vocation":"settings button"
    },
    {
        "element":Button(gui,text="<- go back"),
        "inserting mode":"pack",
        "inserting options":"",
        "dynamical":"def handle_click(event):\n  update_gui_structure(app_gui_structures['presentation'],gui);\n  gui.title('the cheater software - presentation')\nelement_informations['element'].bind('<Button-1>',handle_click);",
        "vocation":"button for go to use application"
    },
    {
        "element":operation_inputs_input_frame,
        "inserting mode":"pack",
        "inserting options":"",
        "vocation":"operation inputs input frame"
    },
    {
        "element":operation_input_frame,
        "inserting mode":"pack",
        "inserting options":"",
        "vocation":"operation input frame"
    },
    {
        "element":Label(operation_inputs_input_frame,text="operation input numbers(separated it by commas):"),
        "inserting mode":"pack",
        "inserting options":"side=LEFT",
        "vocation":"form entry label"
    },
    {
        "element":Entry(operation_inputs_input_frame),
        "inserting mode":"pack",
        "inserting options":"side=LEFT",
        "vocation":"operation numbers entry"
    },
    {
        "element":Label(operation_input_frame,text="operation to do:"),
        "inserting mode":"pack",
        "inserting options":"side=LEFT",
        "vocation":"form combobox label"
    },
    {
        "element":Combobox(operation_input_frame,values=("addition(+ or ∑)","substraction(-)","multiplication(×)","division(÷)","square(√)","cube(³)","exponential(e)","pow(e)","pi getting(∏)","phi getting(φ or ϕ)","e getting","tau getting","tanh","tan","sin","cos","log","asin","atan","log2","log10","ceil","comb","round","copysign","fabs","factorial","floor","fmod","frexp(fre)","fsum(f∑)","gcd","isclose","isfinite","isinf","lcm","ldexp(lde)","modf","nextafter","perm(permutation)","prod","remainder","trunc","ulp","cbrt","expm1","log1p","sqrt","dist","hypot","acosh","asinh","atanh","cosh","sinh","erf","erfc","gamma(y)","lgamma(ly)")),
        "inserting mode":"pack",
        "inserting options":"side=LEFT",
        "vocation":"operation combobox"
    },
    {
        "element":Button(operation_input_frame,text="See the result",command=lambda :exec("result_canvas.delete('all');"+calculator.do(app_gui_structures["use"][7]["element"].get(),app_gui_structures["use"][5]["element"].get().split(",")))),
        "inserting mode":"pack",
        "inserting options":"side=LEFT",
        "dynamical":"",
        "vocation":"operation doing button"
    },
    {
        "element":result_canvas,
        "inserting mode":"pack",
        "inserting options":"side=BOTTOM",
        "vocation":"operation result canvas"
    },
    ],
    "settings":[
        {
            "element":theme_input_frame,
            "inserting mode":"pack",
            "inserting options":"",
            "vocation":"using form frame"
        },
        {
            "element":Label(theme_input_frame,text="input application theme:"),
            "inserting mode":"pack",
            "inserting options":"side=LEFT",
            "vocation":"theme changing combobox label"
        },
        {
            "element":Combobox(theme_input_frame,values=("white","dark")),
            "inserting mode":"pack",
            "inserting options":"",
            "vocation":"theme changing combobox"
        },
        {
            "element":lang_input_frame,
            "inserting mode":"pack",
            "inserting options":"",
            "vocation":"using form frame"
        },
        {
            "element":Label(lang_input_frame,text="input application lang:"),
            "inserting mode":"pack",
            "inserting options":"side=LEFT",
            "vocation":"lang changing combobox label"
        },
        {
            "element":Combobox(lang_input_frame,values=("Afrikans","Albanais","Allemand","Amharique","Anglais","Arabe","Arménien","Assamais","Aymara","Azerbaïdjanais","Bambara","Basque","Bengali","Bhodjpouri","Biélorusse","Birman","Bosniaque","Bulgare","Catalan","Cebuano","Chewa","Chinois (simplifié)","Chinois (traditionnel)","Cingalais","Coréen","Corse","Créole haïtien","Croate","Danois","Dogri","Espagnol","Espéranto","Estonien","Éwé","Finnois","Français","Frison occidental","Gaélique écossais","Galicien","Gallois","Ganda","Géorgien","Goudjarati","Grec","Guarani","Haoussa","Hawaïen","Hébreu","Hindi","Hmong","Hongrois","Igbo","Ilocano","Indonésien","Irlandais","Islandais","Italien","Japonais","Javanais","Kannada","Kazakh","Khmer","Kinyarwanda","Kirghize","Konkani de Goa","Krio","Kurde","Lao","Latin","Letton","Lingala","Lituanien","Lushaï","Luxembourgeois","Macédonien","Maïthili","Malais","Malayalam","Maldivien","Malgache","Maltais","Manipuri (meitei mayek)","Maori","Marathi","Mongol","Néerlandais","Népalais","Norvégien","Odia","Oromo","Ouïghour","Ourdou","Ouzbek","Pachto","Pendjabi","Persan","Polonais","Portugais","Quechua","Roumain","Russe","Samoan","Sanskrit","Serbe","Shona","Sindhi","Slovaque","Slovène","Somali","Sorani","Sotho du Nord","Sotho du Sud","Soundanais","Suédois","Swahili","Tadjik","Tagalog","Tamoul","Tatar","Tchèque","Télougou","Thaï","Tigrigna","Tsonga","Turc","Turkmène","Ukrainien","Vietnamien","Xhosa","Yiddish","Yoruba","Zoulou")),
            "inserting mode":"pack",
            "inserting options":"",
            "vocation":"lang changing combobox"
        },
        {
            "element":Button(gui,text="Confirm my choices",command=lambda :exec("file=open('app_settings.json','w');file.write('{\"theme\":\""+(app_gui_structures['settings'][2]['element'].get() or "white")+"\",\"lang\":\""+(app_gui_structures['settings'][5]['element'].get() or "Anglais")+"\"}');file.close();update_gui_structure(app_gui_structures['presentation'],gui);gui.title('the cheater software - presentation')")),
            "inserting mode":"pack",
            "inserting options":"side=LEFT",
            "vocation":"configuration apply button"
        }
    ]
}
# this function is to clear the gui for it update
def clear_gui(gui):
    # getting all gui elements
    gui_elements=gui.children
    # iter all gui elements
    for gui_element_key in gui_elements.keys():
        # get the element to remove
        gui_element=gui_elements[gui_element_key]
        # Removing it !
        gui_element.pack_forget()
# function to translate the application text
def translate(text):
    # getting translation langs
    lang=json.load(open("app_settings.json"))["lang"]
    langs_codes={"Afrikaans":"af",
        "Albanais":"sq",
        "Amharique":"am",
        "Arabe":"ar",
        "Arménien":"hy",
        "Assamais*":"as",
        "Aymara*":"ay",
        "Azéri":"az",
        "Bambara*":"bm",
        "Basque":"eu",
        "Biélorusse":"be",
        "Bengalî":"bn",
        "Bhodjpouri*":"bho",
        "Bosniaque":"bs",
        "Bulgare":"bg",
        "Catalan":"ca",
        "Cebuano":"ceb",
        "Chinois (simplifié)":"zh-CN",
        "Chinois (traditionnel)":"zh-TW",
        "Corse":"co",
        "Croate":"hr",
        "Tchèque":"cs",
        "Danois":"da",
        "Divéhi*":"dv",
        "Dogri*":"doi",
        "Néerlandais":"nl",
        "Anglais":"en",
        "Espéranto":"eo",
        "Estonien":"et",
        "Ewe*":"ee",
        "Filipino (Tagalog)":"fil",
        "Finnois":"fi",
        "Français":"fr",
        "Frison":"fy",
        "Galicien":"gl",
        "Géorgien":"ka",
        "Allemand":"de",
        "Grec":"el",
        "Guarani*":"gn",
        "Gujarâtî":"gu",
        "Créole haïtien":"ht",
        "Haoussa":"ha",
        "Hawaïen":"haw",
        "Hébreu":"he",
        "Hindi":"hi",
        "Hmong":"hmn",
        "Hongrois":"hu",
        "Islandais":"is",
        "Igbo":"ig",
        "Ilocano*":"ilo",
        "Indonésien":"id",
        "Irlandais":"ga",
        "Italien":"it",
        "Japonais":"ja",
        "Javanais":"jv",
        "Kannara":"kn",
        "Kazakh":"kk",
        "Khmer":"km",
        "Kinyarwanda":"rw",
        "Konkani*":"gom",
        "Coréen":"ko",
        "Krio*":"kri",
        "Kurde":"ku",
        "Kurde (Sorani)*":"ckb",
        "Kirghyz":"ky",
        "Laotien":"lo",
        "Latin":"la",
        "Letton":"lv",
        "Lingala*":"ln",
        "Lituanien":"lt",
        "Luganda*":"lg",
        "Luxembourgeois":"lb",
        "Macédonien":"mk",
        "Maïthili*":"mai",
        "Malgache":"mg",
        "Malais":"ms",
        "Malayâlam":"ml",
        "Maltais":"mt",
        "Maori":"mi",
        "Marathi":"mr",
        "Meitei (Manipuri)*":"mni-Mtei",
        "Mizo*":"lus",
        "Mongol":"mn",
        "Birman":"my",
        "Népalais":"ne",
        "Norvégien":"no",
        "Nyanja (Chichewa)":"ny",
        "Odia (Oriya)":"or",
        "Oromo*":"om",
        "Pachtô":"ps",
        "Perse":"fa",
        "Polonais":"pl",
        "Portugais (Portugal, Brésil)":"pt",
        "Panjabi":"pa",
        "Quechua*":"qu",
        "Roumain":"ro",
        "Russe":"ru",
        "Samoan":"sm",
        "Sanskrit*":"sa",
        "Gaélique (Écosse)":"gd",
        "Sepedi*":"nso",
        "Serbe":"sr",
        "Sesotho":"st",
        "Shona":"sn",
        "Sindhî":"sd",
        "Singhalais":"si",
        "Slovaque":"sk",
        "Slovène":"sl",
        "Somali":"so",
        "Spanish":"es",
        "Soundanais":"su",
        "Swahili":"sw",
        "Suédois":"sv",
        "Tagalog (philippin)":"tl",
        "Tadjik":"tg",
        "Tamoul":"ta",
        "Tatar":"tt",
        "Télougou":"te",
        "Thaï":"th",
        "Tigrinya*":"ti",
        "Tsonga*":"ts",
        "Turc":"tr",
        "Turkmène":"tk",
        "Ukrainien":"uk",
        "Urdu":"ur",
        "Ouïghour":"ug",
        "Ouzbek":"uz",
        "Vietnamien":"vi",
        "Gallois":"cy",
        "Xhosa":"xh",
        "Yiddish":"yi",
        "Yoruba":"yo",
        "Zoulou":"zu"
    }
    tl=langs_codes[lang]
    # translating text and return it
    translator= Translator(to_lang=tl)
    return translator.translate(text=text)
# this function is for config gui apparance using a dictionary of the gui structure and it config(precedent config or no config is used if config not specified)
def update_gui_structure(gui_structure,gui,config=None):
    # clear gui beforee update it
    clear_gui(gui)
    # if config is specified or they have last config,getting informations in config and keep it to change gui elements before insertion(the auther part of config can be do with gui config method)
    white_theme=False
    if config or gui.last_config:
        # keeping last configuration in the configurated gui to dont respecify it
        gui.last_config=config or gui.last_config
        # keeing informations of config
        if gui.last_config["theme"]=="white":
            white_theme=True
    # gui elements insertiing loop
    for element_informations in gui_structure:
        # elements is changed before insertion because application config
        # elements changing for theme configuration
        if white_theme:
            # label elements changing if theme is white
            element_informations['element']["background"]="white"
            if "fg" in element_informations["element"].configure().keys():
                element_informations['element']["fg"]="black"
        else:
            # label elements changing if theme is dark
            element_informations['element']["background"]="#323232"
            if "fg" in element_informations["element"].configure().keys():
                element_informations['element']["fg"]="white"
        # elements changing for lang configuration
        if "text" in element_informations["element"].configure().keys():
                element_informations['element']["text"]=translate(element_informations['element']["text"])
        # eval code for do the element dynamical
        if "dynamical" in element_informations:
            exec(element_informations["dynamical"])
        # eval code to insert the element in the gui
        eval("element_informations['element']."+str(element_informations["inserting mode"])+"("+str(element_informations["inserting options"])+")")# eval code to insert the element in the gui