# Automatic aspect extractor

_Tool for aspect extraction from Russian texts_
## Installation and preparation

### How to use

```python
from aspect_extractor.aspect_extractor import AspectExtractor

extractor = AspectExtractor()
text = "Определена модель для визуализации связей между объектами и их атрибутами в различных процессах. "
       "На основании модели разработан универсальный абстрактный компонент графического пользовательского интерфейса и приведены примеры его программной реализации. "
       "Также проведена апробация компонента для решения прикладной задачи по извлечению информации из документов."
print(extractor.stringify_extracted_aspects(text = text))
```