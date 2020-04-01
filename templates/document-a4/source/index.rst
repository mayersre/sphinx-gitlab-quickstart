.. Documentation project for {{ values.project }} created by 
   {{ values.author }} with sphinx-gitlab-quickstart on {{ values.now }}.

.. Please add your own content between copyright and glossary
.. Bitte Inhalte zwischen copyright und glossar einfügen. Inhalt 1+2 als Beispiel.
.. If you want to change the author, please change in conf.py und pdf_conf/conf.py.
.. Wenn Sie den Author ändern möchten, bitte die Zeile mit author= in conf.py und pdf_conf/conf.py ändern

{{ values.project }}
{{ values.project_underline }}

.. only:: html
    
   Here you can download a :download:`Pdf Version <{{ values.project_fn }}.pdf>` of the document
   after the first build.

.. only:: html
    
   Here you can download a :download:`docx Version <{{ values.project_fn }}.docx>` of the document
   after the first build.


.. toctree::
   :maxdepth: 5
   :caption: {% if values.language ==  'en' %}   Index{% else %}   Inhaltsverzeichnis{% endif %}
   :numbered:
   
{% if values.language ==  'en' %}   copyright_en{% else %}   copyright{% endif %}
   content1
   cheatsheet
   glossary
   version

.. bibliography:: ../library/common/references.bib
   :cited:

