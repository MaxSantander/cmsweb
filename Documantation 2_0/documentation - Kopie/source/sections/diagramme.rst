Diagramme
=========

Diese Sektion enthält die wichtigsten Diagramme für das Projekt.

.. _use-case-diagram:

Use Case Diagramm
------------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   left to right direction
   skinparam packageStyle rectangle

   actor "Administrator" as admin
   actor "Web-Benutzer" as user

   rectangle "RIS Backend System" {
       usecase "Inhalte erstellen" as UC1
       usecase "Inhalte bearbeiten" as UC2
       usecase "Inhalte löschen" as UC3
       usecase "Formulare ausfüllen" as UC5
       usecase "Website durchsuchen" as UC6
   }

   admin --> UC1
   admin --> UC2
   admin --> UC3
   user --> UC5
   user --> UC6
   @enduml

.. _erd-diagram:

ERD-Diagramm
------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   
   entity "Page" {
       * id: Integer
       * title: String
       * url_path: String
       * content: Text
       * created_at: DateTime
       * updated_at: DateTime
   }

   entity "Block" {
       * id: Integer
       * name: String
       * content: Text
       * type: String
   }

   entity "MenuItem" {
       * id: Integer
       * name: String
       * sorting: Integer
       * parent_id: Integer
   }

   entity "Form" {
       * id: Integer
       * title: String
       * fields: JSON
   }

   Page ||--o{ Block : "contains"
   Page ||--o{ MenuItem : "referenced by"
   MenuItem ||--o{ MenuItem : "parent/child"
   Page ||--o{ Form : "contains"
   @enduml

.. _signal-flow-diagram:

Signalfluss-Diagramm
--------------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   
   actor Benutzer
   participant "pages_app" as App
   participant "Cache-System" as Cache

   Benutzer -> App: Änderung (z. B. Block aktualisieren)
   App -> App: Signal post_save/post_delete
   App -> Cache: Cache leeren
   App -> Benutzer: Bestätigung der Aktualisierung
   @enduml

.. _page-rendering-diagram:

Seiten-Rendering-Diagramm
-------------------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   
   actor Benutzer
   participant "Browser" as Browser
   participant "view" as View
   participant "Cache" as Cache
   participant "Datenbank" as DB

   Browser -> View: Anfrage (z. B. /home)
   View -> Cache: Anfrage an Cache
   Cache -> View: Antwort (falls im Cache)
   View -> DB: Datenbankabfrage (falls nicht im Cache)
   DB -> View: Daten liefern
   View -> Cache: Antwort cachen
   View -> Browser: Antwort rendern
   @enduml

.. _navigation-diagram:

Navigations-Diagramm
-------------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   
   entity "Page" {
       * id: Integer
       * title: String
       * url_path: String
   }

   entity "MenuItem" {
       * id: Integer
       * name: String
       * sorting: Integer
   }

   Page ||--o{ MenuItem : "hat"
   @enduml

.. _mtv-architecture:

MTV-Architektur
---------------

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   skinparam componentStyle uml2

   package "Django MTV Architecture" {
       [Browser] as client
    
       frame "Django Framework" {
           [URL Dispatcher] as urls
           [View] as view
           [Template] as template
           [Model] as model
           database "Database" as db
        
           client --> urls : HTTP Request
           urls --> view : Route Request
           view --> model : Query Data
           model <--> db : CRUD Operations
           view --> template : Context Data
           template --> client : HTTP Response
       }
   }

   note right of view
     Handles business logic
     and data processing
   end note

   note right of model
     Manages data structure
     and database operations
   end note

   note right of template
     Renders HTML with
     dynamic content
   end note
   @enduml