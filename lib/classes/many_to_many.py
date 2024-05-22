# classes/many_to_many.py

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be of type Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("title must be between 5 and 50 characters")

        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("title is immutable")

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) == 0:
            raise ValueError("name cannot be empty")

        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("name is immutable")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None
