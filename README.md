## Slow down or mandat ![Languages count](https://img.shields.io/github/languages/count/Ignatella/slow-down-or-mandat) ![Last commit](https://img.shields.io/github/last-commit/Ignatella/slow-down-or-mandat)

### Autorzy
* Ihnatsi Yermakovich
* Kacper Syrnik
* Piotr Ptak

### Opis i założenia projektu

Założeniem projektu było stworzenie aplikacji rozpoznającej samochodowe tablice rejestracyjne. Do powstania programu wykorzystaliśmy język Python wraz z zależnościami określonymi w pliku requirements.txt. Naszym celem było wykorzystanie operacji na obrazach, w maksymalnym stopniu bazując na rozwiązaniach wykorzystujących różne operacje morfologiczne oraz przekształcenia poznane na zajęciach.

### Sposób uruchomienia

Po sklonowaniu repozytorium znajdującego się się pod tym adresem ([GitHub - Ignatella/slow-down-or-mandat](https://github.com/Ignatella/slow-down-or-mandat)), należy wykonać poniższe komendy:

#### Linux

```plaintext
sudo apt install tesseract-ocr python3-tk
```
#### Windows

```plaintext
winget install UB-Mannheim.TesseractOCR
```
Domyślnie winget instaluje tesseracta w `C:\Program Files\Tesseract-OCR`, którego trzeba dodać do PATH.

A następnie zainstalować zależności wykorzystywane bezpośrednio przez projekt i notebook jupyterowy:

```plaintext
pip install -r requirements.txt
```

W opracowaniu projektu skorzystano m.in. z następujących modułów:

* customtkinter - [customtkinter · PyPI](https://pypi.org/project/customtkinter/)
* pytesseract - [pytesseract · PyPI](https://pypi.org/project/pytesseract/)

Pozostałe zależności są wykorzystywane przez notebook jupyter, który prezentuje podstawowe wykorzystanie algorytmu, którym się inspirowaliśmy:
[OpenCV: Automatic License/Number Plate Recognition (ANPR) with Python - PyImageSearch](https://pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/)

Po zainstalowaniu wszystkich modułów potrzebnych przez program, należy wykonać poniższą komendę (znajdując się równocześnie w katalogu z plikiem app.py):

```python
python3 ./app.py
```

### Interfejs użytkownika oraz sposób użycia

Interfejs użytkownika został opracowany przy wykorzystaniu biblioteki customtkinter, okno programu prezentuje się w sposób następujący (program uruchomiony w WSL2 na systemie Windows 11):
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/8bb0556be5d49b1ee195cef034a05f172b096f532cf9f5b2.png)

Interfejs programu został opracowany w języku angielskim, po lewej stronie znajduje się panel menu, za pomocą którego możemy wykonywać różne operacje, oto opis opcji:
 

* Open file - otwiera jeden plik w formacie .jpg bądź .png,
* Export to csv - eksportuje rezultaty rozpoznawania tablic rejestracyjnych, w formacie csv, przykładowe wyniki poniżej:
  ![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/a5f29d834abecf666b22d25f45a36926f975eb9c4a2db0fd.png)

**Bardzo ważne: aby ta funkcjonalność działała, należy podać nazwę pliku z rozszerzeniem csv**

* Load from directory - ładuje obrazy do analizy (w formacie .jpg, .png), należy zwrócić uwagę na to, żeby nie przekazać katalogu ze zbyt dużą ilością obrazów (10-20 plików), folder ten musi być otworzony, nie wybrany,
* Add to scrollbar - dodaje załadowany obraz do scrollowalnego elementu po stronie prawej, równocześnie aplikując algorytm,
* Remove from scrollbar - usuwa zawartość scrollbara,
* Przyciski strzałek - służą do nawigacji pomiędzy załadowanymi zdjęciami, które zostały umieszczone w scrollbarze,
* Scrollowalny element - pokazuje załadowane zdjęcia wraz z rozpoznanymi numerami rejestracyjnymi (obsługuje zdarzenia kliknięcia).

Przykładowo, po załadowaniu zdjęcia Alfy Romeo MiTo, otrzymamy następujący widok:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/33a66bee8e2fe600f68622428edf34e29704686ccc02934f.png)

Po kliknięciu na przycisk “Add to scrollbar”, otrzymamy:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/2a6c5a39b19262730eb98ec807f652103ace8ffa23c2b3a6.png)

Natomiast po kliknięciu przycisku “Remove from scrollbar”:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/6fee5173892183591c62926b10d8e3a820093c21ea1b97f7.png)

Poniżej zaprezentowano rezultat działania załadowania z poziomu katalogu:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/81c3f0cea5d4287e24c6148fd74ac1b4d7c8d2fc0fefbebe.png)

Klikając jednokrotnie przycisk “prawa strzałka” zostaniemy przeniesieni do pierwszego ze zdjęć:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/b7991e7d885e89f671aa4e38df100037e824dbe035e3c348.png)

Klikając na ścieżkę do pliku wraz z rezultatem zostaniemy przeniesieni do odpowiedniego ze zdjęć wraz z wynikiem działania algorytmu:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/63a828af4a10e0c681e80cbd624053eec8fb51301d584877.png)

Interfejs użytkownika po zmianie motywu na jasny prezentuje się następująco:
![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/78a6faa6ca9c5c5b146fd29afa3cc9f5d8cef89a8e1e732e.png)

### Opis użytego algorytmu

Wykorzystany algorytm składa się z 2 etapów, w pierwszym (najważniejszym) etapie wykorzystujemy tylko i wyłącznie operacje na obrazach, w celu znalezienia odpowiedniego kandydata na tablicę rejestracyjną, a następnie wywołujemy odpowiednią metodę z modułu (pytesseract), która z rozpoznanego tekstu na zdjęciu zwróci odpowiedni napis, przykładowy rezultat z etapu 1. wraz ze zrzutami ekranu 

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/5cacd7ea49cdb7aa77049af36e366976c9a280094e699263.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/e4ef228c1004b8c6209047201ec9714fa9766543040cc940.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/278a68b0786320f412ba3b9fb82959153f1c7001d15b2321.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/14518dbefbce0658b404a16be72924ffe7f0debd55ec1c07.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/261c45af14f95f4eb3fb510406e2da372a04117a4e78729a.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/0444a260479e651db1995174f550a0c0e57ccffe404fa23c.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/55ea7c144a73a487db37bea687edf3afbdddcd22fa296298.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/580e8c967e82ce6d6e4a6d0b36d8b050d658002a0e28b435.png)

![](https://33333.cdn.cke-cs.com/kSW7V9NHUXugvhoQeFaf/images/26cada5990926abd607eb2b235f438db525824c12713c40b.png)

Bardzo często zdarza się, że algorytm z etapu pierwszego zwraca prawidłowe rezultaty, natomiast ocr rozpoznaje tekst niepoprawnie, dlatego umieściliśmy w folderze algorithm notebook jupyter z kodem algorytmu w wersji pierwotnej (rozpatrującą pierwszego znalezionego kandydata).

### Podział pracy

Prace wykonywaliśmy z podziałem na część interfejsu użytkownika oraz algorytmu niezależnie od siebie, następnie oba rozwiązania zostały połączone. W celu konsultacji oraz weryfikacji postępów realizacji projektu komunikowaliśmy się za pośrednictwem różnych komunikatorów. Staraliśmy się aby rozłożenie pracy było w miarę możliwości równomierne.  

### Niekompletne/niedziałające funkcjonalności

* Rozpoznawanie tekstu zastosowane w zadaniu nie daje zawsze dobrych rezultatów, dla zdecydowanej większości załączonych w katalogu “test\_images” zdjęć tablice zostają rozpoznane poprawnie, bądź dają rezultat zbliżony do właściwego. Wykorzystane zdjęcia pochodzą z Internetu. 
* W trakcie realizacji projektu skorzystaliśmy również z keras\_ocr, jednak rezultaty rozponawania tekstu nie były satysfakcjonujące, dlatego pozostaliśmy przy tesseract mimo istniejących niedoskonałości.
* Algorytm działa dla tablic o stosunku (width x height) pomiędzy 3.5 a 4.7 (nie zadziała dla tablic o innym stosunku).
* Ładowanie bardzo dużej ilości obrazów do pliku za pomocą funkcjonalności “Load from directory” jest niemożliwe - program ulega zatrzymaniu.
* Program obsługuje tylko rozszerzenia jpg oraz png.