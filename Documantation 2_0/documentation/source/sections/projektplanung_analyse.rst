Projektplanung und Analyse
==========================

Einleitung
----------

Projektumfeld
~~~~~~~~~~~~~

- Ich mache zurzeit eine Umschulung zum Fachinformatiker für Anwendungsentwicklung beim Städtische Berufsschule III Matthäus Runtinger in Regensburg.
- Aktuell absolviere ich meine Ausbildung als Fachinformatiker für Anwendungsentwicklung bei der Firma RIS Web- & Software-Development GmbH & Co. KG in Regensburg, nachfolgend RIS genannt.
- Der Betrieb beschäftigt 13 Mitarbeiter. RIS Development ist ein offizieller Servicepartner der E-Commerce-Software von JTL.
- Neben dem Support für die JTL-Software werden auch individuelle Komponenten für den Webshop oder die Warenwirtschaft (WAWI) entwickelt. Diese reichen vom Erstellen von Template-Vorlagen für Dokumente und Webdesign bis hin zu erweiterten Funktionalitäten in Form von Shop-Plugins.
- Es werden auch individuelle Lösungen für Kunden außerhalb der E-Commerce-Software erstellt. Der Umfang reicht vom Entwickeln von Corporate Designs, Social-Media-Marketing, Neugestaltung des Website-Designs, Erstellung von Web-Applikationen bis hin zur Umsetzung nativer Software.

Projektziel
~~~~~~~~~~~~~

Das Ziel des Projekts ist der Aufbau und die Implementierung eines Backends für RIS. Moderne Technologien wie Django, Laravel oder Node.js werden in Betracht gezogen. Dieses Backend soll folgende Anforderungen erfüllen:

1. **Volle Kontrolle**:
   - Alle Backend-Funktionen sollen feinjustiert werden und unabhängig von allgemeinen Lösungen wie WordPress arbeiten.
   - Die Nutzung von Templates und Plugins, die oft mit Abogebühren verbunden sind, soll vermieden werden.

2. **Verschlankung**:
   - Das Backend soll gezielt auf die spezifischen Bedürfnisse von RIS zugeschnitten werden, um unnötige Funktionen zu vermeiden und die Bedienbarkeit zu vereinfachen.

3. **Effiziente Inhaltspflege**:
   - Die Verwaltung von Inhalten soll ohne die Einschränkungen und Komplexität eines WordPress-Templates erfolgen, wodurch ein direkter und effizienter Arbeitsprozess ermöglicht wird.

4. **Performance**:
   - Die Website soll serverseitig gerendert werden, und die Seiteninhalte sollen vollständig im Cache gespeichert werden, um mit neuer Server-Hardware optimale Ladegeschwindigkeiten zu erreichen.

Ausgangssituation
~~~~~~~~~~~~~~~~~

Die aktuelle Website von RIS Web- & Software-Development GmbH & Co. KG, im Folgenden RIS genannt, basiert auf WordPress und erfüllt ihre grundlegende Funktion. Jedoch sind wir mit WordPress auf allgemeine Lösungen angewiesen, die nicht immer unseren spezifischen Anforderungen entsprechen:

- WordPress erfordert die Nutzung allgemeiner Plugins, die oft nicht an die Anforderungen von RIS angepasst sind.
- WordPress enthält viele Funktionen, die nicht benötigt werden, was unnötigen Overhead beim Lernen und Bedienen verursacht.
- Die Verwaltung von Inhalten in WordPress mit Templating hat sich als umständlich und unvorhersehbar erwiesen.

Abgrenzung des Aufgabenbereichs
-------------------------------

Der Fokus des Projekts liegt auf der Entwicklung des Backends. Frontend-Aufgaben sowie Optimierungen in Bereichen wie Blogs sind nicht Teil des Projekts, da ein Kollege sich um das Frontend kümmern wird. Außerdem werden die Sicherheitsmaßnahmen als Standard angesehen, da nur minimale Daten von den Kunden abgefragt werden (z.B. keine Zahlungsinformationen).

Projektplanung
--------------

Projektphasen
~~~~~~~~~~~~~


- Das Projekt beginnt am 11. November 2024 und endet am 6. Januar 2025, was insgesamt etwa 8 Wochen umfasst. Innerhalb dieses Zeitraums werden die verschiedenen Phasen des Projekts parallel zu den regulären Aufgaben des Unternehmens entwickelt.
- Die projektbezogenen Tätigkeiten werden so geplant, dass die 80 Stunden für das Projekt effizient genutzt werden, um die Ziele fristgerecht zu erreichen.

Grobe Zeitplanung
~~~~~~~~~~~~~

+-------------------------+---------------+
| Projektphase            | Geplante Zeit |
+=========================+===============+
| Projektplanung/Analyse  | 8 h           |
+-------------------------+---------------+
| Entwurf                 | 16 h          |
+-------------------------+---------------+
| Implementierung         | 36 h          |
+-------------------------+---------------+
| Test/Durchführung       | 8 h           |
+-------------------------+---------------+
| Dokumentation           | 8 h           |
+-------------------------+---------------+
| Abnahme                 | 4 h           |
+-------------------------+---------------+
| **Gesamt**              | **80 h**      |
+-------------------------+---------------+

:ref:`detalierter-zeitplanung`

Ressourcenplanung
~~~~~~~~~~~~~

**Software:**

- Framework: Django
- Django Tools: z.B. Pillow
- DB-Software: SQLite für Entwicklung, PostgreSQL für Produktion
- IDE: PyCharm
- Cache-Tools: Redis, Middleware
- Test-Software: PyTest Django, PyTest, FactoryBoy (Testdaten Erstellung), pdoc
- Versionverwaltung: GitLab

**Hardware:**
- Laptop

Analysephase
------------

Auswahl der Technologieplattform
~~~~~~~~~~~~

Für das Projekt wurden moderne Technologien wie Django, Laravel und Node.js in Betracht gezogen, wobei wir uns nach gründlicher Recherche für Django entschieden haben. Dieses Framework bietet robuste und skalierbare Backend-Lösungen und passt ideal zu den Anforderungen unseres Projekts. Ich und der Rest unseres Entwicklungsteams haben bereits umfassende Kenntnisse in Python sowie in JavaScript, HTML und CSS.

**Vorteile von Django**


- **Caching**: Ein flexibles Caching-System unterstützt Technologien wie Middleware Cache und Redis (Backend Cache), was die Anwendungsperformance erheblich steigert.
- **Vollständiges Framework**: Django ist ein „batteries-included“ Framework mit integrierten Funktionen wie Authentifizierung, Administrationsoberflächen und einem leistungsstarken ORM, was die Entwicklung effizienter gestaltet.
- **Große Community und Dokumentation**: Die aktive Community und die umfassende Dokumentation erleichtern die Problemlösung und kontinuierliche Wartung.

In der Entwicklungsphase nutzen wir SQLite wegen seiner Einfachheit und weil es schon by Default in Django konfiguriert ist. In der Produktionsphase setzen wir PostgreSQL ein, um von den erweiterten Funktionen, der Leistung und der Skalierbarkeit zu profitieren, die unser Projekt benötigt.

Ist-Analyse
~~~~~~~~~~~~

- Das Projekt findet im Rahmen der Webentwicklung bei der RIS statt. Ziel ist es, ein neues, maßgeschneidertes Backend für die Unternehmenswebsite zu entwickeln, um die Abhängigkeit von WordPress zu vermeiden.
- Die bestehende Website basiert auf WordPress, was zu Problemen wie unnötigem Overhead, langsamerer Performance und umständlicher Inhaltsverwaltung führt. Die derzeit verwendeten Plugins und Vorlagen entsprechen nicht den spezifischen Anforderungen von RIS.

Wirtschaftlichkeitsanalyse
~~~~~~~~~~~~

Eine klassische Wirtschaftlichkeitsanalyse, inklusive Projektkosten und Amortisationsdauer, 
wurde für dieses Projekt aus folgenden Gründen nicht durchgeführt:

**Ausbildungskontext**
- Projekt im Rahmen der Berufsausbildung
- Fokus auf Kompetenzerwerb statt wirtschaftlichem Nutzen
- Keine zusätzlichen Personal- oder Ausbildungskosten

**Ressourcen und Kosten**
- Nutzung vorhandener Infrastruktur (Hardware/Software)
- Einsatz von Open-Source-Technologien (Django, Python)
- Keine externen Ressourcen oder Lizenzen erforderlich
- Integration in bestehende IT-Systeme

**Projektrahmen**
- Entwicklung durch Auszubildenden
- Teil der regulären Ausbildungszeit
- Keine zusätzlichen Betriebskosten

Die Projektbewertung konzentrierte sich stattdessen auf:

- Technische Umsetzung
- Code-Qualität
- Dokumentation
- Lernerfahrung


Vorgehensmodelle
----------------

Für dieses Projekt wurde das Wasserfallmodell gewählt, da es optimal zu den folgenden Projektbedingungen passt:

- **Klare Zeitplanung**: 

  - Fester Zeitrahmen von 80 Stunden
  - Klar definierte Projektphasen mit zugewiesenen Zeitbudgets

- **Einzelentwickler-Projekt**: 

  - Keine Notwendigkeit für komplexe Team-Koordination
  - Direkte Kontrolle über alle Entwicklungsphasen
  - Vereinfachte Entscheidungsprozesse

- **Vordefinierte Ressourcen**: 

  - Festgelegte technische Infrastruktur
  - Bereits bestimmte Entwicklungswerkzeuge
  - Klare Hardware-Anforderungen

- **Spezifisches Projektziel**: 

  - Eindeutig definierter Funktionsumfang
  - Klare Abgrenzung der Anforderungen
  - Vorhersehbare technische Umsetzung

Diese Rahmenbedingungen ermöglichen eine sequentielle Abarbeitung der Projektphasen, wie sie im Wasserfallmodell vorgesehen ist.


Make or Buy-Entscheidung
------------------------

- Als weborientiertes Entwicklungsunternehmen war die Entscheidung klar, eine fertige Website-Lösung zu kaufen, kam nicht in Frage. Stattdessen haben wir uns dafür entschieden, ein eigenes Backend zu entwickeln, um volle Kontrolle über alle Funktionen und Anpassungen zu haben. Diese Entscheidung geht jedoch über eine einfache Neugestaltung hinaus. Es ging darum, eine Grundlage für eine effiziente, skalierbare und langfristig wartbare Lösung zu schaffen, die den spezifischen Anforderungen von RIS gerecht wird.


Nutzwertanalyse
---------------

+--------------------------------+-----------+----------+----------+----------+
| Kriterium                      | Gewichtung| Django   | Laravel  | Node.js  |
+================================+===========+==========+==========+==========+
| Template-System & Caching      | 30%       | 10 (3.0) | 7 (2.1)  | 6 (1.8)  |
+--------------------------------+-----------+----------+----------+----------+
| Entwicklungsgeschwindigkeit    | 25%       | 9 (2.25) | 8 (2.0)  | 7 (1.75) |
+--------------------------------+-----------+----------+----------+----------+
| Database Integration & ORM     | 25%       | 9 (2.25) | 7 (1.75) | 6 (1.5)  |
+--------------------------------+-----------+----------+----------+----------+
| Skalierbarkeit                 | 20%       | 8 (1.6)  | 7 (1.4)  | 9 (1.8)  |
+--------------------------------+-----------+----------+----------+----------+
| **Gesamtwertung**              | **100%**  | **9.1**  | 7.25     | 6.85     |
+--------------------------------+-----------+----------+----------+----------+


Ergebnis
^^^^^^^^

**Technische Eignung**:

- Besonders stark im Bereich Template-System & Caching
- Ideal für die geforderte serverseitige Renderung

**Teamkompetenz**:

- Vorhandene Python/JavaScript-Expertise außer CSS und HTML im Entwicklungsteam

**Database Integration & ORM**:

- Robustes ORM für komplexe Datenbankstrukturen
- Automatische Migrationen und optimierte Queries

Anwendungsfälle
---------------

**Administratoren können:**

- Inhalt erstellen, bearbeiten und löschen

**Web-Users können:**

- Verschiedene Formulare ausfüllen und schicken
- Web surfen

Für eine visuelle Darstellung der Anwendungsfälle, siehe :ref:`use-case-diagram`.