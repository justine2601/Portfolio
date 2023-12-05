class NameNode:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class NAME:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = NameNode(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print ('\t\t\t\t',printval.dataval)
            printval = printval.nextval
    def search(self, x): 
        current = self.headval
        while current != None: 
            if current.dataval == x: 
                return True # data found 
            current = current.nextval
        return False
import time 
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
sword = 0
flower = 0
required = ("\n Gumamit lamang ng Letrang A, B, or C\n") 
def intro():
  print ('''\nIkaw ay nag lalakad sa kagubatan habang umiinom ng alak lasing na lasing at ang paligid mo ay parang umiikot ng biglang may malakas na kaluskos sa paligid''')
  time.sleep(2)
  print ("\nIsang TIKBALANG!\n\nAno ang iyong gagawin?")
  time.sleep(1)
  print ("A. Pupulot ng bato at ihagis sa Tikbalang \nB. Humiga at mag patay-patayan \nC. Tumakbo ng Mabilis")
  choice = input(">>> ")
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    option_catch()
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ('''\nTumumba ang tikbalang dahil tinabaan mo ang kanyang kahinaan
   ngunit ang Tikbalang ay Nakatayo muli at
   sinumulan ka habulin ano ang iyong gagawin? ''')
  time.sleep(1)
  print ("A. Tumakbo ng Mabilis \nB. Pumunta sa malapit na kweba")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ('''\nDahil Desperado kang mabuhay pumunta ka ng kweba,
  madilim at nakakatakot ang kweba at me napansin kang kumikinang na bagay
  sa lapag ay me espada. \nPupulutin moba? Y/N?''')
  choice = input(">>> ")
  if choice in yes:
    sword = 1
  else:
    sword = 0
  print ("\n Ano ang iyong susunod na gagawin?")
  time.sleep(1)
  print ("A. Mag tago at tumahimik hangang umalis ang Tikbalang \nB. Kalabanin gamit ang espada \nC. Tumakbo muli")
  choice = input(">>> ")
  if choice in answer_A:
    print("nakita ka ng tikbalang kaya naman ikaw ay nahuli")
    time.sleep(1)
    option_catch()
  elif choice in answer_B:
   if sword > 0:
    print ('''\nNag hintay ka habang naka angat ang iyong espada at ang
    tikbalang ay lumapit sayo papalapit ng papalapit at ang iyong puso ang
    tumitibok ng parang lalabas na sa iyong dibdib nang ikaw ay malapitan na
    sinaksak mo sa dibdib ang tikbalang kaya ikaw ay nabuhay''')
    time.sleep(1)
    print ("Tapos na ang laro ikaw ay Nabuhay ng matiwasay ")
    print ("Mag Laro muli? Y/N ")
    time.sleep(1)
    ulet=input(">>> ")
    if ulet in yes:
      intro()
   else: 
      print ("\nDapat kinuha mo ang espeda wala kang dipensa. \n\nPatay kana!")
      time.sleep(1)
      print ("Mag Laro muli? Y/N ")
      ulet=input(">>> ")
      if ulet in yes:
        intro()
      else:
        print("Salamat sa Paglalaro")
  elif choice in answer_C:
    print ("habang pumapasok ang tikbalang paloob ng kweba pumuslit ka ng dahan dahan at tahimik hangang sa ikaw ay makatakbo ")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ('''\nTumakbo ng ng mabilis hangang sa iyong makakaya ngunit mas
  mabilis ang tikbalang ano ang gagawin mo? ''')
  time.sleep(1)
  print ("A. Magtago sa malaking Bato \nB. Lumaban sa makakaya \nC. Pumunta sa abandonadong lugar")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Mabilis ka nakita ng tikbalang. at ikaw ay hinuli")
    time.sleep(1)
    option_catch()
  elif choice in answer_B:
    print ("Na abatan ka ng tikbalang kanaman nahuli ka nito")
    option_catch()
    time.sleep(1)

  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ('''\nhabang ikaw ay tumatakbo sa takot me nakita ka na kinakalawang na espada sa putikan pero hindi mo naabot.\nsa likod ng sirang gusali
  iniintay mo ang tikbalang at umikot sa paligid ng me mapansin kang bulaklak \nkukunin mo ba ito ? Y/N? ''')  
  choice = input(">>> ")
  if choice in yes:
    flower = 1
  else:
    flower = 0
  print ('''May narinig kang malakas na yapak at hinanda mo ang iyong sarili sa mang yayari''')
  time.sleep(1)
  if flower > 0:
    print ('''\nHinawakan mo ng mahigpit ang bulaklak na nag babakasakali na
    mapahitno ang tikbalang sa pag habol sayo. \n Yun nga Hindi kana hinabol
    ng tikbalang ngunit minahal ka nito dahil sa hawak mong
    bulaklak\n\nKakaiba ito pero nabuhay ka!''')
  else: 
    print ("\nSana Kinuha mo ang bulaklak para ikaw ay nabuhay. \nPatay Kana!")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
    else:
      print("Salamat sa Paglalaro") 

#bagong choices para sa intro -b
def option_catch():
  print('''Nahuli ka ng tikbalang itinali ka habang nag iinit ng tubig para ikaw ay iluto at me nakita kang matalim na
  bagay sa iyong tabi ngunit ito ay mahirap abutin'
  ano ang gagawin mo? ''')
  time.sleep(1)
  print ('''A.)pilit abutin ang matalim na bagay upang putulin ang tali
  B.)subukan luwagan ang tali upang makatakas
  C.)mag sisigaw hangang sa may tumulong''')  
  choice = input(">>> ")
  if choice in answer_A:
    option_escape2()
  elif choice in answer_B:
    option_escape()
  elif choice in answer_C:
    option_escape3()
  else:
    print (required)
    option_catch()
#para sa catch -b
def option_escape():
  print('''naluwagan mo ang tali sa sobrang taranta tumakbo
  ka ng mabilis ng hindi  namamalayan ngunit sa takot hindi
  mo namalayang naliligaw kana pala
  habang ikaw ay hingal na hingal me naririnig kang maliit na boses
  mga duwende! 
  ano ang gagawin mo''')
  time.sleep(1)
  print ('''a.) makipag kaibigan at humingi ng tulong
  b.) mag tanong kung saan ang daan
  c.) tumakbo palayo sa teritoryo ng mga duwende''')  
  choice = input(">>> ")
  if choice in answer_A:
    duwende()
  elif choice in answer_B:
    duwende()
  elif choice in answer_C:
    duwende2()
  else:
    print (required)
    option_escape()
    #catch a
def option_escape2():
  print('''magaling naabot mo ang talim at iyong naputol ang tali. tinignan mo ang tikbalang at
  abala ito sa pag ayos para ikaw ay lutuin ano 
  ang gagawin mo?''')
  time.sleep(1)
  print ('''
  a.)saksakin ang tikbalang habang ito ay abala
  b.)tumakbo ng mabilis
  c.)magtago sa mga troso sa gubat ''')  
  choice = input(">>> ")
  if choice in answer_A:
    busaw()
  elif choice in answer_B:
    option_run()
  elif choice in answer_C:
    bata()
  else:
    print (required)
    option_escape2()
    #catch c
def option_escape3():
  print('''sa kakasigaw mo sa gubat unti-unti kanang 
  nawawalan ng lakas at pag asa   ngunit may napansin 
  kang gumalaw sa paligid tila maliliit na mga tao 
  para itong mga...
  Duwende. Ano ang gagawin mo?''')
  print ('''
  a.)mag makaawa sa duwende na tulungan ka makatakas
  b.)ituloy ang pag sigaw  ''')
  time.sleep(1)  
  choice = input(">>> ")
  if choice in answer_A:
    duwende()
  elif choice in answer_B:
    duwende2()
  else:
    print (required)
    option_escape3()

def duwende():
  print('''mababait ang mga duwende kaya naman tinulungan ka nito..
  itinuro sayo ng duwende kung saan ang palabas ng gubathangang doon lang ang kanilang maitutulong
  dahil bawal sa kanilaang tumulong sa tao
  nag lakad ka patungo sa direksyon na tinuro ng duwende ngunit habang ika'y nag lalakbay may nakita kang napakalaking puno..Isang Kapre
  Ano ang gagawin mo?''')
  print ('''
  A.)Iwasan ang daan kung nasaan ang kapre at mag tungo sa kaakit akit na daan
  B.)dumiretso ng tahimik upang hindi mapansin
  C.)tumakbo papalayo ''')  
  time.sleep(1)
  choice = input(">>> ")
  if choice in answer_A:
    kapre()
  elif choice in answer_B:
    print ("\nNakita ka ng kapre at ito ay naging aggresibo. \nPatay Kana!")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  elif choice in answer_C:
    kaprerush()
  else:
    print (required)
    duwende()

def duwende2():
  print('''napansin ka ng duwende kaya naman ikaw ay tinulungan kahit na takot ka sa kanila..
  itinuro ng duwende kung saan ka dapat dumaan para
  ikaw ay   makalabas sa gubat ngunit nag aalangan ka 
  pag katiwalaan ito
  ano ang gagawin mo?''')
  time.sleep(1)
  print ('''
  A.)Sundin ang duwende
  B.)Tumuloy sa mas kaakit akit na daan  ''')  
  choice = input(">>> ")
  if choice in answer_A:
    sirena()
  elif choice in answer_B:
    kapre()
  else:
    print (required)
    duwende2()
    intro()
    #start()
def kapre():
  print('''dumaan ka sa kaakit akit na daan ngunit me nakasalubong kang kapre ano ang gagawin mo?''')
  print('''
  A.)Tumakbo ng mabilis palayo sa kapre
  B.) Mag tungo sa kweba''')
  choice = input(">>> ")
  if choice in answer_A:
    kaprerush()
  elif choice in answer_B:
    kweba()
  else:
    print (required)
    kapre()
def kaprerush():
  print('''nakita ka ng kapre na tumatakbo kaya naman hinabol ka nito.. dahil sa laki nito ano ang gagawin mo?
  ''')
  print('''
  A.)Tumakbo ng mabilis
  B.)Magtago sa kweba''')
  choice = input(">>> ")
  if choice in answer_A:
    print("Sa sobrang laki ng kapre ikaw ay naapakan nito \n Patay kana")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  elif choice in answer_B:
    kweba()
  else:
    print (required)
    kaprerush()
def sirena():
  print('''habang nag lalakbay nakarinig ka ng kaakit akit na boses
  nag mumula sa ,malapit na talon. ito ay mga sirena
  ano ang gagawin mo?''')
  print('''
  A.)Lumapit sa mga sirena upang maki bahagi
  B.)Lumuwis ng daan at magtungo sa kweba
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    print("Kinuha ka ng mga sirena at dinala sa kanilang palasyo at hindi muling nakabalik")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  elif choice in answer_B:
    kweba()
  else:
    print (required)
    kaprerush()
def sirena2():
  print('''Nahulog ka sa bangin at ng kaya mo nang tumayo ay may narinig kang kaakit akit na boses
  nag mumula sa ,malapit na talon. ito ay mga sirena
  ano ang gagawin mo?''')
  print('''
  A.)Lumapit sa mga sirena upang maki bahagi
  B.)Lumuwis ng daan at magtungo sa kweba
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    print("Kinuha ka ng mga sirena at dinala sa kanilang palasyo at hindi muling nakabalik")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  elif choice in answer_B:
    kweba()
  else:
    print (required)
    kaprerush()

def busaw():
  print('''Napatay mo ang tikbalang. Dali-dali ka ngayong umalis sa lugar para bumalik sa iyong 
kumonidad. Pero habang ikaw ay tumatakbo, may naramdaman kang prisensiya na sumusunod saiyo. Ano ang gagawin mo?''')
  time.sleep(1)
  print ('''
  a.) tumigil at tingnan kung sino ang sumusunod
  b.) patuloy lang sa pagtakbo at pabayaan ang sumusunod
  c.) maghanap ng matataguan mula sa mytseryosong prisensiya''')
  choice = input(">>> ")
  if choice in answer_A:
    prisen1()
  elif choice in answer_B:
    prisen2()
  elif choice in answer_C:
    kweba()
  else:
    print (required)
    busaw()

def kweba():
  print ('''\nsa Loob ng kweba madaming kumikinang na bagay sa paligid at may na tatangi ito ay isang kumikinang na espada. \nPupulutin moba? Y/N?''')
  choice = input(">>> ")
  if choice in yes:
    sword = 1
  else:
    sword = 0
  print ("\n Ano ang iyong susunod na gagawin?")
  time.sleep(1)
  print ("A. Dumiretso sa daang itinuro ng duwende \nB. kalabanin ang masamang loob gamit ang espadang kumikinang")
  choice = input(">>> ")
  if choice in answer_A:
    patuloy()
  elif choice in answer_B:
    if sword > 0:
      print ('''\ninangat mo ang espada at ito ay salakayin.. ang espadang ito ay kahinaan ng mga puno kung madikitan nitoang mga masamang loob ay magiging abo..
      nag patuloy ka sa pag hanap ng labasan ng gubat...''')
      time.sleep(1)
      patuloy()
    else: 
      print ("\nDapat kinuha mo ang espeda wala kang dipensa. \n\nPatay kana!")
      time.sleep(1)
      print ("Mag Laro muli? Y/N ")
      ulet= input(">>> ")
      if ulet in yes:
        print('')
        #start()
      else:
        print("Salamat sa Paglalaro")
  else:
    print (required)
    kweba()


def patuloy():
  print('''Patuloy kang nag lakbay upang makalabas sa misteryong gubat ngunit 
  naligaw ka muli hindi mo na makita ang daan na itinuro ng duwendeng tumulong sayo at may nakita kang mga duwende sa punso 
  ano ang gagawin mo?''')
  print('''
  A. Magtanong ng daan palabas ng gubat
  B. hanapin ang daang itinuro ng unang duwende
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    print('''Nagtanong ka sa duwende ngunit hindi ito kasing bait ng unang duwende na tumulong sayo..
    ang kapalit ng kanilang pag tulong ay ang espadang kumikinang
    ibibigay moba?[Y/N]''')
    choice=input(">>>")
    if choice in yes:
      print("sabi ng duwende ay mag tungo ka sa tulay")
      tulay()
  elif choice in answer_B:
    print('''pilit mong hinanap ang daan na tinuro ng unang duwende at nakita mo ito kaya naman nag tungo ka sa tulay''')
    tulay()
  else:
    print (required)
    patuloy()

  

def bata():
  print(''' nagtago ka sa mga troso, umikot ang tikbalang hanggan maalerto sa tunog na mahina pero malinaw na tunog, na parang isang iyak ng sanggol sa loob ng gubat. Pumunta ang tikbalang sa kakaibang tunog at mayang onti ay lumayo rin sa takot. Hindi mo mabuo kung ano at paano matatakot 
  ang isang tikbalang. Paglabas mo ay may isang tiyanak na 
  nakatingin sayo handa nang umatake sayo!!
  Ano ang gagawin mo?''')
  time.sleep(1)
  print('''
  a.) kumuha ng isang malaking sangay at ihampas ang tiyanak
  b.) sumigaw ng malakas para ito ay mabingi.
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    print("natalo mo ang tiyanak at nag lakad ka para mahanap ang labasan")
    duwende2()
  elif choice in answer_B:
    print("nabingi ang tyanak dahil isa sa kahinaan nito ang ingay kaya naman tumakbo ka ng walang alinglangan ngunit ikaw ay nahulog sa bangin")
    time.sleep(1)
    sirena()
  else:
    print (required)
    bata()

def bata1():
  print(''' kumuha ka ng malaking sangyan, at hinampas mo ng 
  malakas ang tiyanak. Tumalsik palayo at nahilo, hindi ka na 
  nagdalawang isip at umalis palayo sa nahilong tiyanak 
  hanggan sa di mo na makita. Nang lumayo ka may Nakita kang 
  isang abandonadong kubo na may mga kalansay na nakakalat sa 
  paligid, sa paglapit mo may suot ito mga damit na pang 
  Espanyol at mga Pilipino. Nang umikot ka sa paligid ng kubo may narinig  kang yapak …
  Hinahabol ka ng Tiyanak''')
  time.sleep(1)
  print('''
  a.) pumasok sa abandonadong kubo.
  b.) Magtungo sa kweba upang mag tago
  c.) Maghanap sa kubo ng isang bagay na makakatulong sayo''')
  choice = input(">>> ")
  if choice in answer_A:
    away1()
  elif choice in answer_B:
    kweba()
  elif choice in answer_C:
    away3()
  else:
    print (required)
    bata1()
def bata2():
  print(''' Sumigaw ka ng malakas, nabingi at nahilo ang tiyanak dahil sa sensitibong pandinig. Lumikas ka palayo sa tiyanak papasok sa gubat nang hindi mo na marinig ang iyak ng tiyanak. Sa paglikas mo dahil sa takot nakarating ka sa 
  daanang nahahati sa tatlo.
  Ano ang gagawin mo?''')
  time.sleep(1)
  print('''
  a.) Mag tungo sa kweba sa bundok
  b.) pumunta sa daanang pababa na may hamog na ulap.
  c.) pumunta sa daan na mas madilim at pahaba.
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    kweba()
  elif choice in answer_B:
    sirena()
  elif choice in answer_C:
    tulay()
  else:
    print (required)
    bata2()
def tulay():
  print('''Habang patuloy ka sa pag hahanap ng labasan sa may narinig kang pagaspas lumingon ka sa paligid kung ano iyon…
  Isang Mananangal
  Ano ang gagawin mo?‘''')
  time.sleep(1)
  print('''
  a.) Tumakbo palayo
  b.) Sa gulat ikaw ay nanginig sa takot at hindi kana nakagalaw''')
  choice = input(">>> ")
  if choice in answer_A:
    print("sa dulo ng tulay ay lumitaw ang sikat ng araw kaya naman ang mananagal ay umalis..\nnakalabas kana ng gubat salamat sa pag lalaro")
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  elif choice in answer_B:
    print("Inatake ka ng mananagal \n patay kana")
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  else:
    print (required)
    tulay()
def away1():
  print('''Nang ikaw ay pumasok sa abandonadong kubo ito pala 
  ay dating maliit na kapilya noong unang panahon. May Nakita 
  kang sagradong kahon na may lamang agwa-bendita ngunit ito ay naka kandado.
  Ano ang gagawin mo''')
  print('''
  a.) sirain ang kahon.
  b.) hanapin ang susi ng lalagyan sa mga kwarto.
  c.) kunin ang pang ipit sa sahig at tangkang buksan ang lalagyan.''')
  choice = input(">>> ")
  if choice in answer_A:
    sirain()
  elif choice in answer_B:
    print('''nakita mo ang susi sa may ilalim ng mesa nabuksan mo at isinaboy mo ang agua bendita sa tiyanak at ito ay nasunog..
    Pagkatapos mo matalo ang tiyanak ay nag tungo ka sa kweba sa bundok upang ipag patuloy ang hinahanap na daan''')
    kweba()
  elif choice in answer_C:
    print("nag tagal ka sa pag bukas ng kahon \n patay kana")
    print ("Mag Laro muli? Y/N ")
    ulet=input(">>> ")
    if ulet in yes:
      intro()
      #start()
  else:
    print (required)
    away1()
def away3():
  print('''habang naghahanap ka ng gamit na panlaban sa 
  tiyanak nakakita ka ng isang lalagyan ng asin na gawa sa 
  kahoy. Nang ini-hagis mo ito sa tiyanak ito ay nasaktan at 
  lumayo sayo, nang umalis ikaw ay tumakbo papalayo dahol sa 
  takot at nahulog ka sa butas na hindi mo inaasahan. nahilo 
  ka dahil sa pagbagsak mo naririnig mo ang tiyanak na 
  tuluyang umalis sa kubo, pero nakakita ka ng isang daanan.
  Ano ang gagawin mo''')
  print(''' 
  a.) lumabas gamit ang daang iyon.
  b.) umakyat sa butas gamit ang mga nasirang kahoy.
  c.) umakyat gamit ang sarili mong kakayahan.''')
  choice = input(">>> ")
  if choice in answer_A:
    sirena()
  elif choice in answer_B:
    tulay()
  elif choice in answer_C:
    print('''Pinili mong bumalik at napansin ka ng tiyanak at 
    ito ay bumalik para atakahin ka.
    patay kana ''')
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    time.sleep(1)
    ulet=input(">>> ")
    if ulet in yes:
      intro()
    else:
      print("Salamat sa Paglalaro")
  else:
    print(required)
    away3()

def prisen1():
  print('''Tumigil ka at tumingin sa iyong kapaligiran, 
  lumamig bigla ang iyong pakiramdam at nakaramdam ka ng 
  matingding takot na parang nagparalisa. Mula sa dilim, 
  isang Busaw ang lumitaw, at gutso ka nitong kainin. Pero ng 
  habang ikaw ay tumakbo sa tikbalang, nasabuyan ka ng asin 
  sa katawan na kinatatakutan ng Busaw, ano ang iyong gagawin''')
  print ('''a.) Hubarin ang damit na mayroong asin at gamitin itong pantaboy sa Busaw
    b.)Takutin mo na ikaw ay nababalutan ng asin
    c.) Gamitin ang iyong patalim na dinala at bantaan ang Busaw''')
  choice = input(">>> ")
  if choice in answer_A:
    busaw1()
  elif choice in answer_B:
    busaw2()
  elif choice in answer_C:
    print('''Ikaw ay naghanap agad ng matataguan na lugar. Ng 
    ika'y makahanap, naramdaman mo na ang prisensiya ay nasa 
    iyong likuran. Bago ka makalingon ay dumilim ang iyong 
    panigin at di mo na naramdaman ang ibang parte ng iyong 
    katawan. Ang ulo mo pala ay napahiwalay sa iyong katawan 
    Namatay Kana''')
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    time.sleep(1)
    ulet=input(">>> ")
    if ulet in yes:
      intro()
    else:
      print("Salamat sa Paglalaro")
  else:
    print(required)
    prisen1()
def prisen2():
  print(''' Patuloy ka sa iyong pagtakbo at hindi mo na pinansin ang prisensiyang sumusunod saiyo. Di mo napansin na ikaw
  ay biglang natapilok at ng ika'y tumayo lumitaw ang isang enkanto, 
  Isang Busaw
  sa iyong harapan, handa kang kainin para mabusog. Natandaan 
  mo ang kahinaan ng Busaw ay asin, na nakadikit sa iyong 
  damit. Ano ang gagawin mo?''')
  time.sleep(1)
  print ('''a.) ipagpag ang asin sa mukha at magtago habang ito ay bulag
    b.) bantaan ang Busaw na ikaw ay natatakpan ng Asin at kapag kinain ka ay mamatay ang Busaw
    c.) Tumayo at tumakbo paalis, inaasahang hindi ka hahabulin dahil ay may Asin ka.''')
  choice = input(">>> ")
  if choice in answer_A:
    busaw1()
  elif choice in answer_B:
    busaw2()
  elif choice in answer_C:
    print('''Binantaan mo ang busaw gamit ang iyong patalim, 
    tumawa ang busaw at ito ay tumalon patungo sayo. 
    Dinaganan ka ng busaw at sinaksaki ka gamit ng Matulis 
    nitong kuko, ngunit dahil sa ikaw ay nababalutan ng Asin, 
    sumigaw sa sakit ang busaw at unti-unting nalusaw ang 
    katawan nito dahil sa asin. /n Parehas kayong namatay.''')
    time.sleep(1)
    print ("Mag Laro muli? Y/N ")
    time.sleep(1)
    ulet=input(">>> ")
    if ulet in yes:
      intro()
    else:
      print("Salamat sa Paglalaro")
  else:
    print (required)
    prisen2()
def busaw1():
  print('''Hinubad mo ang iyong pang-itaas at pinagpag ito malapit sa busaw nakaranas ng matinding sakit. 
  Ano ang susunod mong gagawin habang ang Busaw ay panandaliang bulag''')
  time.sleep(1)
  print ('''
  a.) Gamitin ang patalim na dala-dala at saksakin ang Busaw sa puso.
  b.) Tumakbo palayo at maghanap mag tungo sa daang kaakit akit dahil takot dito ang busaw.
  c.) Pumunta sa kuwebang nakita na di ganong kalayuan''')
  choice = input(">>> ")
  if choice in answer_A:
    print('''Napatay mo ang busaw kaya naman nag tungo ka sa mahabang daan upang makalabas sa gubat''')
    tulay()
  elif choice in answer_B:
    sirena()
  elif choice in answer_C:
    kweba()
  else:
    print (required)
    busaw1()
def busaw2():
  print('''Sinabi mo na nababalutan ka ng Asin. Naging 
  maingat bigla ang busaw at pinahaba nito ang kanyang mga 
  matatalim na kuko para patayin ka ng hindi ka hinahawakan. 
  Nagkaroon ka ng distansya mula sa busaw, ano ang susunod 
  mong gagawin. ''')
  time.sleep(1)
  print ('''
  a.) Balutan ng asin ang patalim na dala mo at bantaan ang busaw.
  b.) Wag alisin ang tingin sa papalapit na busaw at umatraas.
  c.) Kumaripas ng takbo ngayon at mas lalayo ang busaw dahil ikaw ay nababalutan ng asin.''')
  choice = input(">>> ")
  if choice in answer_A:
    print('''natakot ang busaw dahil naamoy nito ang asin
    saiyong damit kaya naman ito ay umali..
    nag tungo ka sa malapit na kweba''')
    kweba()
  elif choice in answer_B:
    print("habang ikaw ay umaatras dmo namalayan na bangin na ang nasalikod mo kaya naman ikaw ay nahulog")
    sirena2()
  elif choice in answer_C:
    kweba()
  else:
    print (required)
    busaw2()
def sirain():
  print('''Sinira mo ang kahon ngunit nabasag ang bote ng 
  agua bendita at me kasama itong patalim na nabasa ng agua 
  bendita..
  sumugod sayo ng mabilis ang tiyanak 
  ano ang iyong gagawin?''')
  time.sleep(1)
  print('''
  A. isaksak sa tyanak ang patalim na nabasa ng agua bendita
  B. sipain ang tiyanak palayo at tumakbo ng mabilis
  ''')
  choice = input(">>> ")
  if choice in answer_A:
    print('''sinaksak mo ang tiyanak gamit ang patalim na may
    agua bendita ito ay epektibo dahil kahinaan ng tiyanak 
    ang agua bendita pagkatapos mo salakayin ang tiyanak nag tungo ka sa tulay upang mag patuloy sa pag lakbay''')
    tulay()
  elif choice in answer_B:
    kweba()
def start():
  list=NAME()
  print("|--------------------------------------------------------------------------------------|")
  print("\t\t\t\t\tIlagay ang pangalan: ")
  nm=input("\t\t\t\t\t\t>>> ")
  list.headval = NameNode(nm)
  print("\t\t\t\tMaglagay muli ng manlalaro? [y/n]:")
  new=input("\t\t\t\t\t>>> ")
  if new == 'y':
    for i in range(5):
        print("\t\t\t\t\tIlagay ang pangalan: ")
        nm=input("\t\t\t\t\t>>> ")
        list.AtEnd(nm)
        print("\t\t\t\tMaglagay muli ng manlalaro? [y/n]: ")
        new=input("\t\t\t\t\t>>> ")
        if new == 'y':
          continue
        else:
          print ("\n\t\t\t\tAng mga Manlalaro: \n")
          time.sleep(1)
          list.listprint()
          time.sleep(1)
          for zx in range (6):
            print("\t\t\t\tSino Ang mag lalaro? : ")
            srch=(input("\t\t\t\t>>>"))
            if list.search(srch):
              print ("|--------------------------------------------------------------------------------------|")
              time.sleep(2)
              print ("\nMaligayang pagdating "+srch)
              time.sleep(1)
              intro()  
              break
            else: 
                print("\t\t\t\t\tWalang'",srch,"'sa talaan")
                continue 
            if zx == 5:
              print('\t\t\t\tLagpas na sa pag ulit\n \t\t\t  Mag Exit...')
              break
  else:
    print ("\n\t\t\t\tAng mga Manlalaro: \n")
    time.sleep(1)
    list.listprint()
    time.sleep(1)
    for zx in range (6):
      if zx == 5:
        print('\t\t\t\t\tLagpas na sa pag ulit\n \t\t\t\t\t  Mag Exit...')
        break
      print("\n\t\t\t\tSino Ang mag lalaro? : ")
      srch=(input("\t\t\t\t>>>"))
      if list.search(srch):
        print ("|--------------------------------------------------------------------------------------|")
        time.sleep(2)
        print ("\nMaligayang pagdating "+srch)
        time.sleep(1)
        intro()  
        break
      else: 
          print("\t\t\t\t\tWalang'",srch,"'sa talaan")
          continue 
  
print ("                                       ,-.")
print("                  ___,---.__          /'|`\          __,---,___")
print("               ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.")
print("             ,'        |           ~'\     /`~           |        `.")
print("            /      ___//              `. ,'          ,  , \___      \ ")
print("           |    ,-'   `-.__   _         |        ,    __,-'   `-.    | ")
print("           |   /          /\_  `   .    |    ,      _/\          \   | ")
print("           \  |           \ \`-.___ \   |   / ___,-'/ /           |  / ")
print("            \  \           | `._   `\\  |  //'   _,' |           /  / ")
print("             `-.\         /'  _ `---'' , . ``---' _  `\         /,-' ")
print("                ``       /     \    ,='/ \`=.    /     \       '' ")
print("                        |__   /|\_,--.,-.--,--._/|\   __| ")
print("                        /  `./  \\`\ |  |  | /,//' \,'  \ ")
print("                       /   /     ||--+--|--+-/-|     \   \ ")
print("                      |   |     /'\_\_\ | /_/_/`\     |   | ")
print("                       \   \__, \_     `~'     _/ .__/   / ")
print("                        `-._,-'   `-._______,-'   `-._,-'")

print("         ::::::::: ::::::::::: ::::::::::: ::::::::::: :::     ::::    ::: ")
print("         :+:    :+:    :+:         :+:         :+:   :+: :+:   :+:+:   :+:  ")
print("         +:+    +:+    +:+         +:+         +:+  +:+   +:+  :+:+:+  +:+   ")
print("         +#++:++#+     +#+         +#+         +#+ +#++:++#++: +#+ +:+ +#+    ")
print("         +#+           +#+         +#+         +#+ +#+     +#+ +#+  +#+#+#    ") 
print("         #+#           #+#         #+#         #+# #+#     #+# #+#   #+#+#    ")  
print("         ###       ########### ###########     ### ###     ### ###    ####    ")   

print("                              ::::    :::  :::::::: ")
print("                              :+:+:   :+: :+:    :+: ")
print("                              :+:+:+  +:+ +:+         ")
print("                              +#+ +:+ +#+ :#:          ")
print("                              +#+  +#+#+# +#+   +#+#   ") 
print("                              #+#   #+#+# #+#    #+#   ")  
print("                              ###    ####  ########    ")   

print(" :::::::::: ::::    ::: :::    :::     :::     ::::    ::: ::::::::::: :::::::: ")
print(" :+:        :+:+:   :+: :+:   :+:    :+: :+:   :+:+:   :+:     :+:    :+:    :+: ")
print(" +:+        :+:+:+  +:+ +:+  +:+    +:+   +:+  :+:+:+  +:+     +:+    +:+    +:+  ")
print(" +#++:++#   +#+ +:+ +#+ +#++:++    +#++:++#++: +#+ +:+ +#+     +#+    +#+    +:+  ")
print(" +#+        +#+  +#+#+# +#+  +#+   +#+     +#+ +#+  +#+#+#     +#+    +#+    +#+   ") 
print(" #+#        #+#   #+#+# #+#   #+#  #+#     #+# #+#   #+#+#     #+#    #+#    #+#   ")  
print(" ########## ###    #### ###    ### ###     ### ###    ####     ###     ########    ")
start()
list = NAME()
time.sleep(2)
