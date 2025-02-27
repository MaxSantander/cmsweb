Database Schema
==============

Model Overview
-------------
The RIS-Web Backend uses several interconnected models to manage content and navigation. Below is a diagram showing the relationships between these models.

.. uml::

   @startuml
   skinparam monochrome true
   skinparam shadowing false
   
   abstract class TimestampedModel {
       +created_at: DateTimeField
       +updated_at: DateTimeField
   }
   
   class Page {
       +title: CharField(255)
       +url_path: CharField(2048)
       +name: CharField(100)
       +language: CharField(2)
       +meta_description: TextField
       +meta_keywords: CharField(255)
       +published_at: DateTimeField
       +is_published(): boolean
       +publish()
       +unpublish()
   }
   
   class Block {
       +template: TextField
       +sorting: IntegerField
       +name: CharField(100)
       +image: ImageField
       +get_image_url(): string
   }
   
   class MenuItem {
       +page: ForeignKey(Page)
       +name: CharField(100)
       +template: TextField
       +sorting: IntegerField
   }

   TimestampedModel <|-- Page
   TimestampedModel <|-- Block
   TimestampedModel <|-- MenuItem
   Page "1" <-- "*" MenuItem
   
   @enduml

Model Details
------------

Page Model
~~~~~~~~~
The Page model is the core content type, managing multilingual pages with SEO capabilities and publication workflow.

Block Model
~~~~~~~~~~
Blocks represent reusable content components that can be positioned within pages.

MenuItem Model
~~~~~~~~~~~~
MenuItems handle navigation structure by linking to pages with customizable templates.

Key Features
-----------
* Automatic timestamp tracking via TimestampedModel
* Version history using django-simple-history
* SEO optimization fields
* Multilingual support (EN/DE)
* Flexible content positioning