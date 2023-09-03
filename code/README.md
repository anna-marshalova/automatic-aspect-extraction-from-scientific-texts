# Automatic aspect extractor

_Tool for aspect extraction from Russian texts_
## Installation and preparation
To install:

`git clone https://github.com/anna-marshalova/automatic-aspect-extraction-from-scientific-texts`

Please download weights file from [here](https://disk.yandex.ru/d/31i9D65Z25cj6Q)
and put it to `aspect_extractor/weights`.

### How to use

```python
from aspect_extractor.aspect_extractor import AspectExtractor

extractor = AspectExtractor()
text = "Определена модель для визуализации связей между объектами и их атрибутами в различных процессах. "
       "На основании модели разработан универсальный абстрактный компонент графического пользовательского интерфейса и приведены примеры его программной реализации. "
       "Также проведена апробация компонента для решения прикладной задачи по извлечению информации из документов."
print(extractor.stringify_extracted_aspects(text = text))
```
