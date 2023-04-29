from django.shortcuts import render
from . import  TripleDES
import wikipedia
import datetime
import matplotlib.pyplot as plt


# import cryptography as crypt
# import pycryptodom


# Create your views here.

def implement_3des(textData):
    print(datetime.datetime.now())
    return TripleDES.TripleDES(textData).getCipher()



def implement_3des_decryption(textData):
    return TripleDES.TripleDES(textData).toNormal()


# def implement_diffe(textData):
# 	return Diffe.Diffe(textData).getCipher()

current_choosen_algorithm = ""
current_text = ""


def home(request):
    if request.method == "POST":
        textData = request.POST["data"]
        choosen_algorithm = request.POST['algorithm']
        current_text = textData
        current_choosen_algorithm = choosen_algorithm
        print(textData, choosen_algorithm)
        cipher_text = ""

        if (choosen_algorithm == "3DES"):
            cipher_text = implement_3des(textData)
        times = getTimes(textData)
        print(times)
        generate_graph(times)
        print(cipher_text)
        # elif(choosen_algorithm=="diffie-hellman"):
        # 	cipher_text=implement_deffe(textData)
        listOfData = getInformationAboutAlgo(textData, cipher_text, choosen_algorithm)
        return render(request, "Output.html",
                      {'textData': listOfData[0], 'cipherText': listOfData[1], 'algo': listOfData[2],
                       'information': listOfData[3], 'decrypt': decryption()})

    return render(request, "homePage.html")


def getTimes(textData):
    dict1 = {"aes": 0, "des": 0, "3des": 0}
    val1 = datetime.datetime.now()
    data = implement_aes(textData)
    dict1["aes"] = (datetime.datetime.now() - val1).microseconds
    method_name(dict1, textData)
    method_nameh(dict1, textData)
    return dict1


def method_nameh(dict1, textData):
    val3 = datetime.datetime.now().microsecond
    data = implement_3des(textData)
    print(datetime.datetime.now(),val3)
    dict1["3des"] = (datetime.datetime.now().microsecond - val3)


def method_name(dict1, textData):
    val3 = datetime.datetime.now().microsecond
    data = implement_des(textData)
    print(datetime.datetime.now(), val3)
    dict1["des"] = (datetime.datetime.now().microsecond - val3)


def decryption():
    textData = current_text
    plaintext = ""
    if (current_choosen_algorithm == "AES"):
        plaintext = implement_aes_decryption(textData)
    elif (current_choosen_algorithm == "DES"):
        plaintext = implement_des_decryption(textData)
    elif (current_choosen_algorithm == "3DES"):
        plaintext = implement_3des_decryption(textData)
    return plaintext


def generate_graph(times):
    plt.title('Time vs algo')
    plt.ylabel('Time in microseconds')
    plt.xlabel('Algorithm')
    X = list(times.keys())
    Y =list(times.values())
    plt.plot(X, Y, color='k', linewidth=3, linestyle='solid', marker='o', markerfacecolor='red', markersize=10,)
    for xy in zip(X, Y):
        plt.annotate(xy, xy=xy)
    plt.savefig("./source/static/output.png")
    plt.close()



def getInformationAboutAlgo(textData, cipher_text, choosen_algorithm):
    # url_to_scrape = "https://www.geeksforgeeks.org/{0}/".format(choosen_algorithm)
    # WantedList = ["https://www.geeksforgeeks.org/advanced-encryption-standard-aes/"]
    #
    # Scraper = AutoScraper()
    # ScrapedData = Scraper.build(url_to_scrape, wanted_list=WantedList)
    # print(ScrapedData)
    map = {"DES": "Data Standard Encryption", "AES": "Advanced Standard Encryption",
           "3DES": "Triple DES"}  # ,"diffie-hellman":"diffie-hellman algorithm"}
    return [textData, cipher_text, choosen_algorithm, refractorData(choosen_algorithm, map)]


def refractorData(choosen_algorithm, map):
    return '.'.join(wikipedia.summary(map[choosen_algorithm]).split('.')[:8])

