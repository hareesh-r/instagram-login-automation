#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import time

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')

driver.implicitly_wait(300)

time.sleep(10)

messageList = ['Tamil:- Iniya Pirandha naal nal vaazhuthukal en chellamay','Albanian: “Gëzuar ditëlindjen”','Bosnian: “Sretan rođendan”','Bulgarian: “Chestit Rozhden den”','Catalan: “Per molts anys”','Cheinese: “Shēngrì kuàilè”','Czech: “Všechno nejlepší k narozeninám”','Danish: “Tillykke med fødselsdagen”','Dutch: Fijne verjaardag”','Filipino: “Maligayang kaarawan”','Finnish: “Hyvää syntymäpäivää”','French: “Bon anniversaire”','Galician: “Feliz Aniversario”','German: “Alles Gute zum Geburtstag”','Greek: “Charoúmena genéthlia”','Hebrew: “יום הולדת שמח”','Hungarian: “Boldog születésnapot”','Icelandic: “Til hamingju með afmælið”','Igbo: “Ezi ncheta ọmụmụ”','Indonesian: “Selamat ulang tahun”','Irish: “Lá breithe shona duit”','Italian: “Buon compleanno”','Japanese: “お誕生日おめでとうございます”','Kazakh: “Twğan küniñ quttı bolsın”','Khmer: “Rikreay​ thngai​ kamnaet”','Korean: “Saeng-il chugha”','Kurdish: “Rojbûna te pîroz be”','Latin: “Felix natalis”','Lithuanian: “Su gimtadieniu”','Luxembourgish: “Alles Guddes fir däi Gebuertsdag”','Malay: “Selamat Hari lahir”','Mongolian: “Төрсөн өдрийн мэнд”','Nepali: “Janmadinakō”','Norwegian: “Gratulerer med dagen”','Polish: “Wszystkiego najlepszego”','Portuguese: “Feliz Aniversário”','Romanian: “La multi ani”','Russian: “S dnem ​​rozhdeniya”','Serbian: “Srećan rođendan”','Slovenian: “Vse najboljše”','Somali: “Dhalasho Wacan”','Spanish: “Feliz cumpleaños”','Swahili: “Siku ya kuzaliwa ya furaha”','Swedish: “Grattis på födelsedagen”','Tai: “S̄uk̄hs̄ạnt̒ wạn keid”','Turkish: “Doğum günün kutlu olsun”','Ukranian: “Z Dnem narodzhennya”','Vietnamese: “Chúc mừng sinh nhật”','Welsh: Penblwydd hapus”','Zulu: “Usuku olumnandi lokuzalwa','Spanish — ¡Feliz cumpleaños!','French — Bon anniversaire !','German — Alles Gute zum Geburtstag!','Italian — Buon compleanno!','Portuguese — Feliz aniversário!','Swedish — Grattis på födelsedagen!','Russian — С Днём рождения!','Indonesian — Selamat ulang tahun!','Dutch — Gefeliciteerd met je verjaardag!','Norwegian — Gratulerer med dagen!','Polish — Wszystkiego najlepszego!','Turkish — Doğum günün kutlu olsun!','Danish — Tillykke med fødselsdagen!','Afrikaans:- Gelukkige verjaarsdag!', 'Albanian:- Gëzuar ditëlindjen!', 'Amharic:- melikami lideti!', 'Arabic:- eid milad saeid!', 'Armenian:- Tsnundd shnorhavor!', 'Azerbaijani:- Ad günün mübarək!', 'Bangla:- Śubha janmadina!', 'Basque:- Zorionak!', 'Belarusian:- Z Dniom Naradžennia!', 'Bosnian:- Sretan rođendan!', 'Bulgarian:- Chestit Rozhden den!', 'Burmese:- pyawrwin hpwalrar mwaynae!', 'Catalan:- Feliç aniversari!', 'Cebuano:- Malipayong adlawng natawhan!', 'Chinese:- Shēngrì kuàilè!', 'Corsican:- Felice Anniversariu!', 'Croatian:- Sretan rođendan!', 'Czech:- Všechno nejlepší k narozeninám!', 'Danish:- Tillykke med fødselsdagen!', 'Dutch:- Gelukkige verjaardag!', 'Esperanto:- Feliĉan naskiĝtagon!', 'Estonian:- Palju õnne sünnipäevaks!', 'Filipino:- Maligayang kaarawan!', 'Finnish:- Hyvää syntymäpäivää!', 'French:- Joyeux anniversaire!', 'Galician:- Feliz Aniversario!', 'Georgian:- Გilotsav dabadebis dghes!', 'German:- Alles Gute zum Geburtstag!', 'Greek:- Charoúmena genéthlia!', 'Gujarati:- Janmadivasa ni subhakamana!', 'Haitian Creole:- Bòn fèt!', 'Hausa:- Barka da ranar haihuwa!', 'Hawaiian:- Hau oli La Hanau!', 'Hindi:- janmadin mubaarak!', 'Hmong:- Zoo siab hnub yug!', 'Hungarian:- Boldog születésnapot!', 'Icelandic:- Til hamingju með afmælið!', 'Igbo:- Ezi ncheta ọmụmụ!', 'Indonesian:- Selamat ulang tahun!', 'Irish:- Lá breithe shona duit!', 'Italian:- Buon compleanno!', 'Japanese:- Otanjōbiomedetōgozaimasu!', 'Javanese:- Sugeng tanggap warsa!', 'Kannada:- Janmadinada subhasayagalu!', 'Kazakh:- Twğan küniñ quttı bolsın!', 'Khmer:- rikreay\u200b thngai\u200b kamnaet!', 'Kinyarwanda:- Isabukuru nziza!', 'Korean:- saeng-il chugha haeyo!', 'Kurdish:- Rojbûna te pîroz be!', 'Kyrgyz:- Tuulgan kunuŋuz menen kuttuktaym!', 'Lao:- suk san van koed!', 'Latvian:- Daudz laimes dzimsanas diena!', 'Lithuanian:- Su gimtadieniu!', 'Luxembourgish:- Alles Guddes fir de Gebuertsdag!', 'Macedonian:- Sreḱen rodenden!', 'Malagasy:- Tratry ny tsingerintaona nahaterahana!', 'Malay:- Selamat Hari lahir!', 'Malayalam:- janmadinasansakal!', 'Maori:- Kia ra whanau!', 'Marathi:- Vadhadivasacya hardika subheccha!', 'Mongolian:- Törsön ödriin mend!', 'Nepali:- Janmadinako subhakamana!', 'Norwegian:- Gratulerer med dagen!', 'Nyanja:- Tsiku labwino lobadwa!', 'Persian:- تولدت مبارک!', 'Polish:- Wszystkiego najlepszego z okazji urodzin!', 'Portugese:- Feliz Aniversario!', 'Punjabi:- Janamadina mubaraka!', 'Romanian:- La multi ani!', 'Russian:- S dnem \u200b\u200brozhdeniya!', 'Samoan:- Manuia le aso fanau!', 'Scottish Gaelic:- Co-là-breith math!', 'Serbian:- Srećan rođendan!', 'Shona:- Bhavhadhe rinofadza!', 'Sinhala:- suba upandinayak vevz!', 'Slovak:- Šťastné narodeniny!', 'Slovenian:- Vse najboljše!', 'Somali:- Dhalasho Wacan!', 'Southern Sotho:- Letsatsi le monate la tsoalo!', 'Spanish:- ¡Feliz cumpleaños!', 'Sundanese:- Wilujeung tepang taun!', 'Swahili:- Heri ya siku ya kuzaliwa!', 'Swedish:- Grattis på födelsedagen!', 'Tagalog:- Maligayang kaarawan!', 'Tajik:- Zodrūz muʙorak!',  'Tatar:- Туган көн белән!', 'Telugu:- Puttinaroju subhzkznkṣalu!', 'Thai:- S̄uk̄hs̄ạnt̒ wạn keid!', 'Turkish:- İyi ki doğdun!', 'Turkmen:- Doglan günüň bilen!', 'Ukranian:- Z Dnem Narodzhennya!', "Uzbek:- Tug'ilgan kuning bilan!", 'Vietnamese:- Chúc mừng sinh nhật!', 'Welsh:- Penblwydd hapus!', 'Western Frisian:- Lokkige jierdei!', 'Xhosa:- Usuku lokuzalwa olumnandi!', 'Yiddish:- mzl deyn geburstog!', 'Yoruba:- O ku ojo ibi!', 'Zulu:- Usuku olumnandi lokuzalwa']

def login():
    
    try:

        searchBox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')

        searchBox.send_keys(r'pappu')

        print('login successful')

        time.wait(6)

        driver.implicitly_wait(10)

        chat = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[15]/div/div/div[2]/div[1]/div[1]')

        chat.click()

        print('chat opened')

        time.wait(6)

        messageBox = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

        messageBox.send_keys('Good Morning')

        print('message typed')

        time.wait(6)

    except:

        print("error occured while login")


login()

