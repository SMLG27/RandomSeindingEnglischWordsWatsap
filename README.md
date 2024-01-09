WhatsApp Spam

Programmübersicht
Dieses Python-Skript nutzt pyautogui, nltk und pyperclip Bibliotheken, um zufällige Wörter aus einem Wörterbuch zu generieren und diese automatisiert als Textnachrichten zu versenden. Es ist im Wesentlichen ein automatisierter Textgenerator und -sender, oft als "Spam-Bot" bezeichnet.

Funktionsweise
Wörterbuch Laden: Das Programm lädt zuerst eine Liste von Wörtern aus dem nltk.corpus.words-Wörterbuch, das etwa 236.736 Wörter enthält.

Zufällige Wortauswahl und Nachrichtengenerierung:

Die Funktion spammm nimmt eine Zahl (how_much) entgegen, die bestimmt, wie viele Wörter zufällig aus der Wörterliste ausgewählt werden sollen. Diese Wörter werden zu einer Nachricht zusammengesetzt.
Die Funktion convert wandelt die Liste von Wörtern in einen einzigen String um, der dann als Nachricht verwendet wird.
Automatisiertes Senden von Nachrichten:

Die Nachrichten werden mit Hilfe von pyautogui automatisch in das aktuell aktive Textfeld des geöffneten Fensters eingefügt.
Die Funktion _workaround_write ist ein Workaround für einen bekannten Bug in pyautogui.write() bei der Verwendung von nicht-QWERTZ-Tastaturen. Sie kopiert den Text in die Zwischenablage und fügt ihn dann ein, anstatt ihn zu tippen.
Das Programm sendet bis zu 2000 Zeilen mit zufällig generierten Wortkombinationen, wobei jede Zeile bis zu 10 Wörter enthalten kann.
Anwendungszweck
Das Skript kann für verschiedene Zwecke eingesetzt werden, wie beispielsweise für das Testen der Reaktionsfähigkeit von Chat-Anwendungen unter hoher Last oder für das automatische Ausfüllen von Textfeldern in Testszenarien. Es ist jedoch wichtig zu beachten, dass der Einsatz als "Spam-Bot" in vielen Kontexten unethisch oder sogar rechtlich problematisch sein kann.

Abhängigkeiten
pyautogui: Für die Automatisierung der Tastatur- und Mausinteraktionen.
nltk: Für den Zugriff auf eine umfangreiche Wortliste.
pyperclip: Für den Umgang mit der Zwischenablage, um den Workaround für pyautogui zu ermöglichen.
Wichtige Hinweise
Das Skript sollte verantwortungsvoll und ethisch verwendet werden. Es sollte vermieden werden, es für störende oder schädliche Zwecke einzusetzen.
Der Benutzer muss sicherstellen, dass das richtige Textfeld im Fokus ist, bevor das Skript ausgeführt wird, da pyautogui automatisch im aktuell aktiven Fenster arbeitet.


So starten Sie das Skript:
Um das Skript zu verwenden, müssen Sie zunächst die erforderlichen Bibliotheken installieren (pyautogui, nltk und pyperclip) und dann das Skript über einen Python-Interpreter ausführen.

pip install pyautogui nltk pyperclip
python <Skriptname>.py
