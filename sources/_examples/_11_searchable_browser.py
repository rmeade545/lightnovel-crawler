# -*- coding: utf-8 -*-
"""
# TODO: Read the TODOs carefully and remove all existing comments in this file.

This is a sample using the SearchableBrowserTemplate as a template. This template
provides a wrapper around the GeneralBrowserTemplate to support searching.

Put your source file inside the language folder. The `en` folder has too many
files, therefore it is grouped using the first letter of the domain name.
"""
import logging
from typing import Generator, Union

from bs4 import BeautifulSoup, Tag

from lncrawl.models import Chapter, SearchResult, Volume
from lncrawl.templates.browser.searchable import SearchableBrowserTemplate

logger = logging.getLogger(__name__)


# TODO: You can safely delete all [OPTIONAL] methods if you do not need them.
class MyCrawlerName(SearchableBrowserTemplate):
    # TODO: [REQUIRED] Provide the URLs supported by this crawler.
    base_url = ["http://sample.url/"]

    # TODO: [OPTIONAL] Set True if this crawler is for manga/manhua/manhwa.
    has_manga = False

    # TODO: [OPTIONAL] Set True if this source contains machine translations.
    has_mtl = False

    # TODO: [OPTIONAL] This is called before all other methods.
    def initialize(self) -> None:
        # You can customize `TextCleaner` and other necessary things.
        pass

    # TODO: [OPTIONAL] Select novel items found by the query using the browser
    def select_search_items_in_browser(self, query: str) -> Generator[Tag, None, None]:
        # The query here is the input from user.
        #
        # Example:
        #   params = {"searchkey": query}
        #   self.visit(f"{self.home_url}search?{urlencode(params)}")
        #   for elem in self.browser.find_all(".col-content .con .txt h3 a"):
        #       yield elem.as_tag()
        pass

    # TODO: [REQUIRED] Select novel items found in search page from the query
    def select_search_items(self, query: str) -> Generator[Tag, None, None]:
        # The query here is the input from user.
        #
        # Example:
        #   params = {"searchkey": query}
        #   soup = self.post_soup(f"{self.home_url}search?{urlencode(params)}")
        #   yield from soup.select(".col-content .con .txt h3 a")
        #
        # `raise ScraperNotSupported()` to use the browser only.
        pass

    # TODO: [REQUIRED] Parse a tag and return single search result
    def parse_search_item(self, tag: Tag) -> SearchResult:
        # The tag here comes from self.select_search_items
        #
        # Example:
        # return SearchResult(
        #     title=tag.text.strip(),
        #     url=self.absolute_url(tag["href"]),
        # )
        pass

    # TODO: [OPTIONAL] Open the Novel URL in the browser
    def visit_novel_page_in_browser(self) -> BeautifulSoup:
        # self.visit(self.novel_url)
        pass

    # TODO: [OPTIONAL] Parse and return the novel title in the browser
    def parse_title_in_browser(self) -> str:
        # return self.parse_title(self.browser.soup)
        pass

    # TODO: [REQUIRED] Parse and return the novel title
    def parse_title(self, soup: BeautifulSoup) -> str:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        pass

    # TODO: [OPTIONAL] Parse and return the novel cover image in the browser
    def parse_cover_in_browser(self) -> str:
        # return self.parse_cover(self.browser.soup)
        pass

    # TODO: [REQUIRED] Parse and return the novel cover
    def parse_cover(self, soup: BeautifulSoup) -> str:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        pass

    # TODO: [OPTIONAL] Parse and return the novel author in the browser
    def parse_authors_in_browser(self) -> Generator[str, None, None]:
        # yield from self.parse_authors(self.browser.soup)
        pass

    # TODO: [OPTIONAL] Parse and return the novel authors
    def parse_authors(self, soup: BeautifulSoup) -> Generator[str, None, None]:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        #
        # Example 1: <a single author example>
        #   tag = soup.find("strong", string="Author:")
        #   assert tag
        #   yield tag.next_sibling.text.strip()
        #
        # Example 2: <multiple authors example>
        #   for a in soup.select(".m-imgtxt a[href*='/authors/']"):
        #       yield a.text.strip()
        pass

    # TODO: [OPTIONAL] Parse and return the novel author in the browser
    def parse_categorie_in_browser(self) -> Generator[str, None, None]:
        # yield from self.parse_genres(self.browser.soup)
        pass

    # TODO: [OPTIONAL] Parse and return the novel categories or tags
    def parse_genres(self, soup: BeautifulSoup) -> Generator[str, None, None]:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        #
        # See the `parse_authors` example above for a similar implementation.
        pass

    # TODO: [OPTIONAL] Parse and return the novel summary or synopsis in the browser
    def parse_summary_in_browser(self) -> str:
        # return self.parse_summary(self.browser.soup)
        pass

    # TODO: [OPTIONAL] Parse and return the novel summary or synopsis
    def parse_summary(self, soup: BeautifulSoup) -> Generator[str, None, None]:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        pass

    # TODO: [OPTIONAL] Parse and return the volumes and chapters in the browser
    def parse_chapter_list_in_browser(
        self,
    ) -> Generator[Union[Chapter, Volume], None, None]:
        # return self.parse_chapter_list(self.browser.soup)
        pass

    # TODO: [REQUIRED] Parse and set the volumes and chapters
    def parse_chapter_list(
        self, soup: BeautifulSoup
    ) -> Generator[Union[Chapter, Volume], None, None]:
        # The soup here is the result of `self.get_soup(self.novel_url)`
        pass

    # TODO: [OPTIONAL] Open the Chapter URL in the browser
    def visit_chapter_page_in_browser(self, chapter: Chapter) -> None:
        # self.visit(chapter.url)
        pass

    # TODO: [OPTIONAL] Select the tag containing the chapter text in the browser
    def select_chapter_body_in_browser(self) -> Tag:
        # return self.select_chapter_body(self.browser.soup)
        pass

    # TODO: [REQUIRED] Select the tag containing the chapter text
    def select_chapter_body(self, soup: BeautifulSoup) -> Tag:
        # The soup here is the result of `self.get_soup(chapter.url)`
        #
        # Example: return soup.select_one(".m-read .txt")
        pass

    # TODO: [OPTIONAL] Return the index in self.chapters which contains a chapter URL
    def index_of_chapter(self, url: str) -> int:
        # To get more help, check the default implemention in the `Crawler` class.
        pass
