from abc import abstractmethod

# AbstractBuilder
class ITextBuilder:
    @abstractmethod
    def add_text(self, value):
        pass

    @abstractmethod
    def add_new_line(self, value):
        pass

# ConcreteBuilder1
class TextBuilder(ITextBuilder):
    def __init__(self):
        self.text = ""

    def add_text(self, value):
        self.text += value

    def add_new_line(self, value):
        self.text += "\n" + value

    def get_text(self):
        return self.text

# ConcreteBuilder2
class HtmlBuilder(ITextBuilder):
    def __init__(self):
        self.html = ""

    def add_text(self, value):
        self.html += "<span>" + value + "</span>"

    def add_new_line(self, value):
        self.html += "<br/>\n"
        self.add_text(value)

    def get_html(self):
        return self.html

# Director
class TextMaker:
    @staticmethod
    def make_text(text_builder):
        text_builder.add_text("first line")
        text_builder.add_new_line("second line")

# Client
textMaker = TextMaker()

textBuilder = TextBuilder()
textMaker.make_text(textBuilder)
text = textBuilder.get_text()

# text: first line
#       second line

htmlBuilder = HtmlBuilder()
textMaker.make_text(htmlBuilder)
html = htmlBuilder.get_html()

# html: <span>first line</span><br/>
#       <span>second line</span><br/>

print(text)
print(html)
