1. Einleitung
=============

Projektumfeld
-------------

* Ich mache zurzeit eine Umschulung zum Fachinformatiker für Anwendungsentwicklung beim Städtische Berufsschule III Matthäus Runtinger in Regensburg.

* Aktuell absolviere ich meine Ausbildung als Fachinformatiker für Anwendungsentwicklung bei der Firma RIS Web- & Software-Development GmbH & Co. KG in Regensburg, nachfolgend **RIS** genannt.

* Der Betrieb beschäftigt 13 Mitarbeiter. RIS Development ist ein offizieller Servicepartner der E-Commerce-Software von **JTL**.

* Neben dem Support für die JTL-Software werden auch individuelle Komponenten für den Webshop oder die Warenwirtschaft (WAWI) entwickelt. Diese reichen vom Erstellen von Template-Vorlagen für Dokumente und Webdesign bis hin zu erweiterten Funktionalitäten in Form von Shop-Plugins.

* Es werden auch individuelle Lösungen für Kunden außerhalb der E-Commerce-Software erstellt. Der Umfang reicht vom Entwickeln von Corporate Designs, Social-Media-Marketing, Neugestaltung des Website-Designs, Erstellung von Web-Applikationen bis hin zur Umsetzung nativer Software.

Projektziel
-----------

Das Ziel des Projekts ist der Aufbau und die Implementierung eines Backends für RIS. Moderne Technologien wie **Django**, **Laravel** oder **Node.js** werden in Betracht gezogen. Dieses Backend soll folgende Anforderungen erfüllen:

* **Volle Kontrolle**: Alle Backend-Funktionen sollen feinjustiert werden und unabhängig von allgemeinen Lösungen wie WordPress arbeiten. Die Nutzung von Templates und Plugins, die oft mit Abogebühren verbunden sind, soll vermieden werden.

* **Verschlankung**: Das Backend soll gezielt auf die spezifischen Bedürfnisse von RIS zugeschnitten werden, um unnötige Funktionen zu vermeiden und die Bedienbarkeit zu vereinfachen.

* **Effiziente Inhaltspflege**: Die Verwaltung von Inhalten soll ohne die Einschränkungen und Komplexität eines WordPress-Templates erfolgen, wodurch ein direkter und effizienter Arbeitsprozess ermöglicht wird.

* **Performance**: Die Website soll serverseitig gerendert werden, und die Seiteninhalte sollen vollständig im Cache gespeichert werden, um mit neuer Server-Hardware optimale Ladegeschwindigkeiten zu erreichen.

Ausgangssituation
-----------------

Die aktuelle Website von RIS Web- & Software-Development GmbH & Co. KG, im Folgenden RIS genannt, basiert auf WordPress und erfüllt ihre grundlegende Funktion. Jedoch sind wir mit WordPress auf allgemeine Lösungen angewiesen, die nicht immer unseren spezifischen Anforderungen entsprechen:

* WordPress erfordert die Nutzung allgemeiner Plugins, die oft nicht an die Anforderungen von RIS angepasst sind.

* WordPress enthält viele Funktionen, die nicht benötigt werden, was unnötigen Overhead beim Lernen und Bedienen verursacht.

* Die Verwaltung von Inhalten in WordPress mit Templating hat sich als umständlich und unvorhersehbar erwiesen.

Abgrenzung des Aufgabenbereichs
-------------------------------

Der Fokus des Projekts liegt auf der Entwicklung des **Backends**. Frontend-Aufgaben sowie Optimierungen in Bereichen wie Blogs sind **nicht** Teil des Projekts, da ein Kollege sich um das Frontend kümmern wird. Außerdem werden die Sicherheitsmaßnahmen als Standard angesehen, da nur minimale Daten von den Kunden abgefragt werden (z.B. keine Zahlungsinformationen).

2. Projektplanung
=================

Projektphasen
-------------

* Das Projekt beginnt am **11. November 2024** und endet am **6. Januar 2025**, was insgesamt etwa **8 Wochen** umfasst. Innerhalb dieses Zeitraums werden die verschiedenen Phasen des Projekts parallel zu den regulären Aufgaben des Unternehmens entwickelt.

* Die projektbezogenen Tätigkeiten werden so geplant, dass die **80 Stunden** für das Projekt effizient genutzt werden, um die Ziele fristgerecht zu erreichen.

Grobe Zeitplanung
-----------------

===============  ================
**Projektphase**     **Geplante Zeit**
===============  ================
Projektplanung/Analyse    8 h
Entwurf                   16 h
Implementierung           36 h
Test/Durchführung         8 h
Dokumentation             8 h
Abnahme                   4 h
**Gesamt**                **80 h**
===============  ================

*Tabelle 1: Grobe Zeitplanung*

Auswahl der Technologieplattform
--------------------------------

Für das Projekt wurden moderne Technologien wie **Django**, **Laravel** und **Node.js** in Betracht gezogen, wobei wir uns nach gründlicher Recherche für **Django** entschieden haben. Dieses Framework bietet robuste und skalierbare Backend-Lösungen und passt ideal zu den Anforderungen unseres Projekts. Ich und der Rest unseres Entwicklungsteams haben bereits umfassende Kenntnisse in **Python** sowie in **JavaScript**, **HTML** und **CSS**.

**Vorteile von Django:**

* **Caching**: Ein flexibles Caching-System unterstützt Technologien wie Middleware Cache und Redis (Backend Cache), was die Anwendungsperformance erheblich steigert.

* **Vollständiges Framework**: Django ist ein „batteries-included“ Framework mit integrierten Funktionen wie Authentifizierung, Administrationsoberflächen und einem leistungsstarken ORM, was die Entwicklung effizienter gestaltet.

* **Große Community und Dokumentation**: Die aktive Community und die umfassende Dokumentation erleichtern die Problemlösung und kontinuierliche Wartung.

In der Entwicklungsphase nutzen wir **SQLite** wegen seiner Einfachheit und weil es standardmäßig in Django konfiguriert ist. In der Produktionsphase setzen wir **PostgreSQL** ein, um von den erweiterten Funktionen, der Leistung und der Skalierbarkeit zu profitieren, die unser Projekt benötigt.

Abweichungen vom Projektantrag
------------------------------

* Stimmen wir:

  * die Zeitplanung?

  * Inhalt und Gliederung?

  * DB- und Cache-Technologien bzw. Architekturen?

Ressourcenplanung
-----------------

**Software:**

* Framework: **Django**

* Django Tools: z.B. **Pillow**

* **DB-Software**: SQLite für Entwicklung, PostgreSQL für Produktion

* **IDE**: PyCharm

* **Cache-Tools**: Redis, Middleware

* **Test-Software**: Django selbst, optional PyTest, FactoryBoy

* **Server**: *Wird noch entschieden*

**Hardware:**

* **Laptop**

Vorgehensmodelle
----------------

* Wie z.B. **Wasserfallmodell** oder das fortgeschrittene **Spiralmodell**? Nicht notwendig, haben wir gesagt, aber...

  * Erlaubt kontinuierliche Kontrolle und Verbesserungen, weil die Phasen nicht streng aufeinander folgen wie beim Wasserfallmodell und würde daher besser passen, um sicherer zu gehen.

Analysephase
============

Ist-Analyse
-----------

* Das Projekt findet im Rahmen der Webentwicklung bei RIS statt. Ziel ist es, ein neues, maßgeschneidertes Backend für die Unternehmenswebsite zu entwickeln, um die Abhängigkeit von WordPress zu vermeiden.

* Die bestehende Website basiert auf WordPress, was zu Problemen wie unnötigem Overhead, langsamerer Performance und umständlicher Inhaltsverwaltung führt. Die derzeit verwendeten Plugins und Vorlagen entsprechen nicht den spezifischen Anforderungen von RIS.

* **Was gilt es zu erstellen/verbessern?**

Wirtschaftlichkeitsanalyse
--------------------------

* Das Thema **Projektkosten** bleibt offen.

Make-or-Buy-Entscheidung
------------------------

* Als weborientiertes Entwicklungsunternehmen war die Entscheidung klar, eine fertige Website-Lösung zu kaufen, kam nicht in Frage. Stattdessen haben wir uns dafür entschieden, ein eigenes Backend zu entwickeln, um volle Kontrolle über alle Funktionen und Anpassungen zu haben.

Diese Entscheidung geht jedoch über eine einfache Neugestaltung hinaus. Es ging darum, eine Grundlage für eine effiziente, skalierbare und langfristig wartbare Lösung zu schaffen, die den spezifischen Anforderungen von RIS gerecht wird!

Projektkosten
-------------

* **Entwicklung, Schulung, Wartung?**

* **Server** gehört auch dazu?

Amortisationsdauer
------------------

* Haben wir Lizenzkosten oder irgendwelche andere mit WordPress?

Nutzwertanalyse
---------------

**Nutzwertanalyse**

Kriterium                      | Gewichtung | Django (Punkte) | Laravel (Punkte) | Node.js (Punkte)
-------------------------------|------------|-----------------|------------------|-----------------
Template-System & Caching      | 30%        | 10 (3.0)        | 7 (2.1)          | 6 (1.8)
Entwicklungsgeschwindigkeit    | 25%        | 9 (2.25)        | 8 (2.0)          | 7 (1.75)
Database Integration & ORM     | 25%        | 9 (2.25)        | 7 (1.75)         | 6 (1.5)
Skalierbarkeit                 | 20%        | 8 (1.6)         | 7 (1.4)          | 9 (1.8)
**Gesamtwertung**              | **100%**   | **9.1**         | **7.25**         | **6.85**

**Ergebnis:**

Basierend auf den vorgegebenen Anforderungen und unter Berücksichtigung der Projektarbeit ist **Django** die optimale Wahl aus folgenden Gründen:

* **Technische Eignung**

  * Besonders stark im Bereich Template-System & Caching

  * Ideal für die geforderte serverseitige Renderung

* **Teamkompetenz**

  * Vorhandene Python/JavaScript-Expertise sowie CSS und HTML im Entwicklungsteam

* **Database Integration & ORM**

  * Robustes ORM für komplexe Datenbankstrukturen

  * Automatische Migrationen und optimierte Queries

Im Laufe der Nutzung habe ich festgestellt, dass es besser wäre, von Anfang an **PostgreSQL** anstelle von SQLite zu verwenden. Unterschiedliche Umgebungen können zu Problemen führen, insbesondere wenn wir später auf PostgreSQL migrieren müssen.

**Gründe:**

1. **Konsistente Entwicklung**

   * Einheitliche Umgebungen

   * Frühes Erkennen von Datenbankproblemen

   * Vermeidung von Migrationsüberraschungen

2. **Projektanforderungen**

   * Unterstützung mehrsprachiger Inhalte

   * Möglichkeit komplexer Datenbankabfragen

   * Leistungsoptimierung

   * Integration von Caching

3. **Technische Vorteile**

   * Verbesserte Indizierung

   * Transaktionssicherheit

   * Unterstützung gleichzeitiger Zugriffe

   * Volltextsuche

Für die Entwicklung und den Produktivbetrieb setzen wir **PostgreSQL** ein. Diese Entscheidung gewährleistet eine konsistente Umgebung während des gesamten Entwicklungszyklus und ermöglicht die optimale Nutzung fortschrittlicher Datenbankfunktionen für unsere mehrsprachige Content-Management-Lösung.

Anwendungsfälle
---------------

**Administratoren** können:

* Inhalt erstellen, bearbeiten und löschen

* Eingegebene Formulare per E-Mail erhalten

* Django Signals per E-Mail bekommen

**Web-User** können:

* Verschiedene Formulare ausfüllen und abschicken

* Auf der Website surfen

Use-Case-Diagramm:
// ...Einfügen des Use-Case-Diagramms...

Qualitätsanforderungen nach ISO/IEC 9126-1
------------------------------------------

* **Funktionalität**: Mehrsprachigkeit (DE/EN), Cache-Management

* **Performance**: Ladezeit < 2 Sekunden, serverseitiges Rendering, Redis Caching implementiert

* **Wartbarkeit**: Dokumentierter Code, modulare Architektur, automatisierte Tests

* **Usability**: Admin-Interface

* **Effizienz**: Optimiertes Caching-System, minimierte Datenbankzugriffe, reduzierte Serverauslastung

Lastenheft/Fachkonzept
----------------------

* Funktionen des Programms (Muss/Soll/Wunsch), Benutzerrollen

Entwurfsphase
=============

Zielplattform
-------------

* **Kriterien zur Auswahl der Zielplattform**

Architekturdesign
-----------------

* Beschreibung und Begründung der gewählten Anwendungsarchitektur (MVC).

Entwurf der Benutzeroberfläche
------------------------------

* Notwendig in meinem Fall?

Datenmodell
-----------

* Das ER-Modell des Website-Backends besteht aus 3 Hauptentitäten:

**Page (Seite)**

* Zentrale Entität für Webseiteninhalte

* Speichert mehrsprachige Inhalte (DE/EN)

* Verwaltet Meta-Informationen

**Block (Inhaltsblock)**

* Enthält Template-basierte Inhaltsblöcke

* Sortierbare Komponenten

* Wiederverwendbare Strukturen

**MenuItem (Menüinhalt)**

* Verwaltet Navigationsstrukturen

* Template-basierte Menüelemente

* Sortierbare Menükomponenten

Beziehungen:

* **Page** (n) hat **Block** (m)

* **Page** (1) hat **MenuItem** (0..1)

Diese Struktur ermöglicht:

* Flexible Seitenerstellung

* Wiederverwendbare Komponenten

* Mehrsprachige Inhalte

* Geordnete Navigation

**Beispielcode:**

.. code-block:: python

   from django.db import models

   class Page(models.Model):
       title = models.CharField(max_length=255)
       url_path = models.CharField(max_length=2048)
       language = models.CharField(
           max_length=2,
           choices=[('EN', 'English'), ('DE', 'Deutsch')],
           default='DE',
       )
       meta_description = models.TextField(blank=True, null=True)
       meta_keywords = models.CharField(max_length=255, blank=True, null=True)
       is_published = models.BooleanField(default=False)
       published_at = models.DateTimeField(blank=True, null=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

   class Block(models.Model):
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

   class MenuItem(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       template = models.TextField()
       sorting = models.IntegerField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

   class PageBlock(models.Model):
       page = models.ForeignKey('Page', on_delete=models.CASCADE)
       block = models.ForeignKey('Block', on_delete=models.CASCADE)

       class Meta:
           unique_together = (('page', 'block'),)
